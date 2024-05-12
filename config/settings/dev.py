# ruff: noqa: F401, F405
"""Django `dev` settings for config project.

Development target settings for the Django project inherited
from the base environment common settings.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/
"""

from config.settings.environment.django import (
    ALLOWED_HOSTS,
    DEBUG,
    SECRET_KEY,
)

from .base import *  # noqa: F403
