"""Synthetic configuration isolated from the owner's environment."""

import pytest


@pytest.fixture
def configuration_env(tmp_path):
    tmp_path.chmod(0o700)
    return {
        "FINANCE_TRACKER_REPORTING_CURRENCY": "USD",
        "FINANCE_TRACKER_MINOR_UNIT_SCALE": "2",
        "FINANCE_TRACKER_DATABASE_PATH": str(tmp_path / "synthetic.sqlite3"),
    }


@pytest.fixture
def clean_environment(monkeypatch, configuration_env):
    import os

    for name in tuple(os.environ):
        if name.startswith(("FINANCE_TRACKER_", "STREAMLIT_", "GEMINI_", "TELEGRAM_")):
            monkeypatch.delenv(name)
    for name, value in configuration_env.items():
        monkeypatch.setenv(name, value)
    return configuration_env
