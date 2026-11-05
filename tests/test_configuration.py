"""TASK-001: TC-001/002 and scoped TC-038/041 configuration checks."""

from pathlib import Path
import os
import subprocess
import sys

import pytest

from finance_tracker.config import ConfigurationError, load_configuration


@pytest.mark.parametrize("currency,scale", [("EUR", 2), ("GBP", 2), ("JPY", 0),
                                           ("KWD", 3), ("TRY", 2), ("USD", 2)])
def test_explicit_currency_and_scale(configuration_env, currency, scale):
    configuration_env.update(FINANCE_TRACKER_REPORTING_CURRENCY=currency,
                             FINANCE_TRACKER_MINOR_UNIT_SCALE=str(scale))
    config = load_configuration(configuration_env)
    assert (config.reporting_currency, config.minor_unit_scale) == (currency, scale)
    assert not config.database_path.exists()  # Configuration must not open SQLite.
    assert not config.gemini_enabled and not config.telegram_enabled
    assert config.warnings == ()


@pytest.mark.parametrize("currency,scale,expected", [
    (" usd ", " 2 ", "USD"), ("jpy", " 0", "JPY"), (" kwd", "3 ", "KWD"),
])
def test_currency_and_scale_normalization(configuration_env, currency, scale, expected):
    configuration_env.update(FINANCE_TRACKER_REPORTING_CURRENCY=currency,
                             FINANCE_TRACKER_MINOR_UNIT_SCALE=scale)
    config = load_configuration(configuration_env)
    assert config.reporting_currency == expected
    assert config.minor_unit_scale == int(scale)


@pytest.mark.parametrize("value", [None, "", " ", "TEST", "ZZZ", "US", "USD\nsecret"])
def test_currency_required_and_supported(configuration_env, value):
    if value is None:
        configuration_env.pop("FINANCE_TRACKER_REPORTING_CURRENCY")
    else:
        configuration_env["FINANCE_TRACKER_REPORTING_CURRENCY"] = value
    with pytest.raises(ConfigurationError, match="REPORTING_CURRENCY"):
        load_configuration(configuration_env)


@pytest.mark.parametrize("value", [None, "", "-1", "3", "2.0", "NaN", "100", "secret"])
def test_scale_required_and_matches_currency(configuration_env, value):
    if value is None:
        configuration_env.pop("FINANCE_TRACKER_MINOR_UNIT_SCALE")
    else:
        configuration_env["FINANCE_TRACKER_MINOR_UNIT_SCALE"] = value
    with pytest.raises(ConfigurationError, match="MINOR_UNIT_SCALE"):
        load_configuration(configuration_env)


@pytest.mark.parametrize("integration", ["GEMINI", "TELEGRAM"])
@pytest.mark.parametrize("flag", ["true", "false", "invalid-secret"])
def test_integrations_fail_closed_without_credentials(configuration_env, integration, flag):
    configuration_env[f"FINANCE_TRACKER_{integration}_ENABLED"] = flag
    config = load_configuration(configuration_env)
    assert not config.gemini_enabled and not config.telegram_enabled
    assert bool(config.warnings) == (flag != "false")
    assert "invalid-secret" not in repr(config)
    if flag == "true":
        assert "configuration incomplete" in config.warnings[0]


@pytest.mark.parametrize("integration", ["GEMINI", "TELEGRAM"])
@pytest.mark.parametrize("flag", [" FALSE ", " TrUe "])
def test_integration_flag_normalization(configuration_env, integration, flag):
    configuration_env[f"FINANCE_TRACKER_{integration}_ENABLED"] = flag
    config = load_configuration(configuration_env)
    assert not config.gemini_enabled and not config.telegram_enabled
    assert bool(config.warnings) == (flag.strip().lower() == "true")


def test_credential_presence_never_activates_adapters(configuration_env):
    configuration_env.update(GEMINI_API_KEY="synthetic-secret",
                             TELEGRAM_BOT_TOKEN="synthetic-secret",
                             TELEGRAM_CHAT_ID="synthetic-secret")
    config = load_configuration(configuration_env)
    assert config.warnings == ()
    configuration_env.update(FINANCE_TRACKER_GEMINI_ENABLED="true",
                             FINANCE_TRACKER_TELEGRAM_ENABLED="true")
    config = load_configuration(configuration_env)
    assert len(config.warnings) == 2
    assert not config.gemini_enabled and not config.telegram_enabled
    assert "synthetic-secret" not in repr(config)


@pytest.mark.parametrize("raw", ["", " ", ":memory:", "file:finance.db?mode=memory",
                                  "https://example.invalid/db", "\x00"])
def test_invalid_database_path_is_redacted(configuration_env, raw):
    configuration_env["FINANCE_TRACKER_DATABASE_PATH"] = raw
    with pytest.raises(ConfigurationError, match="DATABASE_PATH") as error:
        load_configuration(configuration_env)
    assert "example.invalid" not in str(error.value)


def test_database_path_parent_and_file_validation(configuration_env, tmp_path):
    for invalid in [tmp_path, tmp_path / "missing" / "file.sqlite3"]:
        configuration_env["FINANCE_TRACKER_DATABASE_PATH"] = str(invalid)
        with pytest.raises(ConfigurationError, match="DATABASE_PATH"):
            load_configuration(configuration_env)
    existing = tmp_path / "existing.sqlite3"
    existing.write_bytes(b"synthetic placeholder; never opened as a database")
    existing.chmod(0o600)
    configuration_env["FINANCE_TRACKER_DATABASE_PATH"] = str(existing)
    assert load_configuration(configuration_env).database_path == existing
    assert existing.read_bytes() == b"synthetic placeholder; never opened as a database"
    for mode in [0o644, 0o400, 0o200]:
        existing.chmod(mode)
        with pytest.raises(ConfigurationError, match="DATABASE_PATH"):
            load_configuration(configuration_env)
    existing.chmod(0o600)


@pytest.mark.parametrize("foreign_owner", ["parent", "file"])
def test_database_path_rejects_foreign_ownership(
    configuration_env, tmp_path, monkeypatch, foreign_owner
):
    existing = tmp_path / "synthetic.sqlite3"
    existing.write_bytes(b"synthetic placeholder")
    existing.chmod(0o600)
    target = tmp_path if foreign_owner == "parent" else existing
    original_stat = Path.stat

    def foreign_stat(path, *args, **kwargs):
        result = original_stat(path, *args, **kwargs)
        if path == target:
            fields = list(result)
            fields[4] = result.st_uid + 1
            return os.stat_result(fields)
        return result

    # Simulate another owner's metadata without chown or elevated privileges.
    with monkeypatch.context() as patch:
        patch.setattr(Path, "stat", foreign_stat)
        with pytest.raises(ConfigurationError, match="DATABASE_PATH") as error:
            load_configuration(configuration_env)
    assert str(existing) not in str(error.value)
    assert existing.read_bytes() == b"synthetic placeholder"


@pytest.mark.parametrize("mode", [0o755, 0o500, 0o300, 0o600])
def test_insecure_or_inaccessible_parent_rejected(configuration_env, tmp_path, mode):
    parent = tmp_path / "private"
    parent.mkdir(mode=mode)
    configuration_env["FINANCE_TRACKER_DATABASE_PATH"] = str(parent / "file.sqlite3")
    try:
        with pytest.raises(ConfigurationError, match="DATABASE_PATH"):
            load_configuration(configuration_env)
    finally:
        parent.chmod(0o700)


def test_relative_and_default_path_have_explicit_base(configuration_env, tmp_path):
    (tmp_path / "data").mkdir(mode=0o700)
    configuration_env.pop("FINANCE_TRACKER_DATABASE_PATH")
    config = load_configuration(configuration_env, base_dir=tmp_path)
    assert config.database_path == tmp_path / "data" / "finance_tracker.sqlite3"
    assert list((tmp_path / "data").iterdir()) == []


def test_home_relative_database_path_expands_without_creating_file(configuration_env, tmp_path):
    target = tmp_path / "synthetic.sqlite3"
    configuration_env["FINANCE_TRACKER_DATABASE_PATH"] = "~/" + os.path.relpath(target, Path.home())
    assert load_configuration(configuration_env).database_path == target
    assert not target.exists()


def test_configuration_import_without_ui_or_site_packages():
    source = Path(__file__).resolve().parents[1] / "src"
    script = (
        "import sys; "
        f"sys.path.insert(0, {str(source)!r}); "
        "import finance_tracker.config; "
        "assert 'streamlit' not in sys.modules; "
        "assert 'requests' not in sys.modules"
    )
    subprocess.run([sys.executable, "-I", "-S", "-c", script], check=True)
