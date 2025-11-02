from enum import Enum


class MarketStrikeType(str, Enum):
    BETWEEN = "between"
    CUSTOM = "custom"
    FUNCTIONAL = "functional"
    GREATER = "greater"
    GREATER_OR_EQUAL = "greater_or_equal"
    LESS = "less"
    LESS_OR_EQUAL = "less_or_equal"
    STRUCTURED = "structured"

    def __str__(self) -> str:
        return str(self.value)
