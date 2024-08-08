"""Test utils for the config project.

Define and test all project-level utils in this module. Avoid adding
transactional or DB-dependent tests here. Prefer to design and mark utils as
single, isolated, logical units.

Note:
    This module is not intended to host all utils. Django apps should
    host and manage their own `<app>/utils.py` module for easier app deploys.
"""

import re
from typing import Self

import pytest
from django.core.exceptions import ImproperlyConfigured

from src.config.constants import SETTINGS_MODULE
from src.config.enums import Environment
from src.config.utils import get_target_settings

# Regex to validate a string as a Python module format
# according to the official PEP 8 naming conventions.
# See: https://peps.python.org/pep-0008/#package-and-module-names
PYTHON_MODULE_RE: str = r"^[a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z_][a-zA-Z0-9_]*)*$"


# Leverage global variable to apply custom marker at the module level
# for all tests. Add markers by assigning values of type: list.
# For example: [pytest.mark.smoke, pytest.mark.unit, ...]
pytestmark = pytest.mark.unit


@pytest.mark.smoke("critical: logic to configure settings required to run project.")
class TestEnvironmentTargetSettings:
    """Tests to cover the logic to dynamically configure target settings."""

    def test_should_raise_exc_for_invalid_user_configured_env(
        self: Self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        # Given
        target = "non-existent"
        monkeypatch.setenv("ENVIRONMENT", target)

        # Then
        with pytest.raises(
            (ValueError, ImproperlyConfigured), match="configure a valid target"
        ):
            get_target_settings()  # When

    def test_should_default_to_prod_when_env_not_user_configured(
        self: Self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        # Given
        monkeypatch.delenv("ENVIRONMENT", raising=True)
        expected = str(f"{SETTINGS_MODULE}.{Environment.PRODUCTION}")

        # When
        actual = get_target_settings()

        # Then
        assert isinstance(actual, str)
        assert re.match(PYTHON_MODULE_RE, actual)
        assert actual == expected

    def test_should_return_target_setting_for_valid_user_configured_env(
        self: Self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        # Given
        target = Environment("testing")
        monkeypatch.setenv("ENVIRONMENT", target)
        expected = str(f"{SETTINGS_MODULE}.{target}")

        # When
        actual = get_target_settings()

        # Then
        assert isinstance(actual, str)
        assert re.match(PYTHON_MODULE_RE, actual)
        assert actual == expected
