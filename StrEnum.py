from enum import Enum


class StrEnum(Enum):
    def __repr__(self):
        return f"'{self.value}'"
