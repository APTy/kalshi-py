from enum import Enum


class ModelGetSettlementsResponseSettlementsItemMarketResult(str, Enum):
    NO = "no"
    SCALAR = "scalar"
    VOID = "void"
    YES = "yes"

    def __str__(self) -> str:
        return str(self.value)
