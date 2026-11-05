"""Compatible development entrypoint: private, synthetic, loopback SQLite only."""

import os

from .configuration import prototype_database, read_secret
from .settings_common import *  # Shared framework settings, never release inputs.

SECRET_KEY = read_secret(os.environ, "FINANCE_TRACKER_DJANGO_SECRET_KEY", minimum=50)
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "[::1]"]
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": prototype_database()}}
SESSION_COOKIE_SECURE = False  # Guarded loopback HTTP development only.
CSRF_COOKIE_SECURE = False
