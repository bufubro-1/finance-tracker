"""Exact rules for synthetic USD openings; no ORM, UI, clocks or network."""

from decimal import Decimal, localcontext
import re
import unicodedata


PROTOTYPE_CURRENCY = "USD"
PROTOTYPE_SCALE = 2
MAX_MINOR = 2**63 - 1
MAX_NAME_LENGTH = 100


def clean_account_name(value):
    if not isinstance(value, str):
        raise ValueError("Bir hesap adı girin.")
    name = unicodedata.normalize("NFKC", value).strip()
    if not name or len(name) > MAX_NAME_LENGTH:
        raise ValueError("1 ile 100 karakter arasında bir hesap adı girin.")
    if any(unicodedata.category(char).startswith("C") for char in name):
        raise ValueError("Hesap adı kontrol karakteri veya görünmez karakter içeremez.")
    return name


def account_name_key(name):
    return clean_account_name(name).casefold()


def validate_currency(value):
    if value != PROTOTYPE_CURRENCY:
        raise ValueError("USD seçin. Bu deneme prototipi yalnızca 2 ondalık basamaklı USD tutarlarını destekler.")
    return value


def parse_opening_balance(value):
    """Reject excess digits rather than rounding; floats are never accepted."""
    if (not isinstance(value, str) or len(value) > 64
            or not re.fullmatch(r"[0-9]+(?:\.[0-9]{1,2})?", value.strip())):
        raise ValueError("Sıfır veya pozitif bir tutar girin. Ondalık ayırıcı olarak nokta ve en fazla 2 ondalık basamak kullanın (örnek: 1000.00).")
    with localcontext() as context:
        context.prec = 80
        amount = Decimal(value.strip())
        minor = amount * 100
        if minor > MAX_MINOR:
            raise ValueError("Açılış bakiyesi en fazla 92,233,720,368,547,758.07 USD olabilir.")
        return int(minor)


def format_minor(value):
    if type(value) is not int or value < 0:
        raise ValueError("Expected a nonnegative integer balance.")
    whole, fraction = divmod(value, 100)
    return f"{whole:,}.{fraction:02d}"
