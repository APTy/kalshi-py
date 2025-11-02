from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.market_candlestick import MarketCandlestick


T = TypeVar("T", bound="GetEventCandlesticksResponse")


@_attrs_define
class GetEventCandlesticksResponse:
    """
    Attributes:
        market_tickers (list[str]): Array of market tickers in the event.
        market_candlesticks (list[list['MarketCandlestick']]): Array of market candlestick arrays, one for each market
            in the event.
        adjusted_end_ts (int): Adjusted end timestamp if the requested candlesticks would be larger than
            maxAggregateCandidates.
    """

    market_tickers: list[str]
    market_candlesticks: list[list["MarketCandlestick"]]
    adjusted_end_ts: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        market_tickers = self.market_tickers

        market_candlesticks = []
        for market_candlesticks_item_data in self.market_candlesticks:
            market_candlesticks_item = []
            for market_candlesticks_item_item_data in market_candlesticks_item_data:
                market_candlesticks_item_item = market_candlesticks_item_item_data.to_dict()
                market_candlesticks_item.append(market_candlesticks_item_item)

            market_candlesticks.append(market_candlesticks_item)

        adjusted_end_ts = self.adjusted_end_ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "market_tickers": market_tickers,
                "market_candlesticks": market_candlesticks,
                "adjusted_end_ts": adjusted_end_ts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.market_candlestick import MarketCandlestick

        d = dict(src_dict)
        market_tickers = cast(list[str], d.pop("market_tickers"))

        market_candlesticks = []
        _market_candlesticks = d.pop("market_candlesticks")
        for market_candlesticks_item_data in _market_candlesticks:
            market_candlesticks_item = []
            _market_candlesticks_item = market_candlesticks_item_data
            for market_candlesticks_item_item_data in _market_candlesticks_item:
                market_candlesticks_item_item = MarketCandlestick.from_dict(market_candlesticks_item_item_data)

                market_candlesticks_item.append(market_candlesticks_item_item)

            market_candlesticks.append(market_candlesticks_item)

        adjusted_end_ts = d.pop("adjusted_end_ts")

        get_event_candlesticks_response = cls(
            market_tickers=market_tickers,
            market_candlesticks=market_candlesticks,
            adjusted_end_ts=adjusted_end_ts,
        )

        get_event_candlesticks_response.additional_properties = d
        return get_event_candlesticks_response

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
