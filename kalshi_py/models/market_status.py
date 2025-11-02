from enum import Enum


class MarketStatus(str, Enum):
    ACTIVE = "active"
    CLOSED = "closed"
    DETERMINED = "determined"
    INITIALIZED = "initialized"
    SETTLED = "settled"

    def __str__(self) -> str:
        return str(self.value)
