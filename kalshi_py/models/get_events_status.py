from enum import Enum


class GetEventsStatus(str, Enum):
    CLOSED = "closed"
    OPEN = "open"
    SETTLED = "settled"

    def __str__(self) -> str:
        return str(self.value)
