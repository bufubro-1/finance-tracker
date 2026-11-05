"""Prototype settings only. No release, cloud or external-adapter configuration."""

import os
from pathlib import Path
import stat

from django.core.exceptions import ImproperlyConfigured


SECRET_KEY = os.environ.get("FINANCE_TRACKER_DJANGO_SECRET_KEY", "")
if len(SECRET_KEY.strip()) < 50:
    raise ImproperlyConfigured(
        "FINANCE_TRACKER_DJANGO_SECRET_KEY requires at least 50 characters. "
        "See docs/SETUP.md."
    )


def prototype_database():
    """Validate without opening, creating or changing a database or directory."""
    message = (
        "FINANCE_TRACKER_PROTOTYPE_DATABASE_PATH must name a separate local SQLite "
        "file in an existing owner-only readable/writable directory. See docs/SETUP.md."
    )
    raw = os.environ.get("FINANCE_TRACKER_PROTOTYPE_DATABASE_PATH", "data/prototype.sqlite3")
    try:
        if not raw.strip() or raw == ":memory:" or "://" in raw or raw.startswith("file:"):
            raise ValueError
        path = Path(raw).expanduser().resolve()
        legacy = Path(os.environ.get(
            "FINANCE_TRACKER_DATABASE_PATH", "data/finance_tracker.sqlite3"
        )).expanduser().resolve()
        if path == legacy:
            raise ValueError
        for target in (path.parent, path) if path.exists() else (path.parent,):
            info = target.stat()
            mode = stat.S_IMODE(info.st_mode)
            required = 0o700 if target == path.parent else 0o600
            if (info.st_uid != os.getuid() or mode & 0o077
                    or mode & required != required
                    or not os.access(target, os.R_OK | os.W_OK)
                    or (target == path.parent and not target.is_dir())
                    or (target == path and not target.is_file())):
                raise ValueError
        return path
    except (OSError, ValueError, RuntimeError):
        raise ImproperlyConfigured(message) from None


DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "[::1]"]
INSTALLED_APPS = [
    "django.contrib.auth", "django.contrib.contenttypes", "django.contrib.sessions",
    "django.contrib.staticfiles", "finance_tracker.django_app.identity",
    "finance_tracker.django_app",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "finance_tracker.django_app.urls"
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
    ]},
}]
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": prototype_database()}}
AUTH_USER_MODEL = "identity.User"
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "login"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
USE_TZ = True
TIME_ZONE = "UTC"
LANGUAGE_CODE = "en-us"
STATIC_URL = "/static/"
EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SAMESITE = "Lax"
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
