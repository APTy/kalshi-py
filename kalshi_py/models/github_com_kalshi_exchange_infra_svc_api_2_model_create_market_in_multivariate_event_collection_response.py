from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionResponse:
    """
    Attributes:
        event_ticker (Union[Unset, str]): Event ticker for the created market.
        market_ticker (Union[Unset, str]): Market ticker for the created market.
    """

    event_ticker: Union[Unset, str] = UNSET
    market_ticker: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_ticker = self.event_ticker

        market_ticker = self.market_ticker

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_ticker is not UNSET:
            field_dict["event_ticker"] = event_ticker
        if market_ticker is not UNSET:
            field_dict["market_ticker"] = market_ticker

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_ticker = d.pop("event_ticker", UNSET)

        market_ticker = d.pop("market_ticker", UNSET)

        github_com_kalshi_exchange_infra_svc_api_2_model_create_market_in_multivariate_event_collection_response = cls(
            event_ticker=event_ticker,
            market_ticker=market_ticker,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_create_market_in_multivariate_event_collection_response.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_create_market_in_multivariate_event_collection_response

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
