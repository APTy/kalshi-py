from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ticker_pair_side import TickerPairSide

T = TypeVar("T", bound="TickerPair")


@_attrs_define
class TickerPair:
    """
    Attributes:
        market_ticker (str): Market ticker identifier.
        event_ticker (str): Event ticker identifier.
        side (TickerPairSide): Side of the market (yes or no).
    """

    market_ticker: str
    event_ticker: str
    side: TickerPairSide
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        market_ticker = self.market_ticker

        event_ticker = self.event_ticker

        side = self.side.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "market_ticker": market_ticker,
                "event_ticker": event_ticker,
                "side": side,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        market_ticker = d.pop("market_ticker")

        event_ticker = d.pop("event_ticker")

        side = TickerPairSide(d.pop("side"))

        ticker_pair = cls(
            market_ticker=market_ticker,
            event_ticker=event_ticker,
            side=side,
        )

        ticker_pair.additional_properties = d
        return ticker_pair

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
