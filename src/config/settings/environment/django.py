"""Environment `django` settings for the config project.

Note:
    To utilize the custom/standard Django settings in this module in your Python
    code, import the settings module from 'django.conf' rather than this module
    itself. This allows for more flexible and testable code while deriving the
    setting from the configured Django settings module used at runtime.

    [Example]
    - Prefer: `from django.conf import settings; settings.ENVIRONMENT`
    - Avoid: `from config.settings.environment.django import ENVIRONMENT`

    This doesn't apply to base or target environment settings (ie. develop, etc)
    which should import directly from `environment` modules.

See:
    https://docs.djangoproject.com/en/4.2/topics/settings/#using-settings-in-python-code
"""

from pathlib import Path

import environ

from config.enums import Environment
from config.settings.common.base import BASE_DIR

# Set default project-wide ENV casting.
env = environ.FileAwareEnv(
    ALLOWED_HOSTS=(list, []),
    DEBUG=(bool, False),
    ENVIRONMENT=(str, Environment.PRODUCTION),
    SECRET_KEY=(str, None),
)

# Read environment variables from .env file.
# We explicitly do not want to override the above
# envs where we also supply envs at the infra-level (Compose).
environ.Env.read_env(
    Path(BASE_DIR, ".envs", "django.env"),
    overwrite=False,
)

ALLOWED_HOSTS = env("ALLOWED_HOSTS")
DEBUG = env("DEBUG")
ENVIRONMENT = env("ENVIRONMENT")
SECRET_KEY = env("SECRET_KEY")
