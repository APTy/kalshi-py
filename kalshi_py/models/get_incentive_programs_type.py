from enum import Enum


class GetIncentiveProgramsType(str, Enum):
    ALL = "all"
    LIQUIDITY = "liquidity"
    VOLUME = "volume"

    def __str__(self) -> str:
        return str(self.value)
