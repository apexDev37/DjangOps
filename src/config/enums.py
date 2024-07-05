"""Enums for the config project.

Module to host all enumerations at the project-level.

Note:
    This module is not intended to host all Enums. Django apps should
    host and manage their own `enums.py` module for easier app deploys.
"""

from enum import Enum
from typing import NoReturn

from typing_extensions import LiteralString


class BaseStrEnum(Enum):
    """Generic abstract class for the project's string enums.

    Note:
        Thanks to @artbataev, for inspiring this implementation!
        See: https://github.com/NVIDIA/NeMo/blob/main/nemo/utils/enum.py#L18
    """

    @classmethod
    def _missing_(cls, value: object) -> NoReturn:
        choices = ", ".join(map(str, cls))
        errmsg = f"""
            {value} is not a valid {cls.__name__}.
            Valid choices: {choices}
            """
        raise ValueError(errmsg)

    def __str__(self) -> LiteralString:
        return str(self.value)


class Env(Enum):
    """Target environment settings for the Django project."""

    DEVELOP: str = "develop"
    TESTING: str = "testing"
    STAGING: str = "staging"
    PRODUCTION: str = "production"
