from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BidAskDistribution")


@_attrs_define
class BidAskDistribution:
    """
    Attributes:
        open_ (int): Offer price on the market at the start of the candlestick period (in cents).
        open_dollars (str): Offer price on the market at the start of the candlestick period (in dollars).
        low (int): Lowest offer price on the market during the candlestick period (in cents).
        low_dollars (str): Lowest offer price on the market during the candlestick period (in dollars).
        high (int): Highest offer price on the market during the candlestick period (in cents).
        high_dollars (str): Highest offer price on the market during the candlestick period (in dollars).
        close (int): Offer price on the market at the end of the candlestick period (in cents).
        close_dollars (str): Offer price on the market at the end of the candlestick period (in dollars).
    """

    open_: int
    open_dollars: str
    low: int
    low_dollars: str
    high: int
    high_dollars: str
    close: int
    close_dollars: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_ = self.open_

        open_dollars = self.open_dollars

        low = self.low

        low_dollars = self.low_dollars

        high = self.high

        high_dollars = self.high_dollars

        close = self.close

        close_dollars = self.close_dollars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "open": open_,
                "open_dollars": open_dollars,
                "low": low,
                "low_dollars": low_dollars,
                "high": high,
                "high_dollars": high_dollars,
                "close": close,
                "close_dollars": close_dollars,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        open_ = d.pop("open")

        open_dollars = d.pop("open_dollars")

        low = d.pop("low")

        low_dollars = d.pop("low_dollars")

        high = d.pop("high")

        high_dollars = d.pop("high_dollars")

        close = d.pop("close")

        close_dollars = d.pop("close_dollars")

        bid_ask_distribution = cls(
            open_=open_,
            open_dollars=open_dollars,
            low=low,
            low_dollars=low_dollars,
            high=high,
            high_dollars=high_dollars,
            close=close,
            close_dollars=close_dollars,
        )

        bid_ask_distribution.additional_properties = d
        return bid_ask_distribution

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
