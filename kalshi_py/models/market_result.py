from enum import Enum


class MarketResult(str, Enum):
    NO = "no"
    VALUE_2 = ""
    YES = "yes"

    def __str__(self) -> str:
        return str(self.value)
