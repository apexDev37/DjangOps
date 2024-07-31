"""Constants for the config project.

Module to host all literals and constants at the project-level.

Note:
    This module is not intended to host all constants. Django apps should
    host and manage their own `constants.py` module for easier app deploys.
"""

import sys

from config.enums import Environment
from config.settings.environment.django import DEBUG, ENVIRONMENT

SETTINGS_MODULE: str = "config.settings"

# Only enable the toolbar when we're in debug mode,
# running the application with `develop` settings,
# and we're not running tests.
ENABLE_DEBUG_TOOLBAR = bool(
    DEBUG and "test" not in sys.argv and str(Environment.DEVELOP) == ENVIRONMENT
)
