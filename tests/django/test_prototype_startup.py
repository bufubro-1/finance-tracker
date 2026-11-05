"""Exercise the real Django launcher and listener separately from Streamlit."""

from pathlib import Path
import socket
import sqlite3
import subprocess
import sys
import time
from types import SimpleNamespace
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

import pytest

from finance_tracker.django_app import __main__ as launcher


def test_launcher_rejects_other_python(monkeypatch, capsys):
    monkeypatch.setattr(launcher, "sys", SimpleNamespace(version_info=(3, 13), stderr=sys.stderr))
    assert launcher.main([]) == 1
    assert "Python 3.14.x" in capsys.readouterr().err


@pytest.mark.parametrize("args", [["--port", "0"], ["--port", "65536"], ["--bind", "0.0.0.0"]])
def test_launcher_rejects_invalid_listener_arguments(args):
    with pytest.raises(SystemExit) as error:
        launcher.main(args)
    assert error.value.code == 2


def test_actual_loopback_startup_and_static_assets(prototype_env, tmp_path):
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        port = probe.getsockname()[1]
    prototype_env.update(
        DJANGO_SETTINGS_MODULE="nonexistent_release_settings",
        STREAMLIT_SERVER_ADDRESS="0.0.0.0",
        FINANCE_TRACKER_GEMINI_ENABLED="true", FINANCE_TRACKER_TELEGRAM_ENABLED="true",
    )
    with (tmp_path / "startup.log").open("w+") as output:
        process = subprocess.Popen(
            [sys.executable, "-m", "finance_tracker.django_app", "--port", str(port)],
            cwd=tmp_path, env=prototype_env, stdout=output, stderr=subprocess.STDOUT,
        )
        try:
            opener = build_opener(ProxyHandler({}))
            deadline = time.monotonic() + 20
            while time.monotonic() < deadline:
                assert process.poll() is None, (tmp_path / "startup.log").read_text()
                try:
                    response = opener.open(f"http://127.0.0.1:{port}/", timeout=1)
                    break
                except (URLError, TimeoutError):
                    time.sleep(.1)
            else:
                raise AssertionError("Django startup timed out")
            with response:
                assert response.status == 200 and b"Synthetic data only" in response.read()
                assert response.url.endswith("/login/?next=/")
            for path, expected in [("/accounts/", b"Sign in"), ("/static/prototype/style.css", b".card-grid")]:
                with opener.open(f"http://127.0.0.1:{port}{path}", timeout=2) as response:
                    assert response.status == 200 and expected in response.read()
                    if path == "/accounts/":
                        assert response.url.endswith("/login/?next=/accounts/")
            listeners = [row.split()[1] for row in Path("/proc/net/tcp").read_text().splitlines()[1:]
                         if row.split()[3] == "0A" and row.split()[1].endswith(f":{port:04X}")]
            assert listeners == [f"0100007F:{port:04X}"]
            assert not Path(prototype_env["FINANCE_TRACKER_DATABASE_PATH"]).exists()
            # Django's existing runserver migration probe opens SQLite, but must
            # neither apply migrations nor provision an identity on startup.
            db = Path(prototype_env["FINANCE_TRACKER_PROTOTYPE_DATABASE_PATH"])
            assert db.stat().st_mode & 0o077 == 0
            with sqlite3.connect(f"{db.as_uri()}?mode=ro", uri=True) as connection:
                assert connection.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall() == []
        finally:
            process.terminate()
            process.wait(timeout=10)
