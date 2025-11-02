from enum import Enum


class SeriesFeeType(str, Enum):
    FLAT = "flat"
    QUADRATIC = "quadratic"
    QUADRATIC_WITH_MAKER_FEES = "quadratic_with_maker_fees"

    def __str__(self) -> str:
        return str(self.value)
