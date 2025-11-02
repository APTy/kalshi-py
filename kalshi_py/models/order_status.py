from enum import Enum


class OrderStatus(str, Enum):
    CANCELED = "canceled"
    EXECUTED = "executed"
    PENDING = "pending"
    RESTING = "resting"

    def __str__(self) -> str:
        return str(self.value)
