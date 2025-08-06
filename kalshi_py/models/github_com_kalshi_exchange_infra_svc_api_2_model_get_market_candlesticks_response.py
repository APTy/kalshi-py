from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_get_market_candlesticks_response_candlesticks_item import (
        GithubComKalshiExchangeInfraSvcApi2ModelGetMarketCandlesticksResponseCandlesticksItem,
    )


T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelGetMarketCandlesticksResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelGetMarketCandlesticksResponse:
    """
    Attributes:
        candlesticks (Union[Unset,
            list['GithubComKalshiExchangeInfraSvcApi2ModelGetMarketCandlesticksResponseCandlesticksItem']]): Array of
            candlestick data points for the specified time range.
        ticker (Union[Unset, str]): Unique identifier for the market.
    """

    candlesticks: Union[
        Unset, list["GithubComKalshiExchangeInfraSvcApi2ModelGetMarketCandlesticksResponseCandlesticksItem"]
    ] = UNSET
    ticker: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        candlesticks: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.candlesticks, Unset):
            candlesticks = []
            for candlesticks_item_data in self.candlesticks:
                candlesticks_item = candlesticks_item_data.to_dict()
                candlesticks.append(candlesticks_item)

        ticker = self.ticker

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if candlesticks is not UNSET:
            field_dict["candlesticks"] = candlesticks
        if ticker is not UNSET:
            field_dict["ticker"] = ticker

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_get_market_candlesticks_response_candlesticks_item import (
            GithubComKalshiExchangeInfraSvcApi2ModelGetMarketCandlesticksResponseCandlesticksItem,
        )

        d = dict(src_dict)
        candlesticks = []
        _candlesticks = d.pop("candlesticks", UNSET)
        for candlesticks_item_data in _candlesticks or []:
            candlesticks_item = (
                GithubComKalshiExchangeInfraSvcApi2ModelGetMarketCandlesticksResponseCandlesticksItem.from_dict(
                    candlesticks_item_data
                )
            )

            candlesticks.append(candlesticks_item)

        ticker = d.pop("ticker", UNSET)

        github_com_kalshi_exchange_infra_svc_api_2_model_get_market_candlesticks_response = cls(
            candlesticks=candlesticks,
            ticker=ticker,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_get_market_candlesticks_response.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_get_market_candlesticks_response

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
