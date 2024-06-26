"""Enums for the config project.

Module to host all enumerations at the project-level.

Note:
    This module is not intended to host all Enums. Django apps should
    host and manage their own `enums.py` module for easier app deploys.
"""

from enum import Enum


class Env(Enum):
    """Target environment settings for the Django project."""

    DEVELOP: str = "develop"
    TESTING: str = "testing"
    STAGING: str = "staging"
    PRODUCTION: str = "production"
