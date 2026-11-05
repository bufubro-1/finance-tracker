"""Django scenarios run in child interpreters, isolated from TASK-001 fixtures."""

import os
from pathlib import Path
import subprocess
import sys

import pytest


@pytest.fixture
def prototype_env(tmp_path):
    tmp_path.chmod(0o700)
    env = {k: v for k, v in os.environ.items() if not k.startswith((
        "FINANCE_TRACKER_", "DJANGO_", "GEMINI_", "TELEGRAM_", "STREAMLIT_",
    ))}
    env.update(
        # This checkout is authoritative even when reusing another venv's dependencies.
        PYTHONPATH=str(Path(__file__).resolve().parents[2] / "src"),
        DJANGO_SETTINGS_MODULE="finance_tracker.django_app.settings",
        FINANCE_TRACKER_DJANGO_SECRET_KEY="synthetic-test-key-no-live-credentials-" * 2,
        FINANCE_TRACKER_PROTOTYPE_DATABASE_PATH=str(tmp_path / "prototype.sqlite3"),
        FINANCE_TRACKER_DATABASE_PATH=str(tmp_path / "legacy.sqlite3"),
    )
    return env


@pytest.fixture
def run_django(prototype_env, tmp_path):
    def run(script, *, env=None, success=True):
        result = subprocess.run(
            [sys.executable, "-c", "from pathlib import Path; import finance_tracker; "
             "assert Path(finance_tracker.__file__).resolve().is_relative_to("
             + repr(str(Path(__file__).resolve().parents[2])) + ");\n" + script],
            env=prototype_env if env is None else env,
            cwd=tmp_path, capture_output=True, text=True, timeout=30,
        )
        if success:
            assert result.returncode == 0, result.stdout + result.stderr
        return result
    return run


@pytest.fixture
def migrated_prototype(run_django):
    run_django('''
import os
os.umask(0o077)
import django
django.setup()
from django.core.management import call_command
call_command("migrate", interactive=False, verbosity=0)
''')
