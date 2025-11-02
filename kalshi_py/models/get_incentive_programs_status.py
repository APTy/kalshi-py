from enum import Enum


class GetIncentiveProgramsStatus(str, Enum):
    ACTIVE = "active"
    ALL = "all"
    CLOSED = "closed"
    PAID_OUT = "paid_out"
    UPCOMING = "upcoming"

    def __str__(self) -> str:
        return str(self.value)
