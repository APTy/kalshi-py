from enum import Enum


class SvcApi2ModelCreateOrderRequestType(str, Enum):
    LIMIT = "limit"
    MARKET = "market"

    def __str__(self) -> str:
        return str(self.value)
