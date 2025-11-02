from enum import Enum


class CreateOrderRequestType(str, Enum):
    LIMIT = "limit"
    MARKET = "market"

    def __str__(self) -> str:
        return str(self.value)
