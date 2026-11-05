"""Environment validation without UI, database, or provider initialization."""

from collections.abc import Mapping
from dataclasses import dataclass, field
import os
from pathlib import Path
import stat


# Explicit initial ISO 4217 subset; no monetary arithmetic is defined here.
# Source: SIX ISO 4217 List One (linked in docs/SETUP.md).
SUPPORTED_CURRENCIES = {"EUR": 2, "GBP": 2, "JPY": 0, "KWD": 3, "TRY": 2, "USD": 2}
PREFIX = "FINANCE_TRACKER_"


class ConfigurationError(ValueError):
    """An actionable error whose text never contains environment values."""


@dataclass(frozen=True)
class Configuration:
    reporting_currency: str
    minor_unit_scale: int
    database_path: Path = field(repr=False)
    gemini_enabled: bool = False
    telegram_enabled: bool = False
    warnings: tuple[str, ...] = ()


def _database_path(raw: str, base_dir: Path) -> Path:
    message = (
        "FINANCE_TRACKER_DATABASE_PATH must name a local SQLite file in an existing "
        "owner-only, readable and writable directory. See docs/SETUP.md."
    )
    if not raw.strip() or raw == ":memory:" or "://" in raw or raw.startswith("file:"):
        raise ConfigurationError(message)
    try:
        path = Path(raw).expanduser()
        if not path.is_absolute():
            path = base_dir / path
        path = path.resolve()
        parent = path.parent
        parent_stat = parent.stat()
        if (
            not parent.is_dir()
            or parent_stat.st_uid != os.getuid()
            or stat.S_IMODE(parent_stat.st_mode) & 0o077
            or stat.S_IMODE(parent_stat.st_mode) & 0o700 != 0o700
            or not os.access(parent, os.R_OK | os.W_OK | os.X_OK)
        ):
            raise ConfigurationError(message)
        if path.exists():
            file_stat = path.stat()
            if (
                not path.is_file()
                or file_stat.st_uid != os.getuid()
                or stat.S_IMODE(file_stat.st_mode) & 0o077
                or stat.S_IMODE(file_stat.st_mode) & 0o600 != 0o600
                or not os.access(path, os.R_OK | os.W_OK)
            ):
                raise ConfigurationError(message)
        return path
    except (OSError, ValueError, RuntimeError):
        raise ConfigurationError(message) from None


def _integration_warnings(env: Mapping[str, str], integration: str) -> list[str]:
    variable = f"{PREFIX}{integration}_ENABLED"
    flag = env.get(variable, "false").strip().lower()
    if flag == "false":
        return []
    if flag != "true":
        return [f"{variable} must be true or false; the integration remains disabled."]
    credentials = (
        ("GEMINI_API_KEY",)
        if integration == "GEMINI"
        else ("TELEGRAM_BOT_TOKEN", "TELEGRAM_CHAT_ID")
    )
    missing = [name for name in credentials if not env.get(name, "").strip()]
    if missing:
        return [f"{integration} configuration incomplete: set {', '.join(missing)}. "
                "The integration remains disabled; local startup is available."]
    return [f"{integration} is unavailable in this version and remains disabled."]


def load_configuration(
    env: Mapping[str, str] | None = None, *, base_dir: Path | None = None
) -> Configuration:
    """Read process environment; never create paths or retain credentials.

    Explicit environment and base directory make validation independently testable.
    Currency persistence/immutability belong to later tasks, not this runtime shell.
    """
    env = os.environ if env is None else env
    currency = env.get(f"{PREFIX}REPORTING_CURRENCY", "").strip().upper()
    if currency not in SUPPORTED_CURRENCIES:
        raise ConfigurationError(
            "FINANCE_TRACKER_REPORTING_CURRENCY is required; choose EUR, GBP, JPY, "
            "KWD, TRY, or USD explicitly. See docs/SETUP.md."
        )
    scale = env.get(f"{PREFIX}MINOR_UNIT_SCALE", "").strip()
    if scale != str(SUPPORTED_CURRENCIES[currency]):
        raise ConfigurationError(
            "FINANCE_TRACKER_MINOR_UNIT_SCALE is required and must match the "
            "selected currency. See supported pairs in docs/SETUP.md."
        )
    database_path = _database_path(
        env.get(f"{PREFIX}DATABASE_PATH", "data/finance_tracker.sqlite3"),
        Path.cwd() if base_dir is None else base_dir,
    )
    warnings = tuple(
        _integration_warnings(env, "GEMINI") + _integration_warnings(env, "TELEGRAM")
    )
    return Configuration(currency, int(scale), database_path, warnings=warnings)
