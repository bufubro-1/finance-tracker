"""TASK-004A1: exact openings, P1-03/04/05/06 and scoped TC-039/040/047/053/058/059."""

from pathlib import Path
import subprocess
import sys
import time
import socket
from urllib.error import URLError
from urllib.request import ProxyHandler, Request, build_opener

import pytest

from finance_tracker.django_app.account_rules import MAX_MINOR, format_minor, parse_opening_balance


@pytest.mark.parametrize("text, minor", [
    ("0", 0), ("0.00", 0), ("0.01", 1), ("0.1", 10), ("1000.00", 100000),
    ("92233720368547758.07", MAX_MINOR),
])
def test_exact_parser_and_formatter(text, minor):
    assert parse_opening_balance(text) == minor
    assert parse_opening_balance(format_minor(minor).replace(",", "")) == minor


@pytest.mark.parametrize("invalid", [
    "", " ", "-1", "-0.00", "+1", "1.001", "1.230", "NaN", "Infinity", "-Infinity",
    "1e2", "1,000.00", "1,23", "1.", ".25", "１２.３４", "92233720368547758.08",
    "9" * 65, 0.1, float("nan"), None, True,
])
def test_parser_rejects_invalid_precision_and_non_text(invalid):
    with pytest.raises(ValueError):
        parse_opening_balance(invalid)


SETUP = r'''
import re
import secrets
import socket
from uuid import uuid4, UUID
from datetime import datetime, timezone, timedelta
from unittest.mock import patch
def reject(*args, **kwargs):
    raise AssertionError("Unexpected external call")
socket.socket.connect = reject
import django
django.setup()
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.db import connection, IntegrityError, OperationalError, transaction
from django.test import Client
from django.test.utils import setup_test_environment
from finance_tracker.django_app.models import Account, BalanceObservation, UserSettings
from finance_tracker.django_app.services import create_savings_account, recorded_accounts, CreationError
setup_test_environment()
User = get_user_model()
password = secrets.token_urlsafe(24)
owner = User.objects.create_user("owner@example.invalid", password)
client = Client(HTTP_HOST="127.0.0.1", enforce_csrf_checks=True)
client.force_login(owner)
def csrf(client, path="/accounts/create/"):
    response = client.get(path)
    assert response.status_code == 200
    return re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', response.content.decode())[1]
def payload(client=client, **overrides):
    data = {"name": "Example Saved Savings", "currency": "USD", "opening_balance": "1000.00",
            "submission_key": str(uuid4()), "csrfmiddlewaretoken": csrf(client)}
    data.update(overrides)
    return data
def create(client=client, **overrides):
    return client.post("/accounts/create/", payload(client, **overrides))
'''


def test_real_login_creation_exact_storage_and_display(run_django, migrated_prototype, prototype_env):
    run_django(SETUP + r'''
client.logout()
token = csrf(client, "/login/")
response = client.post("/login/", {"username": owner.email, "password": password, "csrfmiddlewaretoken": token})
assert response.status_code == 302
page = client.get("/accounts/create/")
form = page.context["form"]
assert form["currency"].value() is None
key = str(form["submission_key"].value())
assert create(name="  Holiday Savings  ", opening_balance="1234.56", submission_key=key).status_code == 302
account = Account.objects.get()
assert account.owner_id == owner.pk and account.name == "Holiday Savings"
assert account.kind == "savings" and str(account.creation_key) == key
settings = UserSettings.objects.get(owner=owner)
assert (settings.reporting_currency, settings.minor_unit_scale) == ("USD", 2)
observation = BalanceObservation.objects.get(account=account)
assert type(observation.cash_minor) is int and observation.cash_minor == 123456
with connection.cursor() as cursor:
    cursor.execute("SELECT cash_minor, typeof(cash_minor) FROM django_app_balanceobservation")
    assert cursor.fetchone() == (123456, "integer")
for path in ("/accounts/?saved=" + str(account.pk), "/"):
    response = client.get(path)
    html = response.content.decode()
    assert response.status_code == 200 and "USD" in html and "1,234.56" in html
    assert "no-store" in response["Cache-Control"]
    assert response.context["total_balance"] == "1,234.56"
html = client.get("/accounts/?saved=" + str(account.pk)).content.decode()
assert 'role="status"' in html and "kaydedildi" in html and "Kaydedildi · Deneme hesabı" in html
assert "Kaydedilmez" in html and "hiçbir toplama dahil edilmez" in html
assert Account.objects.count() == BalanceObservation.objects.count() == 1
assert not any("movement" in table or "transaction" in table for table in connection.introspection.table_names())
''')
    assert not Path(prototype_env["FINANCE_TRACKER_DATABASE_PATH"]).exists()


@pytest.mark.parametrize("changes, error_field", [
    ({"name": ""}, "name"), ({"name": " "}, "name"), ({"name": "a" * 101}, "name"),
    ({"name": "bad\x00name"}, "name"), ({"name": "bad\u200bname"}, "name"),
    ({"currency": ""}, "currency"), ({"currency": "EUR"}, "currency"),
    ({"currency": "usd"}, "currency"), ({"opening_balance": ""}, "opening_balance"),
    ({"opening_balance": "-0.01"}, "opening_balance"), ({"opening_balance": "NaN"}, "opening_balance"),
    ({"opening_balance": "1.234"}, "opening_balance"),
    ({"opening_balance": "92233720368547758.08"}, "opening_balance"),
    ({"submission_key": ""}, "submission_key"), ({"submission_key": "invalid"}, "submission_key"),
])
def test_form_validation_preserves_input_and_writes_nothing(run_django, migrated_prototype, changes, error_field):
    run_django(SETUP + "\nchanges = " + repr(changes) + "\nerror_field = " + repr(error_field) + r'''
data = payload(**changes)
response = client.post("/accounts/create/", data)
assert response.status_code == 200
form = response.context["form"]
assert error_field in form.errors
assert form["name"].value() == data["name"]
assert form["opening_balance"].value() == data["opening_balance"]
assert str(form["submission_key"].value()) == data["submission_key"]
html = response.content.decode()
assert 'role="alert"' in html and "Girdiğiniz bilgiler korundu" in html
assert not Account.objects.exists() and not BalanceObservation.objects.exists() and not UserSettings.objects.exists()
''')


def test_names_are_normalized_unique_per_owner_and_escaped(run_django, migrated_prototype):
    run_django(SETUP + r'''
assert create(name="  Ｓａｖｉｎｇｓ  ").status_code == 302
assert Account.objects.get().name == "Savings"
response = create(name="SAVINGS")
assert response.status_code == 200 and "name" in response.context["form"].errors
assert Account.objects.count() == BalanceObservation.objects.count() == 1
assert create(name="<script>synthetic</script>", opening_balance="0").status_code == 302
html = client.get("/accounts/").content.decode()
assert "<script>synthetic</script>" not in html and "&lt;script&gt;synthetic&lt;/script&gt;" in html
assert "0.00" in html
''')


def test_owned_lists_totals_and_forged_identifiers(run_django, migrated_prototype):
    run_django(SETUP + r'''
other = User.objects.create_user("other@example.invalid")
other_client = Client(HTTP_HOST="127.0.0.1", enforce_csrf_checks=True)
other_client.force_login(other)
key = str(uuid4())
assert create(name="Same name", opening_balance="0.10", submission_key=key, owner_id=other.pk, owner=other.pk).status_code == 302
assert create(other_client, name="Same name", opening_balance="500", submission_key=key, owner_id=owner.pk).status_code == 302
assert create(other_client, name="Other private name", opening_balance="250").status_code == 302
assert create(name="Second owned", opening_balance="0.20").status_code == 302
for browser, expected_owner, expected_total, forbidden in (
    (client, owner, "0.30", "Other private name"), (other_client, other, "750.00", "Second owned"),
):
    foreign = Account.objects.exclude(owner=expected_owner).first()
    for path in ("/?owner=" + str(foreign.owner_id), "/accounts/?saved=" + str(foreign.pk)):
        response = browser.get(path)
        assert response.context["total_balance"] == expected_total
        assert forbidden not in response.content.decode()
        if "saved=" in path:
            assert not response.context["saved"]
    assert browser.post("/accounts/", {"owner": foreign.owner_id}).status_code == 403  # missing CSRF
    assert browser.post("/accounts/", {"csrfmiddlewaretoken": csrf(browser)}).status_code == 405
    for suffix in ("", "edit/", "delete/"):
        assert browser.get(f"/accounts/{foreign.pk}/{suffix}").status_code == 404
assert Account.objects.filter(owner=owner).count() == 2
assert Account.objects.filter(owner=other).count() == 2
assert BalanceObservation.objects.count() == 4
''')


def test_anonymous_csrf_and_disallowed_methods(run_django, migrated_prototype):
    run_django(SETUP + r'''
anonymous = Client(HTTP_HOST="127.0.0.1", enforce_csrf_checks=True)
token = csrf(anonymous, "/login/")
for path in ("/", "/accounts/", "/accounts/create/"):
    response = anonymous.get(path)
    assert response.status_code == 302 and response.url.startswith("/login/?next=")
assert anonymous.post("/accounts/create/", {"csrfmiddlewaretoken": token}).status_code == 302
data = payload()
for overrides in ({"csrfmiddlewaretoken": ""}, {"csrfmiddlewaretoken": "invalid"}):
    assert client.post("/accounts/create/", dict(data, **overrides)).status_code == 403
assert client.post("/accounts/create/", data, HTTP_ORIGIN="http://outside.example.invalid").status_code == 403
assert client.put("/accounts/create/", HTTP_X_CSRFTOKEN=csrf(client)).status_code == 405
assert not Account.objects.exists() and not UserSettings.objects.exists()
''')


@pytest.mark.parametrize("flag", ["is_staff", "is_superuser"])
def test_privileged_identity_has_no_financial_path(run_django, migrated_prototype, flag):
    run_django(SETUP + "\nflag = " + repr(flag) + r'''
assert create().status_code == 302
setattr(owner, flag, True)
owner.save()
for path in ("/", "/accounts/", "/accounts/create/"):
    response = client.get(path)
    assert response.status_code == 403 and "Example Saved Savings" not in response.content.decode()
try:
    recorded_accounts(owner)
except PermissionDenied:
    pass
else:
    raise AssertionError("Privileged identity acquired financial access")
assert client.post("/accounts/create/", {"csrfmiddlewaretoken": client.cookies["csrftoken"].value}).status_code == 403
assert Account.objects.count() == 1
''')


def test_duplicate_intent_conflict_and_distinct_equal_balances(run_django, migrated_prototype):
    run_django(SETUP + r'''
data = payload(opening_balance="0.10")
first = client.post("/accounts/create/", data)
second = client.post("/accounts/create/", data)
assert first.status_code == second.status_code == 302 and first.url == second.url
for _ in range(2):
    assert client.get(first.url).status_code == 200
assert Account.objects.count() == BalanceObservation.objects.count() == 1
# Equivalent decimal spelling represents the same exact intent.
assert client.post("/accounts/create/", dict(data, opening_balance="0.1")).url == first.url
response = client.post("/accounts/create/", dict(data, opening_balance="0.20"))
assert response.status_code == 200 and response.context["form"].non_field_errors()
assert BalanceObservation.objects.get().cash_minor == 10
assert create(name="Different account", opening_balance="0.10").status_code == 302
assert Account.objects.count() == 2 and client.get("/").context["total_balance"] == "0.20"
''')


def test_atomic_failure_rolls_back_guard_settings_and_opening(run_django, migrated_prototype):
    run_django(SETUP + r'''
key = uuid4()
original = BalanceObservation.objects.create
def fail_after_observation(**kwargs):
    original(**kwargs)
    raise RuntimeError("synthetic injected failure")
with patch.object(BalanceObservation.objects, "create", side_effect=fail_after_observation):
    try:
        create_savings_account(owner, name="Atomic", currency="USD", opening_balance="1", submission_key=key)
    except RuntimeError:
        pass
    else:
        raise AssertionError("Injected failure not raised")
assert not Account.objects.exists() and not BalanceObservation.objects.exists() and not UserSettings.objects.exists()
result = create_savings_account(owner, name="Atomic", currency="USD", opening_balance="1", submission_key=key)
assert result.created and Account.objects.count() == BalanceObservation.objects.count() == 1
''')


def test_busy_database_returns_retryable_error_without_partial_writes(run_django, migrated_prototype):
    run_django(SETUP + r'''
data = payload()
with patch.object(Account.objects, "create", side_effect=OperationalError("database is locked")):
    response = client.post("/accounts/create/", data)
assert response.status_code == 200 and "meşgul" in str(response.context["form"].non_field_errors())
assert not Account.objects.exists() and not UserSettings.objects.exists()
assert client.post("/accounts/create/", data).status_code == 302
''')


def test_exact_maximum_totals_and_synthetic_utc_clock(run_django, migrated_prototype):
    run_django(SETUP + r'''
instant = datetime(2026, 11, 5, 1, 0, tzinfo=timezone(timedelta(hours=3)))
for name in ("Maximum one", "Maximum two"):
    create_savings_account(owner, name=name, currency="USD", opening_balance="92233720368547758.07",
        submission_key=uuid4(), clock=lambda: instant)
assert client.get("/").context["total_balance"] == "184,467,440,737,095,516.14"
for observation in BalanceObservation.objects.all():
    assert observation.cash_minor == 2**63 - 1
    assert str(observation.effective_date) == "2026-11-04"
    assert observation.recorded_at == instant.astimezone(timezone.utc)
try:
    create_savings_account(owner, name="Invalid clock", currency="USD", opening_balance="1",
        submission_key=uuid4(), clock=lambda: datetime(2026, 11, 5))
except ValueError:
    pass
else:
    raise AssertionError("Naive clock accepted")
assert Account.objects.count() == 2
for value in (0.1, float("nan")):
    try:
        create_savings_account(owner, name="Float", currency="USD", opening_balance=value, submission_key=uuid4())
    except ValueError:
        pass
    else:
        raise AssertionError("Float financial input accepted")
''')


def test_database_constraints_and_missing_observation_is_not_zero(run_django, migrated_prototype):
    run_django(SETUP + r'''
assert create(opening_balance="1.23").status_code == 302
account = Account.objects.get()
for changes in ({"cash_minor": -1}, {"account": account, "cash_minor": 1}):
    try:
        with transaction.atomic():
            BalanceObservation.objects.create(account=changes.get("account", account), cash_minor=changes["cash_minor"],
                effective_date=datetime(2026, 11, 5).date(), recorded_at=datetime.now(timezone.utc))
    except IntegrityError:
        pass
    else:
        raise AssertionError("Invalid observation accepted")
other = User.objects.create_user("unsupported@example.invalid")
try:
    with transaction.atomic():
        UserSettings.objects.create(owner=other, reporting_currency="EUR", minor_unit_scale=2)
except IntegrityError:
    pass
else:
    raise AssertionError("Unsupported currency persisted")
Account.objects.create(owner=owner, name="Missing observation", normalized_name="missing observation",
    creation_key=uuid4(), creation_fingerprint="0" * 64, created_at=datetime.now(timezone.utc))
response = client.get("/")
assert not response.context["total_complete"] and response.context["total_balance"] == "1.23"
assert "Eksik" in response.content.decode()
assert "Açılış bakiyesi mevcut değil" in client.get("/accounts/").content.decode()
''')


def test_empty_states_and_form_accessibility(run_django, migrated_prototype):
    run_django(SETUP + r'''
response = client.get("/")
assert not response.context["accounts"] and "Henüz kayıtlı bakiye yok" in response.content.decode()
assert "1,000.00" not in response.content.decode()
html = client.get("/accounts/").content.decode()
assert "Henüz kaydedilmiş hesap yok" in html and 'href="/accounts/create/"' in html
assert "hiçbir toplama dahil edilmez" in html and "kaydedilmez" in html
response = create(opening_balance="1.234")
html = response.content.decode()
for name in ("name", "currency", "opening_balance"):
    assert f'<label for="id_{name}">' in html
    assert f'id="id_{name}_helptext"' in html
assert 'aria-invalid="true"' in html and 'id_opening_balance_error' in html
assert 'aria-describedby="id_opening_balance_helptext id_opening_balance_error"' in html
assert 'name="viewport"' in html and 'Yalnızca örnek veriler' in html
assert 'type="hidden" name="submission_key"' in html
assert 'name="owner"' not in html and 'name="owner_id"' not in html
''')


def test_opening_and_replay_survive_process_restart(run_django, migrated_prototype, prototype_env):
    legacy = Path(prototype_env["FINANCE_TRACKER_DATABASE_PATH"])
    legacy.write_bytes(b"isolated synthetic legacy sentinel")
    legacy.chmod(0o600)
    run_django(SETUP + r'''
result = create_savings_account(owner, name="Restart savings", currency="USD", opening_balance="0.29",
    submission_key=UUID("6b8ce368-335d-48b5-adb8-60bd12e26591"))
assert result.created
''')
    run_django(r'''
import django
django.setup()
from uuid import UUID
from django.contrib.auth import get_user_model
from finance_tracker.django_app.models import Account, BalanceObservation
from finance_tracker.django_app.services import create_savings_account, recorded_accounts
owner = get_user_model().objects.get(email="owner@example.invalid")
result = create_savings_account(owner, name="Restart savings", currency="USD", opening_balance="0.29",
    submission_key=UUID("6b8ce368-335d-48b5-adb8-60bd12e26591"))
assert not result.created
assert Account.objects.count() == BalanceObservation.objects.count() == 1
assert recorded_accounts(owner)["total_balance"] == "0.29"
''')
    assert legacy.read_bytes() == b"isolated synthetic legacy sentinel"


def test_additive_migration_preserves_existing_identity_and_session(run_django):
    run_django(r'''
import os
os.umask(0o077)
import django
django.setup()
from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from django.test import Client
call_command("migrate", "identity", interactive=False, verbosity=0)
call_command("migrate", "sessions", interactive=False, verbosity=0)
owner = get_user_model().objects.create_user("existing@example.invalid", "synthetic-migration-password")
client = Client(HTTP_HOST="127.0.0.1")
client.force_login(owner)
cookie = client.cookies["sessionid"].value
original_hash = owner.password
call_command("migrate", interactive=False, verbosity=0)
call_command("makemigrations", check=True, dry_run=True, verbosity=0)
call_command("migrate", check_unapplied=True, verbosity=0)
owner.refresh_from_db()
assert owner.password == original_hash and owner.check_password("synthetic-migration-password")
assert Session.objects.filter(session_key=cookie).exists()
assert client.get("/accounts/").status_code == 200
from finance_tracker.django_app.models import Account
assert not Account.objects.exists()
''')


def test_saved_accounts_survive_application_restart(run_django, migrated_prototype, prototype_env, tmp_path):
    run_django(SETUP + r'''
assert create(name="Server restart savings", opening_balance="9876.54").status_code == 302
from pathlib import Path
Path("synthetic-session").write_text(client.cookies["sessionid"].value)
''')
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        port = probe.getsockname()[1]
    opener = build_opener(ProxyHandler({}))
    cookie = (tmp_path / "synthetic-session").read_text()
    for restart in range(2):
        with (tmp_path / f"restart-{restart}.log").open("w") as output:
            process = subprocess.Popen(
                [sys.executable, "-m", "finance_tracker.django_app", "--port", str(port)],
                cwd=tmp_path, env=prototype_env, stdout=output, stderr=subprocess.STDOUT,
            )
            try:
                deadline = time.monotonic() + 20
                while time.monotonic() < deadline:
                    assert process.poll() is None
                    try:
                        with opener.open(Request(f"http://127.0.0.1:{port}/", headers={"Cookie": f"sessionid={cookie}"}), timeout=1) as response:
                            assert "9,876.54" in response.read().decode()
                        break
                    except (URLError, TimeoutError):
                        time.sleep(.1)
                else:
                    raise AssertionError("Restarted application did not become ready")
                with opener.open(Request(f"http://127.0.0.1:{port}/accounts/", headers={"Cookie": f"sessionid={cookie}"}), timeout=2) as response:
                    html = response.read().decode()
                    assert "Server restart savings" in html and "9,876.54" in html
            finally:
                process.terminate()
                process.wait(timeout=10)
    assert not Path(prototype_env["FINANCE_TRACKER_DATABASE_PATH"]).exists()
