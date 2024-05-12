"""Environment `django` settings for the config project."""

from pathlib import Path

import environ

# Set default project-wide ENV casting.
env = environ.FileAwareEnv(
    ALLOWED_HOSTS=(list, []),
    DEBUG=(bool, False),
    SECRET_KEY=(str, None),
)

# Set the project base directory
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parents[3]

environ.Env.read_env(Path(BASE_DIR, ".envs", "django.env"))

ALLOWED_HOSTS = env("ALLOWED_HOSTS")
DEBUG = env("DEBUG")
SECRET_KEY = env("SECRET_KEY")
