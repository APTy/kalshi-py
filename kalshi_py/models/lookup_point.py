import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_ticker_pair import (
        GithubComKalshiExchangeInfraSvcApi2ModelTickerPair,
    )


T = TypeVar("T", bound="LookupPoint")


@_attrs_define
class LookupPoint:
    """
    Attributes:
        event_ticker (Union[Unset, str]): Event ticker for the lookup point.
        last_queried_ts (Union[Unset, datetime.datetime]): Timestamp when this lookup was last queried.
        market_ticker (Union[Unset, str]): Market ticker for the lookup point.
        selected_markets (Union[Unset, list['GithubComKalshiExchangeInfraSvcApi2ModelTickerPair']]): Markets that were
            selected for this lookup.
    """

    event_ticker: Union[Unset, str] = UNSET
    last_queried_ts: Union[Unset, datetime.datetime] = UNSET
    market_ticker: Union[Unset, str] = UNSET
    selected_markets: Union[Unset, list["GithubComKalshiExchangeInfraSvcApi2ModelTickerPair"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_ticker = self.event_ticker

        last_queried_ts: Union[Unset, str] = UNSET
        if not isinstance(self.last_queried_ts, Unset):
            last_queried_ts = self.last_queried_ts.isoformat()

        market_ticker = self.market_ticker

        selected_markets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.selected_markets, Unset):
            selected_markets = []
            for selected_markets_item_data in self.selected_markets:
                selected_markets_item = selected_markets_item_data.to_dict()
                selected_markets.append(selected_markets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_ticker is not UNSET:
            field_dict["event_ticker"] = event_ticker
        if last_queried_ts is not UNSET:
            field_dict["last_queried_ts"] = last_queried_ts
        if market_ticker is not UNSET:
            field_dict["market_ticker"] = market_ticker
        if selected_markets is not UNSET:
            field_dict["selected_markets"] = selected_markets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_ticker_pair import (
            GithubComKalshiExchangeInfraSvcApi2ModelTickerPair,
        )

        d = dict(src_dict)
        event_ticker = d.pop("event_ticker", UNSET)

        _last_queried_ts = d.pop("last_queried_ts", UNSET)
        last_queried_ts: Union[Unset, datetime.datetime]
        if isinstance(_last_queried_ts, Unset):
            last_queried_ts = UNSET
        else:
            last_queried_ts = isoparse(_last_queried_ts)

        market_ticker = d.pop("market_ticker", UNSET)

        selected_markets = []
        _selected_markets = d.pop("selected_markets", UNSET)
        for selected_markets_item_data in _selected_markets or []:
            selected_markets_item = GithubComKalshiExchangeInfraSvcApi2ModelTickerPair.from_dict(
                selected_markets_item_data
            )

            selected_markets.append(selected_markets_item)

        lookup_point = cls(
            event_ticker=event_ticker,
            last_queried_ts=last_queried_ts,
            market_ticker=market_ticker,
            selected_markets=selected_markets,
        )

        lookup_point.additional_properties = d
        return lookup_point

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
