"""TASK-022A: P1-01 and shell subsets of P1-03/06, TC-001/038/039/053."""

from pathlib import Path

import pytest


def test_anonymous_redirect_and_login_without_database_or_network(run_django, prototype_env):
    run_django('''
import socket
def reject(*args, **kwargs):
    raise AssertionError("Unexpected external call")
socket.socket.connect = reject
import django
django.setup()
from django.test import Client
client = Client(HTTP_HOST="127.0.0.1")
for path in ("/", "/accounts/"):
    response = client.get(path)
    assert response.status_code == 302
    assert response.url == "/login/?next=" + path
    assert b"Example Savings" not in response.content
response = client.get("/login/")
assert response.status_code == 200
assert b"Synthetic data only" in response.content
assert b"csrfmiddlewaretoken" in response.content
''')
    assert not Path(prototype_env["FINANCE_TRACKER_PROTOTYPE_DATABASE_PATH"]).exists()
    assert not Path(prototype_env["FINANCE_TRACKER_DATABASE_PATH"]).exists()


def test_authenticated_navigation_and_sample_cards_without_network(run_django, prototype_env, migrated_prototype):
    run_django(r'''
import socket
def reject(*args, **kwargs):
    raise AssertionError("Unexpected external call")
socket.socket.connect = reject
import django
django.setup()
from django.test import Client
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
client = Client(HTTP_HOST="127.0.0.1")
client.force_login(get_user_model().objects.create_user("cards@example.invalid"))
for path, active, other in [("/", "/", "/accounts/"), ("/accounts/", "/accounts/", "/")]:
    response = client.get(path)
    assert response.status_code == 200
    html = response.content.decode()
    assert f'href="{active}" aria-current="page"' in html
    assert f'href="{other}"' in html
    assert html.count('aria-current="page"') == 1
    assert "Synthetic data only" in html
    assert "name=\"viewport\"" in html
    assert "/static/prototype/style.css" in html
assert "Example Savings" in html and "USD" in html and "1,000.00" in html
assert "Not saved" in html and "No saved accounts yet" in html
assert "not included in any total" in html
card = render_to_string("prototype/account_card.html", {
    "name": "<script>synthetic</script>", "currency": "USD", "balance": "0.00",
})
assert "<script>" not in card and "&lt;script&gt;" in card
assert client.post("/").status_code == 405
assert client.post("/accounts/").status_code == 405
assert client.get("/admin/").status_code == 404
assert client.get("/accounts/create/").status_code == 404
assert client.get("/", HTTP_HOST="example.invalid").status_code == 400
''')
    assert not Path(prototype_env["FINANCE_TRACKER_DATABASE_PATH"]).exists()


def test_migrations_identity_and_system_checks(run_django, prototype_env):
    legacy = Path(prototype_env["FINANCE_TRACKER_DATABASE_PATH"])
    legacy.write_bytes(b"synthetic legacy sentinel: must never be opened as SQLite")
    legacy.chmod(0o600)
    run_django('''
import os
os.umask(0o077)
import django
django.setup()
from django.core.management import call_command
call_command("check")
call_command("migrate", interactive=False, verbosity=0)
call_command("makemigrations", check=True, dry_run=True)
from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
User = get_user_model()
assert User._meta.label == "identity.User"
assert User.USERNAME_FIELD == "email"
user = User.objects.create_user("  Sample@Example.INVALID  ", "synthetic-test-password")
assert user.email == "sample@example.invalid"
assert user.check_password("synthetic-test-password")
assert user.password != "synthetic-test-password"
assert not user.is_staff and not user.is_superuser
try:
    with transaction.atomic():
        User.objects.bulk_create([User(email="SAMPLE@example.invalid")])
except IntegrityError:
    pass
else:
    raise AssertionError("Case-insensitive duplicate identity accepted")
try:
    User.objects.create_superuser("admin@example.invalid", "synthetic-password")
except ValueError:
    pass
else:
    raise AssertionError("Unexpected application superuser provisioning")
''')
    # Confirm a separate process can read the same initial identity schema/data.
    run_django('''
import django
django.setup()
from django.contrib.auth import get_user_model
assert get_user_model().objects.get(email="sample@example.invalid").is_active
''')
    assert legacy.read_bytes() == b"synthetic legacy sentinel: must never be opened as SQLite"
    db = Path(prototype_env["FINANCE_TRACKER_PROTOTYPE_DATABASE_PATH"])
    assert db.stat().st_mode & 0o077 == 0


@pytest.mark.parametrize("raw", ["", ":memory:", "file:private-secret?mode=memory", "https://private-secret/db", "missing-private-secret/db"])
def test_bad_database_configuration_is_redacted(run_django, prototype_env, raw):
    prototype_env["FINANCE_TRACKER_PROTOTYPE_DATABASE_PATH"] = raw
    result = run_django("import finance_tracker.django_app.settings", success=False)
    assert result.returncode != 0
    assert "FINANCE_TRACKER_PROTOTYPE_DATABASE_PATH" in result.stderr
    assert "private-secret" not in result.stderr


def test_legacy_database_collision_rejected(run_django, prototype_env):
    prototype_env["FINANCE_TRACKER_PROTOTYPE_DATABASE_PATH"] = prototype_env["FINANCE_TRACKER_DATABASE_PATH"]
    result = run_django("import finance_tracker.django_app.settings", success=False)
    assert result.returncode != 0 and "separate local SQLite" in result.stderr


@pytest.mark.parametrize("target", ["directory", "file"])
def test_insecure_database_permissions_rejected(run_django, prototype_env, target):
    db = Path(prototype_env["FINANCE_TRACKER_PROTOTYPE_DATABASE_PATH"])
    path = db.parent if target == "directory" else db
    if target == "file":
        path.write_bytes(b"synthetic placeholder")
    path.chmod(0o755 if target == "directory" else 0o644)
    try:
        result = run_django("import finance_tracker.django_app.settings", success=False)
        assert result.returncode != 0
        assert "owner-only" in result.stderr
    finally:
        path.chmod(0o700 if target == "directory" else 0o600)


def test_missing_secret_is_actionable_without_revealing_value(run_django, prototype_env):
    prototype_env["FINANCE_TRACKER_DJANGO_SECRET_KEY"] = "private-short-secret"
    result = run_django("import finance_tracker.django_app.settings", success=False)
    assert result.returncode != 0
    assert "FINANCE_TRACKER_DJANGO_SECRET_KEY" in result.stderr
    assert "private-short-secret" not in result.stderr
