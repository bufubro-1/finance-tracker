"""Owner-scoped synthetic openings and reads; no integration or movement writes."""

from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
from uuid import UUID

from django.core.exceptions import PermissionDenied
from django.db import IntegrityError, OperationalError, transaction
from django.db.models import Prefetch

from .account_rules import (
    account_name_key, clean_account_name, format_minor, parse_opening_balance,
    validate_currency,
)
from .models import Account, BalanceObservation, UserSettings


class CreationError(ValueError):
    def __init__(self, message, field=None):
        super().__init__(message)
        self.field = field


@dataclass(frozen=True)
class CreationResult:
    account: Account
    created: bool


def require_owner(owner):
    """Prototype ordinary identities only; no application-admin bypass."""
    if (not owner.is_authenticated or not owner.pk or not owner.is_active
            or owner.is_staff or owner.is_superuser):
        raise PermissionDenied


def utc_now():
    return datetime.now(timezone.utc)


def _replay(account, fingerprint):
    if account.creation_fingerprint != fingerprint:
        raise CreationError("Bu gönderim daha önce farklı bilgilerle kullanıldı. Yeni bir hesap oluşturma formu açın.")
    return CreationResult(account, False)


def create_savings_account(owner, *, name, currency, opening_balance, submission_key, clock=utc_now):
    require_owner(owner)
    name = clean_account_name(name)
    normalized_name = account_name_key(name)
    currency = validate_currency(currency)
    minor = parse_opening_balance(opening_balance)
    key = UUID(str(submission_key))
    canonical = json.dumps([name, currency, 2, minor], ensure_ascii=True, separators=(",", ":"))
    fingerprint = hashlib.sha256(canonical.encode("ascii")).hexdigest()
    try:
        with transaction.atomic():
            existing = Account.objects.filter(owner=owner, creation_key=key).first()
            if existing:
                return _replay(existing, fingerprint)
            instant = clock()
            if not isinstance(instant, datetime) or instant.utcoffset() is None:
                raise ValueError("Opening clock must supply an aware datetime.")
            instant = instant.astimezone(timezone.utc)
            preferences, _ = UserSettings.objects.get_or_create(
                owner=owner, defaults={"reporting_currency": currency, "minor_unit_scale": 2},
            )
            if (preferences.reporting_currency, preferences.minor_unit_scale) != (currency, 2):
                raise CreationError("Mevcut para birimi ayarları desteklenmiyor. Hesap kaydedilmedi.", "currency")
            account = Account.objects.create(
                owner=owner, name=name, normalized_name=normalized_name,
                creation_key=key, creation_fingerprint=fingerprint, created_at=instant,
            )
            BalanceObservation.objects.create(
                account=account, cash_minor=minor, effective_date=instant.date(), recorded_at=instant,
            )
            return CreationResult(account, True)
    except IntegrityError:
        # Another request may have committed the same intent. Query only after rollback.
        existing = Account.objects.filter(owner=owner, creation_key=key).first()
        if existing:
            return _replay(existing, fingerprint)
        if Account.objects.filter(owner=owner, normalized_name=normalized_name).exists():
            raise CreationError("Bu adla bir hesabınız zaten var. Farklı bir ad seçin.", "name") from None
        raise
    except OperationalError as error:
        if "locked" not in str(error).lower():
            raise
        raise CreationError("Yerel veritabanı meşgul. Formu tekrar gönderin; açılış bakiyesi yalnızca bir kez kaydedilir.") from None


def recorded_accounts(owner):
    """One owner-scoped query set supplies both cards and the exact subtotal."""
    require_owner(owner)
    with transaction.atomic():
        preferences = UserSettings.objects.filter(owner=owner).first()
        accounts = list(Account.objects.filter(owner=owner).prefetch_related(Prefetch(
            "observations", queryset=BalanceObservation.objects.order_by("pk"), to_attr="opening_records",
        )))
    currency_ok = preferences is not None and (
        preferences.reporting_currency, preferences.minor_unit_scale
    ) == ("USD", 2)
    total = 0
    complete = True
    cards = []
    for account in accounts:
        known = currency_ok and len(account.opening_records) == 1
        observation = account.opening_records[0] if known else None
        if known:
            total += observation.cash_minor
        else:
            complete = False
        cards.append({
            "id": account.pk, "name": account.name,
            "currency": "USD" if currency_ok else "Desteklenmeyen para birimi",
            "balance": format_minor(observation.cash_minor) if known else None,
            "effective_date": observation.effective_date if known else None,
        })
    return {
        "accounts": cards, "account_count": len(cards), "total_balance": format_minor(total),
        "total_complete": complete, "currency": "USD" if currency_ok else None,
    }
