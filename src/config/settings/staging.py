# ruff: noqa: F401, F405
"""Django `staging` settings for config project.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from config.settings.common.base import *  # noqa: F403
from config.settings.common.database import DATABASES
from config.settings.environment.django import (
    ALLOWED_HOSTS,
    DEBUG,
    SECRET_KEY,
)
