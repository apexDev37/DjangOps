# ruff: noqa: F401, F405
"""Django `test` settings for config project.

Testing target settings for the Django project inherited
from the base environment common settings.

Note:
    - Django will change `DEBUG` to `False` when running tests
    despite what has been configured in the environment.
    - DB-dependent tests create isolated blank databases for test
    execution only and do not use your “real” (production) database.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/
"""

import os

from config.settings.environment.database import DATABASES
from config.settings.environment.django import (
    ALLOWED_HOSTS,
    DEBUG,
    SECRET_KEY,
)

from .base import *  # noqa: F403

# Settings for test databases for the target env: `testing`.
# NB: Test databases are destroyed when all the tests have been executed,
# regardless of whether they (pass) or (fail).
DATABASES["default"]["TEST"] = {"MIGRATE": True, "NAME": None}


# TODO(apexDev37): Test running tests in separate parallel processes.
# Uncomment after verified successful behavior.
# os.environ.setdefault("DJANGO_TEST_PROCESSES", 4)  # noqa: ERA001


# Leverage faster PWD hasher to speed up tests.
# NB: (MD5) cryptographically weak hashing algorithm unsuitable for production.
# NB: (SHA1) less faster, but more secure than `MD5`; significantly faster than Django defaults.
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.SHA1PasswordHasher",
]