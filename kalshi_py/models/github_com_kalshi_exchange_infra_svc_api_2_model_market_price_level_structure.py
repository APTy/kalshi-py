from enum import Enum


class GithubComKalshiExchangeInfraSvcApi2ModelMarketPriceLevelStructure(str, Enum):
    DECI_CENT = "deci_cent"
    LINEAR_CENT = "linear_cent"
    TAPERED_DECI_CENT = "tapered_deci_cent"

    def __str__(self) -> str:
        return str(self.value)
