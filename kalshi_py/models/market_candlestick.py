from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_bid_ask_distribution import (
        GithubComKalshiExchangeInfraSvcApi2ModelBidAskDistribution,
    )
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_price_distribution import (
        GithubComKalshiExchangeInfraSvcApi2ModelPriceDistribution,
    )


T = TypeVar("T", bound="MarketCandlestick")


@_attrs_define
class MarketCandlestick:
    """
    Attributes:
        end_period_ts (Union[Unset, int]): Unix timestamp for the inclusive end of the candlestick period.
        open_interest (Union[Unset, int]): Number of contracts bought on the market by end of the candlestick period
            (end_period_ts).
        price (Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelPriceDistribution]):
        volume (Union[Unset, int]): Number of contracts bought on the market during the candlestick period.
        yes_ask (Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelBidAskDistribution]):
        yes_bid (Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelBidAskDistribution]):
    """

    end_period_ts: Union[Unset, int] = UNSET
    open_interest: Union[Unset, int] = UNSET
    price: Union[Unset, "GithubComKalshiExchangeInfraSvcApi2ModelPriceDistribution"] = UNSET
    volume: Union[Unset, int] = UNSET
    yes_ask: Union[Unset, "GithubComKalshiExchangeInfraSvcApi2ModelBidAskDistribution"] = UNSET
    yes_bid: Union[Unset, "GithubComKalshiExchangeInfraSvcApi2ModelBidAskDistribution"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_period_ts = self.end_period_ts

        open_interest = self.open_interest

        price: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        volume = self.volume

        yes_ask: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.yes_ask, Unset):
            yes_ask = self.yes_ask.to_dict()

        yes_bid: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.yes_bid, Unset):
            yes_bid = self.yes_bid.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_period_ts is not UNSET:
            field_dict["end_period_ts"] = end_period_ts
        if open_interest is not UNSET:
            field_dict["open_interest"] = open_interest
        if price is not UNSET:
            field_dict["price"] = price
        if volume is not UNSET:
            field_dict["volume"] = volume
        if yes_ask is not UNSET:
            field_dict["yes_ask"] = yes_ask
        if yes_bid is not UNSET:
            field_dict["yes_bid"] = yes_bid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_bid_ask_distribution import (
            GithubComKalshiExchangeInfraSvcApi2ModelBidAskDistribution,
        )
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_price_distribution import (
            GithubComKalshiExchangeInfraSvcApi2ModelPriceDistribution,
        )

        d = dict(src_dict)
        end_period_ts = d.pop("end_period_ts", UNSET)

        open_interest = d.pop("open_interest", UNSET)

        _price = d.pop("price", UNSET)
        price: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelPriceDistribution]
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = GithubComKalshiExchangeInfraSvcApi2ModelPriceDistribution.from_dict(_price)

        volume = d.pop("volume", UNSET)

        _yes_ask = d.pop("yes_ask", UNSET)
        yes_ask: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelBidAskDistribution]
        if isinstance(_yes_ask, Unset):
            yes_ask = UNSET
        else:
            yes_ask = GithubComKalshiExchangeInfraSvcApi2ModelBidAskDistribution.from_dict(_yes_ask)

        _yes_bid = d.pop("yes_bid", UNSET)
        yes_bid: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelBidAskDistribution]
        if isinstance(_yes_bid, Unset):
            yes_bid = UNSET
        else:
            yes_bid = GithubComKalshiExchangeInfraSvcApi2ModelBidAskDistribution.from_dict(_yes_bid)

        market_candlestick = cls(
            end_period_ts=end_period_ts,
            open_interest=open_interest,
            price=price,
            volume=volume,
            yes_ask=yes_ask,
            yes_bid=yes_bid,
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
