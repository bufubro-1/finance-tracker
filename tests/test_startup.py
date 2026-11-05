"""TASK-001: TC-037/044 loopback startup subset on the current Linux host."""

import os
from pathlib import Path
import signal
import socket
import subprocess
import sys
import time
from types import SimpleNamespace
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

import pytest

from finance_tracker import __main__ as launcher


@pytest.mark.parametrize("version", [(3, 13, 9), (3, 15, 0)])
def test_unsupported_python_rejected_before_startup(monkeypatch, capsys, version):
    def reject_startup(*args, **kwargs):
        raise AssertionError("Unsupported Python must not start Streamlit")

    monkeypatch.setattr(launcher, "sys", SimpleNamespace(version_info=version, stderr=sys.stderr))
    monkeypatch.setattr(launcher, "subprocess", SimpleNamespace(call=reject_startup))
    assert launcher.main() == 1
    assert capsys.readouterr().err == "Finance Tracker requires Python 3.14.x.\n"


def test_documented_launcher_binds_loopback(clean_environment, tmp_path):
    # Reserve an unused port briefly; the child owns it after this socket closes.
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        port = probe.getsockname()[1]
    env = dict(os.environ, STREAMLIT_SERVER_PORT=str(port),
               STREAMLIT_SERVER_ADDRESS="0.0.0.0")
    log = tmp_path / "startup.log"
    with log.open("w+") as output:
        process = subprocess.Popen(
            [sys.executable, "-m", "finance_tracker"],
            cwd=tmp_path, env=env, stdout=output, stderr=subprocess.STDOUT,
            start_new_session=True,
        )
        try:
            opener = build_opener(ProxyHandler({}))
            deadline = time.monotonic() + 30
            while time.monotonic() < deadline:
                assert process.poll() is None, log.read_text()
                try:
                    with opener.open(f"http://127.0.0.1:{port}/_stcore/health", timeout=1) as response:
                        assert response.status == 200
                        assert response.read() == b"ok"
                    break
                except (URLError, TimeoutError):
                    time.sleep(0.1)
            else:
                raise AssertionError(f"Streamlit startup timed out: {log.read_text()}")
            # Linux socket table verifies the actual listener, not just a CLI flag.
            listeners = [row.split()[1] for row in Path("/proc/net/tcp").read_text().splitlines()[1:]
                         if row.split()[3] == "0A" and row.split()[1].endswith(f":{port:04X}")]
            assert listeners == [f"0100007F:{port:04X}"]
            assert not Path(clean_environment["FINANCE_TRACKER_DATABASE_PATH"]).exists()
        finally:
            os.killpg(process.pid, signal.SIGTERM)
            process.wait(timeout=10)
