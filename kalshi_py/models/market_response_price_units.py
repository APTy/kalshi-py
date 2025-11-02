from enum import Enum


class MarketResponsePriceUnits(str, Enum):
    CENTS = "cents"

    def __str__(self) -> str:
        return str(self.value)
