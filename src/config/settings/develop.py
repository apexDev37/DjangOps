# ruff: noqa: F401, F405
"""Django `development` settings for config project.

Development target settings for the Django project inherited
from the base environment common settings.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/
"""

from config.settings.common.base import *  # noqa: F403
from config.settings.common.base import INSTALLED_APPS, MIDDLEWARE
from config.settings.common.database import DATABASES
from config.settings.environment.django import (
    ALLOWED_HOSTS,
    DEBUG,
    ENVIRONMENT,
    SECRET_KEY,
)

INTERNAL_IPS = [".localhost", "127.0.0.1", "[::1]"]

# Include apps required only for development.
INSTALLED_APPS.extend(
    [
        "debug_toolbar",
    ]
)

# Include middleware required only for development.
# Note: Consider middleware order is often critical to work effectively.
MIDDLEWARE.extend(
    [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]
)
