from enum import Enum


class GetMultivariateEventCollectionsStatus(str, Enum):
    CLOSED = "closed"
    OPEN = "open"
    UNOPENED = "unopened"

    def __str__(self) -> str:
        return str(self.value)
