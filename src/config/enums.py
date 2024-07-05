"""Enums for the config project.

Module to host all enumerations at the project-level.

Note:
    This module is not intended to host all Enums. Django apps should
    host and manage their own `enums.py` module for easier app deploys.
"""

from enum import Enum, auto, unique
from typing import Any, NoReturn

from typing_extensions import LiteralString


class BaseStrEnum(str, Enum):
    """Base class for the project's enum string constants.

    Disclaimer:
        This class runs type conversion, str(v), on member assigned values
        but does not validate initial values are of type:string.

    Note:
        Thanks to @artbataev, for inspiring this implementation!
        See: https://github.com/NVIDIA/NeMo/blob/main/nemo/utils/enum.py#L18
    """

    @staticmethod
    def _generate_next_value_(
        name: str, start: int, count: int, last_values: list[Any]
    ) -> LiteralString:
        """Return the lower-cased version of the member name."""
        return name.lower()

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


@unique
class Environment(BaseStrEnum):
    """Target environment settings for the Django project."""

    DEVELOP = auto()
    TESTING = auto()
    STAGING = auto()
    PRODUCTION = auto()
