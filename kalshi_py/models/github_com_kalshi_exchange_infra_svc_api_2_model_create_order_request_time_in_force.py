from enum import Enum


class GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestTimeInForce(str, Enum):
    FILL_OR_KILL = "fill_or_kill"
    IMMEDIATE_OR_CANCEL = "immediate_or_cancel"

    def __str__(self) -> str:
        return str(self.value)
