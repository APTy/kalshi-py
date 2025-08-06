from enum import Enum


class SvcApi2ModelAmendOrderRequestAction(str, Enum):
    BUY = "buy"
    SELL = "sell"

    def __str__(self) -> str:
        return str(self.value)
