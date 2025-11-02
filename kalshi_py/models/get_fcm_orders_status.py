from enum import Enum


class GetFCMOrdersStatus(str, Enum):
    CANCELED = "canceled"
    EXECUTED = "executed"
    RESTING = "resting"

    def __str__(self) -> str:
        return str(self.value)
