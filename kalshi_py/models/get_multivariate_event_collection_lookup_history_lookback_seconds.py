from enum import IntEnum


class GetMultivariateEventCollectionLookupHistoryLookbackSeconds(IntEnum):
    VALUE_10 = 10
    VALUE_60 = 60
    VALUE_300 = 300
    VALUE_3600 = 3600

    def __str__(self) -> str:
        return str(self.value)
