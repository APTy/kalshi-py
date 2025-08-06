from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_lookup_tickers_for_market_in_multivariate_event_collection_request_selected_markets_item_side import (
    GithubComKalshiExchangeInfraSvcApi2ModelLookupTickersForMarketInMultivariateEventCollectionRequestSelectedMarketsItemSide,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="GithubComKalshiExchangeInfraSvcApi2ModelLookupTickersForMarketInMultivariateEventCollectionRequestSelectedMarketsItem",
)


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelLookupTickersForMarketInMultivariateEventCollectionRequestSelectedMarketsItem:
    """
    Attributes:
        event_ticker (Union[Unset, str]): Event ticker identifier.
        market_ticker (Union[Unset, str]): Market ticker identifier.
        side (Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelLookupTickersForMarketInMultivariateEventCollectionRe
            questSelectedMarketsItemSide]): Side of the market (yes or no).
    """

    event_ticker: Union[Unset, str] = UNSET
    market_ticker: Union[Unset, str] = UNSET
    side: Union[
        Unset,
        GithubComKalshiExchangeInfraSvcApi2ModelLookupTickersForMarketInMultivariateEventCollectionRequestSelectedMarketsItemSide,
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_ticker = self.event_ticker

        market_ticker = self.market_ticker

        side: Union[Unset, str] = UNSET
        if not isinstance(self.side, Unset):
            side = self.side.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_ticker is not UNSET:
            field_dict["event_ticker"] = event_ticker
        if market_ticker is not UNSET:
            field_dict["market_ticker"] = market_ticker
        if side is not UNSET:
            field_dict["side"] = side

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_ticker = d.pop("event_ticker", UNSET)

        market_ticker = d.pop("market_ticker", UNSET)

        _side = d.pop("side", UNSET)
        side: Union[
            Unset,
            GithubComKalshiExchangeInfraSvcApi2ModelLookupTickersForMarketInMultivariateEventCollectionRequestSelectedMarketsItemSide,
        ]
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = GithubComKalshiExchangeInfraSvcApi2ModelLookupTickersForMarketInMultivariateEventCollectionRequestSelectedMarketsItemSide(
                _side
            )

        github_com_kalshi_exchange_infra_svc_api_2_model_lookup_tickers_for_market_in_multivariate_event_collection_request_selected_markets_item = cls(
            event_ticker=event_ticker,
            market_ticker=market_ticker,
            side=side,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_lookup_tickers_for_market_in_multivariate_event_collection_request_selected_markets_item.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_lookup_tickers_for_market_in_multivariate_event_collection_request_selected_markets_item

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
