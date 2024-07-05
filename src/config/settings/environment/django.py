"""Environment `django` settings for the config project."""

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
