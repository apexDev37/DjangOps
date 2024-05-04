# ruff: noqa: F405
"""Django `dev` settings for config project.

Development target settings for the Django project inherited
from the base environment common settings.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/
"""

from .base import *  # noqa: F403

# Core
# https://docs.djangoproject.com/en/4.2/ref/settings/

ALLOWED_HOSTS = env("ALLOWED_HOSTS")
DEBUG = env("DEBUG")
SECRET_KEY = env("SECRET_KEY")
