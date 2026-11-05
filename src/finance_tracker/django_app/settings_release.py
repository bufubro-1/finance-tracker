"""Release configuration contract only; operational release gates remain open."""

import os

from .configuration import release_configuration
from .settings_common import *

globals().update(release_configuration(os.environ))
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
USE_X_FORWARDED_HOST = False
SECURE_HSTS_SECONDS = 0  # Activate only with the later reviewed HTTPS topology.
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
