from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_lookup_tickers_for_market_in_multivariate_event_collection_request_selected_markets_item import (
        GithubComKalshiExchangeInfraSvcApi2ModelLookupTickersForMarketInMultivariateEventCollectionRequestSelectedMarketsItem,
    )


T = TypeVar(
    "T", bound="GithubComKalshiExchangeInfraSvcApi2ModelLookupTickersForMarketInMultivariateEventCollectionRequest"
)


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelLookupTickersForMarketInMultivariateEventCollectionRequest:
    """
    Attributes:
        selected_markets (Union[Unset, list['GithubComKalshiExchangeInfraSvcApi2ModelLookupTickersForMarketInMultivariat
            eEventCollectionRequestSelectedMarketsItem']]): List of selected markets that act as parameters to determine
            which market is produced.
    """

    selected_markets: Union[
        Unset,
        list[
            "GithubComKalshiExchangeInfraSvcApi2ModelLookupTickersForMarketInMultivariateEventCollectionRequestSelectedMarketsItem"
        ],
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        selected_markets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.selected_markets, Unset):
            selected_markets = []
            for selected_markets_item_data in self.selected_markets:
                selected_markets_item = selected_markets_item_data.to_dict()
                selected_markets.append(selected_markets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if selected_markets is not UNSET:
            field_dict["selected_markets"] = selected_markets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_lookup_tickers_for_market_in_multivariate_event_collection_request_selected_markets_item import (
            GithubComKalshiExchangeInfraSvcApi2ModelLookupTickersForMarketInMultivariateEventCollectionRequestSelectedMarketsItem,
        )

        d = dict(src_dict)
        selected_markets = []
        _selected_markets = d.pop("selected_markets", UNSET)
        for selected_markets_item_data in _selected_markets or []:
            selected_markets_item = GithubComKalshiExchangeInfraSvcApi2ModelLookupTickersForMarketInMultivariateEventCollectionRequestSelectedMarketsItem.from_dict(
                selected_markets_item_data
            )

            selected_markets.append(selected_markets_item)

        github_com_kalshi_exchange_infra_svc_api_2_model_lookup_tickers_for_market_in_multivariate_event_collection_request = cls(
            selected_markets=selected_markets,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_lookup_tickers_for_market_in_multivariate_event_collection_request.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_lookup_tickers_for_market_in_multivariate_event_collection_request

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
