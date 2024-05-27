# ruff: noqa: F401, F405
"""Django `test` settings for config project.

Testing target settings for the Django project inherited
from the base environment common settings.

Note:
    Django will change `DEBUG` to `False` when running tests
    despite what has been configured in the environment.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/
"""

from config.settings.environment.database import DATABASES
from config.settings.environment.django import (
    ALLOWED_HOSTS,
    DEBUG,
    SECRET_KEY,
)

from .base import *  # noqa: F403
