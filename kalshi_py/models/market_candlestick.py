from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bid_ask_distribution import BidAskDistribution
    from ..models.price_distribution import PriceDistribution


T = TypeVar("T", bound="MarketCandlestick")


@_attrs_define
class MarketCandlestick:
    """
    Attributes:
        end_period_ts (int): Unix timestamp for the inclusive end of the candlestick period.
        yes_bid (BidAskDistribution):
        yes_ask (BidAskDistribution):
        price (PriceDistribution):
        volume (int): Number of contracts bought on the market during the candlestick period.
        open_interest (int): Number of contracts bought on the market by end of the candlestick period (end_period_ts).
    """

    end_period_ts: int
    yes_bid: "BidAskDistribution"
    yes_ask: "BidAskDistribution"
    price: "PriceDistribution"
    volume: int
    open_interest: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_period_ts = self.end_period_ts

        yes_bid = self.yes_bid.to_dict()

        yes_ask = self.yes_ask.to_dict()

        price = self.price.to_dict()

        volume = self.volume

        open_interest = self.open_interest

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end_period_ts": end_period_ts,
                "yes_bid": yes_bid,
                "yes_ask": yes_ask,
                "price": price,
                "volume": volume,
                "open_interest": open_interest,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bid_ask_distribution import BidAskDistribution
        from ..models.price_distribution import PriceDistribution

        d = dict(src_dict)
        end_period_ts = d.pop("end_period_ts")

        yes_bid = BidAskDistribution.from_dict(d.pop("yes_bid"))

        yes_ask = BidAskDistribution.from_dict(d.pop("yes_ask"))

        price = PriceDistribution.from_dict(d.pop("price"))

        volume = d.pop("volume")

        open_interest = d.pop("open_interest")

        market_candlestick = cls(
            end_period_ts=end_period_ts,
            yes_bid=yes_bid,
            yes_ask=yes_ask,
            price=price,
            volume=volume,
            open_interest=open_interest,
        )

        market_candlestick.additional_properties = d
        return market_candlestick

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
