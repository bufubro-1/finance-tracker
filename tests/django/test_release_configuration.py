"""TASK-022B: TC-001/038/041 scope; release configuration is not deployment."""

from pathlib import Path

import pytest


PREFIX = "FINANCE_TRACKER_RELEASE_"


@pytest.fixture
def release_env(prototype_env):
    env = prototype_env.copy()
    env.update({
        PREFIX + "SECRET_KEY": "synthetic-release-signing-PRIVATE-SENTINEL-" * 2,
        PREFIX + "ALLOWED_HOSTS": "finance.example.invalid",
        PREFIX + "CSRF_TRUSTED_ORIGINS": "https://finance.example.invalid",
        PREFIX + "DB_NAME": "synthetic_finance",
        PREFIX + "DB_USER": "synthetic_runtime",
        PREFIX + "DB_PASSWORD": "synthetic-db-PRIVATE-SENTINEL",
        PREFIX + "DB_HOST": "postgres",
        PREFIX + "STATIC_ROOT": str(Path(prototype_env["FINANCE_TRACKER_PROTOTYPE_DATABASE_PATH"]).parent / "static-assets"),
    })
    return env


def test_release_contract_never_opens_database_or_loads_providers(run_django, release_env):
    # Bad development configuration must not affect release configuration parsing.
    release_env["FINANCE_TRACKER_PROTOTYPE_DATABASE_PATH"] = "invalid/PRIVATE-SENTINEL.sqlite3"
    release_env["FINANCE_TRACKER_DJANGO_SECRET_KEY"] = ""
    release_env["FINANCE_TRACKER_GEMINI_ENABLED"] = "true"
    release_env["FINANCE_TRACKER_TELEGRAM_ENABLED"] = "true"
    run_django('''
import socket
import sys
def reject(*args, **kwargs):
    raise AssertionError("Unexpected database or network initialization")
socket.socket.connect = reject
import finance_tracker.django_app.settings_release as release
assert not release.DEBUG
assert release.ALLOWED_HOSTS == ["finance.example.invalid"]
assert release.CSRF_TRUSTED_ORIGINS == ["https://finance.example.invalid"]
db = release.DATABASES["default"]
assert db["ENGINE"] == "django.db.backends.postgresql"
assert db["NAME"] == "synthetic_finance" and db["USER"] == "synthetic_runtime"
assert db["HOST"] == "postgres" and db["PORT"] == "5432"
assert not release.SECURE_PROXY_SSL_HEADER and not release.USE_X_FORWARDED_HOST
assert release.SECURE_SSL_REDIRECT and release.SESSION_COOKIE_SECURE and release.CSRF_COOKIE_SECURE
assert release.SESSION_COOKIE_HTTPONLY and release.SESSION_COOKIE_SAMESITE == "Lax"
assert release.CSRF_COOKIE_SAMESITE == "Lax"
assert release.X_FRAME_OPTIONS == "DENY" and release.SECURE_CONTENT_TYPE_NOSNIFF
assert release.AUTH_USER_MODEL == "identity.User" and release.LANGUAGE_CODE == "tr"
assert release.EMAIL_BACKEND.endswith("dummy.EmailBackend")
assert release.SECURE_HSTS_SECONDS == 0 and not release.SECURE_HSTS_PRELOAD
assert "django.db.backends.postgresql.base" not in sys.modules
assert not any(m.startswith(("psycopg", "google.genai", "telegram")) for m in sys.modules)
''', env=release_env)
    assert not Path(release_env["FINANCE_TRACKER_DATABASE_PATH"]).exists()
    assert not Path(release_env[PREFIX + "STATIC_ROOT"]).exists()


@pytest.mark.parametrize("name", [
    "SECRET_KEY", "ALLOWED_HOSTS", "CSRF_TRUSTED_ORIGINS", "DB_NAME", "DB_USER", "DB_PASSWORD", "DB_HOST", "STATIC_ROOT",
])
def test_missing_release_inputs_fail_without_development_fallback(run_django, release_env, name):
    release_env.pop(PREFIX + name)
    result = run_django("import finance_tracker.django_app.settings_release", env=release_env, success=False)
    assert result.returncode != 0 and PREFIX + name in result.stderr
    assert "PRIVATE-SENTINEL" not in result.stdout + result.stderr
    assert not Path(release_env["FINANCE_TRACKER_PROTOTYPE_DATABASE_PATH"]).exists()


@pytest.mark.parametrize("name,value", [
    ("SECRET_KEY", "short-PRIVATE-SENTINEL"),
    ("SECRET_KEY", "x" * 60),
    ("SECRET_KEY", "django-insecure-" + "synthetic-PRIVATE-SENTINEL" * 3),
    ("SECRET_KEY", "synthetic-PRIVATE-SENTINEL\n" * 3),
    ("ALLOWED_HOSTS", "*"),
    ("ALLOWED_HOSTS", ".example.invalid"),
    ("ALLOWED_HOSTS", "https://PRIVATE-SENTINEL.invalid"),
    ("ALLOWED_HOSTS", "finance.example.invalid:443"),
    ("ALLOWED_HOSTS", "finance.example.invalid,"),
    ("CSRF_TRUSTED_ORIGINS", "http://finance.example.invalid"),
    ("CSRF_TRUSTED_ORIGINS", "https://*.example.invalid"),
    ("CSRF_TRUSTED_ORIGINS", "https://other.example.invalid"),
    ("CSRF_TRUSTED_ORIGINS", "https://PRIVATE-SENTINEL@finance.example.invalid"),
    ("CSRF_TRUSTED_ORIGINS", "https://finance.example.invalid/private-PRIVATE-SENTINEL"),
    ("CSRF_TRUSTED_ORIGINS", "https://finance.example.invalid?PRIVATE-SENTINEL"),
    ("CSRF_TRUSTED_ORIGINS", "https://finance.example.invalid#PRIVATE-SENTINEL"),
    ("CSRF_TRUSTED_ORIGINS", "https://finance.example.invalid:"),
    ("CSRF_TRUSTED_ORIGINS", "https://finance.example.invalid:99999"),
    ("DB_NAME", "PRIVATE-SENTINEL/db"),
    ("DB_USER", "PRIVATE-SENTINEL user"),
    ("DB_PASSWORD", "PRIVATE-SENTINEL\n"),
    ("DB_HOST", "postgres://PRIVATE-SENTINEL/db"),
    ("DB_HOST", ""),
    ("DB_PORT", "PRIVATE-SENTINEL"),
    ("DB_PORT", "0"),
    ("DB_PORT", "65536"),
    ("TRUST_PROXY_HTTPS", "PRIVATE-SENTINEL"),
    ("STATIC_ROOT", "relative-PRIVATE-SENTINEL"),
    ("STATIC_ROOT", "/"),
    ("STATIC_ROOT", "/tmp/../PRIVATE-SENTINEL"),
])
def test_invalid_release_configuration_is_actionable_and_redacted(run_django, release_env, name, value):
    release_env[PREFIX + name] = value
    result = run_django("import finance_tracker.django_app.settings_release", env=release_env, success=False)
    assert result.returncode != 0 and PREFIX + name in result.stderr
    assert "PRIVATE-SENTINEL" not in result.stdout + result.stderr


@pytest.mark.parametrize("proxy", ["true", "false"])
def test_proxy_trust_is_explicit_and_settings_are_isolated(run_django, release_env, proxy):
    release_env[PREFIX + "TRUST_PROXY_HTTPS"] = proxy
    run_django('''
import os
import finance_tracker.django_app.settings_release as release
import finance_tracker.django_app.settings as development
expected = ("HTTP_X_FORWARDED_PROTO", "https") if os.environ["FINANCE_TRACKER_RELEASE_TRUST_PROXY_HTTPS"] == "true" else None
assert release.SECURE_PROXY_SSL_HEADER == expected
assert development.ALLOWED_HOSTS == ["127.0.0.1", "localhost", "[::1]"]
assert development.DATABASES["default"]["ENGINE"] == "django.db.backends.sqlite3"
assert not development.SESSION_COOKIE_SECURE and not development.CSRF_COOKIE_SECURE
assert development.SECRET_KEY != release.SECRET_KEY
assert development.DATABASES is not release.DATABASES
''', env=release_env)


@pytest.mark.parametrize("host,origin", [
    ("finance.example.invalid", "https://finance.example.invalid:8443"),
    ("[::1]", "https://[::1]"),
    ("127.0.0.1", "https://127.0.0.1"),
])
def test_exact_hosts_and_explicit_https_ports(run_django, release_env, host, origin):
    release_env[PREFIX + "ALLOWED_HOSTS"] = host
    release_env[PREFIX + "CSRF_TRUSTED_ORIGINS"] = origin
    release_env[PREFIX + "DB_HOST"] = "[::1]"
    run_django('''
import finance_tracker.django_app.settings_release as release
assert release.DATABASES["default"]["HOST"] == "::1"
''', env=release_env)


@pytest.mark.parametrize("name", ["FINANCE_TRACKER_DJANGO_SECRET_KEY", PREFIX + "SECRET_KEY", PREFIX + "DB_PASSWORD"])
def test_private_secret_file_and_conflicting_inputs(run_django, release_env, tmp_path, name):
    value = release_env.pop(name)
    secret = tmp_path / "synthetic-private-key"
    secret.write_text(value + "\n")
    secret.chmod(0o600)
    release_env[name + "_FILE"] = str(secret)
    module = "settings" if name == "FINANCE_TRACKER_DJANGO_SECRET_KEY" else "settings_release"
    run_django("import finance_tracker.django_app." + module, env=release_env)
    release_env[name] = value
    result = run_django("import finance_tracker.django_app." + module, env=release_env, success=False)
    assert result.returncode != 0 and "exactly one" in result.stderr
    assert "PRIVATE-SENTINEL" not in result.stdout + result.stderr


@pytest.mark.parametrize("kind", ["public", "missing", "symlink", "directory", "fifo", "oversize", "invalid_utf8", "blank", "newline"])
def test_invalid_secret_files_fail_privately(run_django, release_env, tmp_path, kind):
    import os

    path = tmp_path / "PRIVATE-SENTINEL.key"
    if kind == "directory":
        path.mkdir(mode=0o700)
    elif kind == "fifo":
        os.mkfifo(path, 0o600)
    elif kind == "symlink":
        target = tmp_path / "synthetic-target"
        target.write_text(release_env[PREFIX + "SECRET_KEY"])
        target.chmod(0o600)
        path.symlink_to(target)
    elif kind != "missing":
        contents = {
            "oversize": b"x" * 4097, "invalid_utf8": b"\xff", "blank": b"\n",
            "newline": b"synthetic-PRIVATE-SENTINEL\n" * 3,
        }.get(kind, release_env[PREFIX + "SECRET_KEY"].encode())
        path.write_bytes(contents)
        path.chmod(0o644 if kind == "public" else 0o600)
    release_env.pop(PREFIX + "SECRET_KEY")
    release_env[PREFIX + "SECRET_KEY_FILE"] = str(path)
    result = run_django("import finance_tracker.django_app.settings_release", env=release_env, success=False)
    assert result.returncode != 0 and PREFIX + "SECRET_KEY" in result.stderr
    assert "PRIVATE-SENTINEL" not in result.stdout + result.stderr


def test_secret_file_rejects_foreign_owner_and_accepts_read_only(run_django, release_env, tmp_path):
    path = tmp_path / "synthetic-read-only-key"
    path.write_text(release_env[PREFIX + "SECRET_KEY"])
    path.chmod(0o400)
    release_env.pop(PREFIX + "SECRET_KEY")
    release_env[PREFIX + "SECRET_KEY_FILE"] = str(path)
    run_django('''
import os
from types import SimpleNamespace
from unittest.mock import patch
from django.core.exceptions import ImproperlyConfigured
from finance_tracker.django_app.configuration import read_secret
name = "FINANCE_TRACKER_RELEASE_SECRET_KEY"
assert len(read_secret(os.environ, name, minimum=50)) >= 50
real_stat = os.fstat
def foreign_owner(fd):
    info = real_stat(fd)
    return SimpleNamespace(st_mode=info.st_mode, st_uid=os.getuid() + 1)
with patch("os.fstat", side_effect=foreign_owner):
    try:
        read_secret(os.environ, name, minimum=50)
    except ImproperlyConfigured as error:
        assert "PRIVATE-SENTINEL" not in str(error)
    else:
        raise AssertionError("Foreign-owned secret accepted")
''', env=release_env)


def test_logs_never_interpolate_private_messages_or_exception_data(run_django, release_env):
    run_django('''
import io
import logging
import logging.config
import os
import django
django.setup()
import finance_tracker.django_app.settings_release as release
from django.conf import settings
assert settings.LOGGING == release.LOGGING
output = io.StringIO()
for name in ("", "django", "django.server", "finance_tracker"):
    logger = logging.getLogger(name)
    for handler in logger.handlers:
        handler.setStream(output)
secret = os.environ["FINANCE_TRACKER_RELEASE_DB_PASSWORD"]
class NeverRender:
    def __str__(self):
        raise AssertionError("Sensitive log interpolation")
for name in ("django.server", "django.request", "django.security.csrf", "django.db.backends", "finance_tracker.configuration"):
    logger = logging.getLogger(name)
    try:
        raise ValueError(secret)
    except ValueError:
        logger.exception("private request %s", secret, extra={"request": secret, "status_code": 500})
    logger.warning(NeverRender(), extra={"status_code": secret})
assert secret not in output.getvalue() and "PRIVATE-SENTINEL" not in output.getvalue()
assert "HTTP 500" in output.getvalue() and "Traceback" not in output.getvalue()
''', env=release_env)


def test_release_https_and_cookies_using_isolated_development_storage(run_django, release_env, migrated_prototype):
    # Exercise the actual middleware with SQLite, without claiming PostgreSQL startup.
    run_django('''
import django
django.setup()
import finance_tracker.django_app.settings_release as release
from django.contrib.auth import get_user_model
from django.test import Client, override_settings
names = ("ALLOWED_HOSTS", "CSRF_TRUSTED_ORIGINS", "SESSION_COOKIE_SECURE", "CSRF_COOKIE_SECURE", "SECURE_SSL_REDIRECT", "SECURE_PROXY_SSL_HEADER", "USE_X_FORWARDED_HOST")
with override_settings(**{name: getattr(release, name) for name in names}):
    client = Client(enforce_csrf_checks=True, HTTP_HOST="finance.example.invalid")
    assert client.get("/login/").status_code == 301
    assert client.get("/login/", HTTP_X_FORWARDED_PROTO="https").status_code == 301
    response = client.get("/login/", secure=True)
    assert response.status_code == 200 and client.cookies["csrftoken"]["secure"]
    assert client.post("/login/", {}, secure=True).status_code == 403
    assert client.get("/login/", secure=True, HTTP_HOST="other.example.invalid").status_code == 400
    user = get_user_model().objects.create_user("release-cookie@example.invalid")
    client.force_login(user)
    response = client.get("/", secure=True)
    assert response.status_code == 200 and "no-store" in response.headers["Cache-Control"]
    # A real session save response must set the secure session cookie.
    session = client.session
    session["synthetic"] = True
    session.save()
    from django.contrib.sessions.middleware import SessionMiddleware
    from django.http import HttpRequest, HttpResponse
    request = HttpRequest()
    request.session = session
    request.session.modified = True
    response = SessionMiddleware(lambda request: HttpResponse()).process_response(request, HttpResponse())
    assert response.cookies["sessionid"]["secure"] and response.cookies["sessionid"]["httponly"]
with override_settings(ALLOWED_HOSTS=release.ALLOWED_HOSTS, SECURE_SSL_REDIRECT=True, SECURE_PROXY_SSL_HEADER=("HTTP_X_FORWARDED_PROTO", "https")):
    assert Client(HTTP_HOST="finance.example.invalid").get("/login/", HTTP_X_FORWARDED_PROTO="https").status_code == 200
''', env=release_env)


def test_financial_input_rules_run_without_django_or_credentials(run_django, prototype_env):
    env = {name: value for name, value in prototype_env.items() if not name.startswith(("FINANCE_TRACKER_", "DJANGO_"))}
    run_django('''
import builtins
import socket
original_import = builtins.__import__
def isolated_import(name, *args, **kwargs):
    if name.startswith(("django", "streamlit", "psycopg", "google", "telegram")):
        raise AssertionError("Unexpected framework/provider dependency")
    return original_import(name, *args, **kwargs)
builtins.__import__ = isolated_import
def reject(*args, **kwargs):
    raise AssertionError("Unexpected network")
socket.socket.connect = reject
from finance_tracker.django_app.account_rules import parse_opening_balance, format_minor
assert parse_opening_balance("1000.00") == 100000
assert format_minor(100000) == "1,000.00"
''', env=env)
