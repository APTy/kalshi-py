from enum import Enum


class ModelAmendOrderRequestSide(str, Enum):
    NO = "no"
    YES = "yes"

    def __str__(self) -> str:
        return str(self.value)
