from enum import Enum


class CreateOrderRequestSelfTradePreventionType(str, Enum):
    MAKER = "maker"
    TAKER_AT_CROSS = "taker_at_cross"

    def __str__(self) -> str:
        return str(self.value)
