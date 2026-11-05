"""TASK-025A: synthetic, interactive provisioning without credential output."""

from pathlib import Path

import pytest


SETUP = r'''
import io
import secrets
import django
django.setup()
from django.contrib.auth import get_user_model
from django.core.management import call_command, CommandError
from unittest.mock import patch
User = get_user_model()
password = secrets.token_urlsafe(24)
output = io.StringIO()
def provision(values):
    with patch("getpass.getpass", side_effect=values):
        call_command("provision_prototype_user", stdout=output, stderr=output)
'''


def test_provisioning_hashes_password_and_refuses_duplicate(run_django, migrated_prototype):
    run_django(SETUP + r'''
provision([password, password])
user = User.objects.get(email="sample@example.invalid")
assert user.check_password(password) and user.password != password
assert user.is_active and not user.is_staff and not user.is_superuser
assert password not in output.getvalue()
assert "sample@example.invalid" in output.getvalue()
original = user.password
with patch("getpass.getpass", side_effect=AssertionError("Duplicate must not prompt")):
    try:
        call_command("provision_prototype_user", stdout=output)
    except CommandError as error:
        assert "already exists" in str(error) and password not in str(error)
    else:
        raise AssertionError("Duplicate provisioning accepted")
user.refresh_from_db()
assert User.objects.count() == 1 and user.password == original
''')


@pytest.mark.parametrize("case", ["blank", "mismatch", "eof", "interrupt", "no_secure_terminal"])
def test_rejected_password_entry_creates_no_user(run_django, migrated_prototype, case):
    run_django(SETUP + "\ncase = " + repr(case) + r'''
import getpass
import warnings
values = {
    "blank": ["  ", "  "],
    "mismatch": [password, password + "x"],
    "eof": [EOFError()],
    "interrupt": [KeyboardInterrupt()],
}
def insecure_prompt(*args):
    warnings.warn("No terminal", getpass.GetPassWarning)
    raise AssertionError("Must not read visible input")
try:
    if case == "no_secure_terminal":
        with patch("getpass.getpass", side_effect=insecure_prompt):
            call_command("provision_prototype_user", stdout=output)
    else:
        provision(values[case])
except CommandError as error:
    assert password not in str(error)
else:
    raise AssertionError("Invalid provisioning accepted")
assert User.objects.count() == 0 and password not in output.getvalue()
''')


@pytest.mark.parametrize("overrides", [
    {"SETTINGS_MODULE": "finance_tracker.release_settings"},
    {"DATABASES": {"default": {"ENGINE": "django.db.backends.postgresql"}}},
])
def test_provisioning_refuses_nonprototype_settings(run_django, migrated_prototype, overrides):
    run_django(SETUP + "\noverrides = " + repr(overrides) + r'''
from django.test import override_settings
with override_settings(**overrides), patch("getpass.getpass", side_effect=AssertionError("Must not prompt")):
    try:
        call_command("provision_prototype_user", stdout=output)
    except CommandError as error:
        assert "prototype settings" in str(error)
    else:
        raise AssertionError("Nonprototype provisioning accepted")
assert User.objects.count() == 0
''')


def test_provisioning_requires_explicit_migrations(run_django, prototype_env):
    run_django(SETUP + r'''
with patch("getpass.getpass", side_effect=AssertionError("Must not prompt")):
    try:
        call_command("provision_prototype_user", stdout=output)
    except CommandError as error:
        assert "migrations first" in str(error)
    else:
        raise AssertionError("Missing schema accepted")
''')
    assert not Path(prototype_env["FINANCE_TRACKER_PROTOTYPE_DATABASE_PATH"]).exists()


def test_provisioning_has_no_email_or_password_options(run_django):
    run_django(SETUP + r'''
from django.core.management import load_command_class
command = load_command_class("finance_tracker.django_app.identity", "provision_prototype_user")
parser = command.create_parser("django", "provision_prototype_user")
options = {option for action in parser._actions for option in action.option_strings}
assert "--password" not in options and "--email" not in options
''')
