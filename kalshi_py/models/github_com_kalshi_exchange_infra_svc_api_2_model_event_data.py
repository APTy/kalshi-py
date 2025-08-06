from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_market import (
        GithubComKalshiExchangeInfraSvcApi2ModelMarket,
    )


T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelEventData")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelEventData:
    """
    Attributes:
        category (Union[Unset, str]): Event category (deprecated, use series-level category instead).
        collateral_return_type (Union[Unset, str]):
        event_ticker (Union[Unset, str]): Unique identifier for this event.
        markets (Union[Unset, list['GithubComKalshiExchangeInfraSvcApi2ModelMarket']]): Array of markets associated with
            this event. Only populated when 'with_nested_markets=true' is specified in the request.
        mutually_exclusive (Union[Unset, bool]): If true, only one market in this event can resolve to 'yes'. If false,
            multiple markets can resolve to 'yes'.
        price_level_structure (Union[Unset, str]):
        series_ticker (Union[Unset, str]): Unique identifier for the series this event belongs to.
        strike_date (Union[Unset, Any]):
        strike_period (Union[Unset, str]): The time period this event covers (e.g., 'week', 'month'). Only filled when
            the event uses a period strike (mutually exclusive with strike_date).
        sub_title (Union[Unset, str]): Shortened descriptive title for the event.
        title (Union[Unset, str]): Full title of the event (deprecated, use sub_title instead).
    """

    category: Union[Unset, str] = UNSET
    collateral_return_type: Union[Unset, str] = UNSET
    event_ticker: Union[Unset, str] = UNSET
    markets: Union[Unset, list["GithubComKalshiExchangeInfraSvcApi2ModelMarket"]] = UNSET
    mutually_exclusive: Union[Unset, bool] = UNSET
    price_level_structure: Union[Unset, str] = UNSET
    series_ticker: Union[Unset, str] = UNSET
    strike_date: Union[Unset, Any] = UNSET
    strike_period: Union[Unset, str] = UNSET
    sub_title: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        collateral_return_type = self.collateral_return_type

        event_ticker = self.event_ticker

        markets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.markets, Unset):
            markets = []
            for markets_item_data in self.markets:
                markets_item = markets_item_data.to_dict()
                markets.append(markets_item)

        mutually_exclusive = self.mutually_exclusive

        price_level_structure = self.price_level_structure

        series_ticker = self.series_ticker

        strike_date = self.strike_date

        strike_period = self.strike_period

        sub_title = self.sub_title

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if collateral_return_type is not UNSET:
            field_dict["collateral_return_type"] = collateral_return_type
        if event_ticker is not UNSET:
            field_dict["event_ticker"] = event_ticker
        if markets is not UNSET:
            field_dict["markets"] = markets
        if mutually_exclusive is not UNSET:
            field_dict["mutually_exclusive"] = mutually_exclusive
        if price_level_structure is not UNSET:
            field_dict["price_level_structure"] = price_level_structure
        if series_ticker is not UNSET:
            field_dict["series_ticker"] = series_ticker
        if strike_date is not UNSET:
            field_dict["strike_date"] = strike_date
        if strike_period is not UNSET:
            field_dict["strike_period"] = strike_period
        if sub_title is not UNSET:
            field_dict["sub_title"] = sub_title
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_market import (
            GithubComKalshiExchangeInfraSvcApi2ModelMarket,
        )

        d = dict(src_dict)
        category = d.pop("category", UNSET)

        collateral_return_type = d.pop("collateral_return_type", UNSET)

        event_ticker = d.pop("event_ticker", UNSET)

        markets = []
        _markets = d.pop("markets", UNSET)
        for markets_item_data in _markets or []:
            markets_item = GithubComKalshiExchangeInfraSvcApi2ModelMarket.from_dict(markets_item_data)

            markets.append(markets_item)

        mutually_exclusive = d.pop("mutually_exclusive", UNSET)

        price_level_structure = d.pop("price_level_structure", UNSET)

        series_ticker = d.pop("series_ticker", UNSET)

        strike_date = d.pop("strike_date", UNSET)

        strike_period = d.pop("strike_period", UNSET)

        sub_title = d.pop("sub_title", UNSET)

        title = d.pop("title", UNSET)

        github_com_kalshi_exchange_infra_svc_api_2_model_event_data = cls(
            category=category,
            collateral_return_type=collateral_return_type,
            event_ticker=event_ticker,
            markets=markets,
            mutually_exclusive=mutually_exclusive,
            price_level_structure=price_level_structure,
            series_ticker=series_ticker,
            strike_date=strike_date,
            strike_period=strike_period,
            sub_title=sub_title,
            title=title,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_event_data.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_event_data

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
