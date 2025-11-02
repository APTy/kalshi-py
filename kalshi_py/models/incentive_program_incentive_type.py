from enum import Enum


class IncentiveProgramIncentiveType(str, Enum):
    LIQUIDITY = "liquidity"
    VOLUME = "volume"

    def __str__(self) -> str:
        return str(self.value)
