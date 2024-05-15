"""Utility module for config project.

Utils to provide functionality required for the Django project.
This consists of getters, helpers, and more at the project-level.

Note:
    This module is not intended to host all utils. Django apps should
    host and manage their own `utils` module for easier app deploys.
"""

from config.settings.environment.django import ENVIRONMENT


def get_target_settings() -> str:
    """Return the user-configured target environment settings."""
    settings_module = "config.settings"
    target = ENVIRONMENT
    return f"{settings_module}.{target}"
