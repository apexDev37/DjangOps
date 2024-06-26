"""Environment `database` settings for the config project.

The environment variables defined here are for the database
connection settings for the Django project.

See:
https://docs.djangoproject.com/en/4.2/ref/settings/#databases
"""

from pathlib import Path

import environ

from config.settings.common.base import BASE_DIR

# Set default project-wide ENV casting.
env = environ.FileAwareEnv(
    DB_ENGINE=(str, None),
    DB_HOST=(str, None),
    DB_NAME=(str, None),
    DB_PASSWORD=(str, None),
    DB_PORT=(int, None),
    DB_USER=(str, None),
)

# Read environment variables from .env file
environ.Env.read_env(Path(BASE_DIR, ".envs", "database.env"))

DB_ENGINE = env("DB_ENGINE")
DB_HOST = env("DB_HOST")
DB_NAME = env("DB_NAME")
DB_PASSWORD = env("DB_PASSWORD")
DB_PORT = env("DB_PORT")
DB_USER = env("DB_USER")
