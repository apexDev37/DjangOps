"""Database settings for the config project.

Define required base `database` settings, shareable across
target environments for the Django project.

See:
https://docs.djangoproject.com/en/4.2/ref/settings/#databases
"""

from config.settings.environment.database import (
    DB_ENGINE,
    DB_HOST,
    DB_NAME,
    DB_PASSWORD,
    DB_PORT,
    DB_USER,
)

DATABASES = {
    "default": {
        "ENGINE": DB_ENGINE,
        "HOST": DB_HOST,
        "NAME": DB_NAME,
        "PASSWORD": DB_PASSWORD,
        "PORT": DB_PORT,
        "USER": DB_USER,
    }
}
