from enum import Enum


class GetPositionsSettlementStatus(str, Enum):
    ALL = "all"
    SETTLED = "settled"
    UNSETTLED = "unsettled"

    def __str__(self) -> str:
        return str(self.value)
