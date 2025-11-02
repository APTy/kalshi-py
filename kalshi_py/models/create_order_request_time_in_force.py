from enum import Enum


class CreateOrderRequestTimeInForce(str, Enum):
    FOK = "FOK"
    GTC = "GTC"
    IOC = "IOC"

    def __str__(self) -> str:
        return str(self.value)
