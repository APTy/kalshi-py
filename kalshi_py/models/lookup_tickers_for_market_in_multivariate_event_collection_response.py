from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LookupTickersForMarketInMultivariateEventCollectionResponse")


@_attrs_define
class LookupTickersForMarketInMultivariateEventCollectionResponse:
    """
    Attributes:
        event_ticker (str): Event ticker for the looked up market.
        market_ticker (str): Market ticker for the looked up market.
    """

    event_ticker: str
    market_ticker: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_ticker = self.event_ticker

        market_ticker = self.market_ticker

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_ticker": event_ticker,
                "market_ticker": market_ticker,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_ticker = d.pop("event_ticker")

        market_ticker = d.pop("market_ticker")

        lookup_tickers_for_market_in_multivariate_event_collection_response = cls(
            event_ticker=event_ticker,
            market_ticker=market_ticker,
        )

        lookup_tickers_for_market_in_multivariate_event_collection_response.additional_properties = d
        return lookup_tickers_for_market_in_multivariate_event_collection_response

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
