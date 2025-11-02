import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.ticker_pair import TickerPair


T = TypeVar("T", bound="LookupPoint")


@_attrs_define
class LookupPoint:
    """
    Attributes:
        event_ticker (str): Event ticker for the lookup point.
        market_ticker (str): Market ticker for the lookup point.
        selected_markets (list['TickerPair']): Markets that were selected for this lookup.
        last_queried_ts (datetime.datetime): Timestamp when this lookup was last queried.
    """

    event_ticker: str
    market_ticker: str
    selected_markets: list["TickerPair"]
    last_queried_ts: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_ticker = self.event_ticker

        market_ticker = self.market_ticker

        selected_markets = []
        for selected_markets_item_data in self.selected_markets:
            selected_markets_item = selected_markets_item_data.to_dict()
            selected_markets.append(selected_markets_item)

        last_queried_ts = self.last_queried_ts.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_ticker": event_ticker,
                "market_ticker": market_ticker,
                "selected_markets": selected_markets,
                "last_queried_ts": last_queried_ts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ticker_pair import TickerPair

        d = dict(src_dict)
        event_ticker = d.pop("event_ticker")

        market_ticker = d.pop("market_ticker")

        selected_markets = []
        _selected_markets = d.pop("selected_markets")
        for selected_markets_item_data in _selected_markets:
            selected_markets_item = TickerPair.from_dict(selected_markets_item_data)

            selected_markets.append(selected_markets_item)

        last_queried_ts = isoparse(d.pop("last_queried_ts"))

        lookup_point = cls(
            event_ticker=event_ticker,
            market_ticker=market_ticker,
            selected_markets=selected_markets,
            last_queried_ts=last_queried_ts,
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
