from enum import Enum


class GetFCMPositionsSettlementStatus(str, Enum):
    ALL = "all"
    SETTLED = "settled"
    UNSETTLED = "unsettled"

    def __str__(self) -> str:
        return str(self.value)
