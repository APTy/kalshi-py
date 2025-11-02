from enum import Enum


class MarketMarketType(str, Enum):
    BINARY = "binary"
    SCALAR = "scalar"

    def __str__(self) -> str:
        return str(self.value)
