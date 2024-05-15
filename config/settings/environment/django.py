"""Environment `django` settings for the config project."""

from pathlib import Path

import environ

from config.settings.base import BASE_DIR

# Set default project-wide ENV casting.
env = environ.FileAwareEnv(
    ALLOWED_HOSTS=(list, []),
    DEBUG=(bool, False),
    ENVIRONMENT=(str, "production"),
    SECRET_KEY=(str, None),
)

# Read environment variables from .env file
environ.Env.read_env(Path(BASE_DIR, ".envs", "django.env"))

ALLOWED_HOSTS = env("ALLOWED_HOSTS")
DEBUG = env("DEBUG")
ENVIRONMENT = env("ENVIRONMENT")
SECRET_KEY = env("SECRET_KEY")
