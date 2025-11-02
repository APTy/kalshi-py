from enum import Enum


class QuoteStatus(str, Enum):
    ACCEPTED = "accepted"
    CANCELLED = "cancelled"
    CONFIRMED = "confirmed"
    EXECUTED = "executed"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
