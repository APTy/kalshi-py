from enum import IntEnum


class GetMarketCandlesticksByEventPeriodInterval(IntEnum):
    VALUE_1 = 1
    VALUE_60 = 60
    VALUE_1440 = 1440

    def __str__(self) -> str:
        return str(self.value)
