from enum import Enum


class SvcApi2ModelAcceptQuoteRequestAcceptedSide(str, Enum):
    NO = "no"
    YES = "yes"

    def __str__(self) -> str:
        return str(self.value)
