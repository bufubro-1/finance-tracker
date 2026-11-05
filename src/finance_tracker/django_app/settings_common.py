"""Shared Django presentation/identity settings; no storage or secret defaults."""

DEBUG = False
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
AUTH_USER_MODEL = "identity.User"
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "login"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
USE_TZ = True
TIME_ZONE = "UTC"
LANGUAGE_CODE = "tr"
STATIC_URL = "/static/"
EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SAMESITE = "Lax"
CSRF_FAILURE_VIEW = "finance_tracker.django_app.views.csrf_failure"
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

# Emit operational metadata only: no request, environment, SQL or exception text.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"private": {
        "()": "finance_tracker.django_app.configuration.MetadataFormatter",
    }},
    "handlers": {"private_console": {
        "class": "logging.StreamHandler", "formatter": "private",
    }},
    "root": {"handlers": ["private_console"], "level": "WARNING"},
    "loggers": {
        "django": {"handlers": ["private_console"], "level": "INFO", "propagate": False},
        "django.server": {"handlers": ["private_console"], "level": "INFO", "propagate": False},
        "finance_tracker": {"handlers": ["private_console"], "level": "INFO", "propagate": False},
    },
}
