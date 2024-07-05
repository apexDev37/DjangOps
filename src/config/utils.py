"""Utility module for config project.

Utils to provide functionality required for the Django project.
This consists of getters, helpers, and more at the project-level.

Note:
    This module is not intended to host all utils. Django apps should
    host and manage their own `utils` module for easier app deploys.
"""

from typing_extensions import LiteralString

from config.constants import SETTINGS_MODULE
from config.enums import Environment
from config.settings.environment.django import ENVIRONMENT


def get_target_settings() -> LiteralString:
    """Return valid module setting for a target environment.

    Concatenates the project's settings module and a valid
    user-configured target environment.

    Note:
        If the target `environment` ENV is not configured by the user,
        the default environment, `production`, will be used.
    """
    try:
        target: Environment = Environment(ENVIRONMENT)
    except ValueError as exc:
        errmsg = "Please configure a valid target `ENVIRONMENT`."
        raise ValueError(errmsg) from exc
    return f"{SETTINGS_MODULE}.{str(target)}"
