"""TASK-001: real Streamlit script execution with synthetic configuration."""

from pathlib import Path
import socket

from streamlit.testing.v1 import AppTest


APP = Path(__file__).resolve().parents[1] / "src" / "finance_tracker" / "app.py"


def test_local_shell_runs_without_provider_calls(clean_environment, monkeypatch):
    def reject_network(*args, **kwargs):
        raise AssertionError("Runtime shell attempted a network connection")

    monkeypatch.setattr(socket.socket, "connect", reject_network)
    app = AppTest.from_file(str(APP)).run()
    assert not app.exception
    assert not app.error
    assert app.title[0].value == "Finance Tracker"
    assert app.success[0].value == "Local configuration is valid."
    assert any("USD" in item.value for item in app.markdown)
    assert any("Gemini: disabled" in item.value for item in app.markdown)
    assert not Path(clean_environment["FINANCE_TRACKER_DATABASE_PATH"]).exists()


def test_missing_currency_shows_actionable_error(clean_environment, monkeypatch):
    monkeypatch.delenv("FINANCE_TRACKER_REPORTING_CURRENCY")
    app = AppTest.from_file(str(APP)).run()
    assert not app.exception
    assert "REPORTING_CURRENCY" in app.error[0].value
    assert not app.success


def test_bad_path_is_redacted_in_ui(clean_environment, monkeypatch):
    monkeypatch.setenv("FINANCE_TRACKER_DATABASE_PATH", "private-synthetic-secret/missing/db")
    app = AppTest.from_file(str(APP)).run()
    assert not app.exception
    assert "DATABASE_PATH" in app.error[0].value
    assert "private-synthetic-secret" not in app.error[0].value
    assert not app.success


def test_incomplete_integrations_leave_shell_usable(clean_environment, monkeypatch):
    monkeypatch.setenv("FINANCE_TRACKER_GEMINI_ENABLED", "true")
    monkeypatch.setenv("FINANCE_TRACKER_TELEGRAM_ENABLED", "true")
    app = AppTest.from_file(str(APP)).run()
    assert not app.exception and not app.error
    assert len(app.warning) == 2
    assert app.success
