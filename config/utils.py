"""Utility module for config project.

Utils to provide functionality required for the Django project.
This consists of getters, helpers, and more at the project-level.

Note:
    This module is not intended to host all utils. Django apps should
    host and manage their own `utils` module for easier app deploys.
"""

from config.settings.environment.django import ENVIRONMENT

SETTINGS_MODULE: str = "config.settings"


def get_target_settings() -> str:
    """Return valid module setting for a target environment.

    Concatenates the project's settings module and a valid
    user-configured target environment.

    Raises:
        ValueError: If the target environment is not valid.

    Note:
        If the target `environment` ENV is not configured by the user,
        the default `prod` environment will be used.
    """
    target: str = ENVIRONMENT
    if target not in ("dev", "staging", "prod"):
        errmsg = (
            "Please use a valid target environment module for `ENVIRONMENT` env."
            "See modules in `config.settings.<environments>`"
        )
        raise ValueError(errmsg)
    return f"{SETTINGS_MODULE}.{target}"
