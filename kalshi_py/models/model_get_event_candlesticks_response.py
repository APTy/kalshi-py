from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_get_event_candlesticks_response_market_candlesticks_item_item import (
        ModelGetEventCandlesticksResponseMarketCandlesticksItemItem,
    )


T = TypeVar("T", bound="ModelGetEventCandlesticksResponse")


@_attrs_define
class ModelGetEventCandlesticksResponse:
    """
    Attributes:
        adjusted_end_ts (Union[Unset, int]): Adjusted end timestamp if the requested candlesticks would be larger than
            maxAggregateCandidates.
        market_candlesticks (Union[Unset, list[list['ModelGetEventCandlesticksResponseMarketCandlesticksItemItem']]]):
            Array of market candlestick arrays, one for each market in the event.
        market_tickers (Union[Unset, list[str]]): Array of market tickers in the event.
    """

    adjusted_end_ts: Union[Unset, int] = UNSET
    market_candlesticks: Union[Unset, list[list["ModelGetEventCandlesticksResponseMarketCandlesticksItemItem"]]] = UNSET
    market_tickers: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adjusted_end_ts = self.adjusted_end_ts

        market_candlesticks: Union[Unset, list[list[dict[str, Any]]]] = UNSET
        if not isinstance(self.market_candlesticks, Unset):
            market_candlesticks = []
            for market_candlesticks_item_data in self.market_candlesticks:
                market_candlesticks_item = []
                for market_candlesticks_item_item_data in market_candlesticks_item_data:
                    market_candlesticks_item_item = market_candlesticks_item_item_data.to_dict()
                    market_candlesticks_item.append(market_candlesticks_item_item)

                market_candlesticks.append(market_candlesticks_item)

        market_tickers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.market_tickers, Unset):
            market_tickers = self.market_tickers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adjusted_end_ts is not UNSET:
            field_dict["adjusted_end_ts"] = adjusted_end_ts
        if market_candlesticks is not UNSET:
            field_dict["market_candlesticks"] = market_candlesticks
        if market_tickers is not UNSET:
            field_dict["market_tickers"] = market_tickers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_get_event_candlesticks_response_market_candlesticks_item_item import (
            ModelGetEventCandlesticksResponseMarketCandlesticksItemItem,
        )

        d = dict(src_dict)
        adjusted_end_ts = d.pop("adjusted_end_ts", UNSET)

        market_candlesticks = []
        _market_candlesticks = d.pop("market_candlesticks", UNSET)
        for market_candlesticks_item_data in _market_candlesticks or []:
            market_candlesticks_item = []
            _market_candlesticks_item = market_candlesticks_item_data
            for market_candlesticks_item_item_data in _market_candlesticks_item:
                market_candlesticks_item_item = ModelGetEventCandlesticksResponseMarketCandlesticksItemItem.from_dict(
                    market_candlesticks_item_item_data
                )

                market_candlesticks_item.append(market_candlesticks_item_item)

            market_candlesticks.append(market_candlesticks_item)

        market_tickers = cast(list[str], d.pop("market_tickers", UNSET))

        model_get_event_candlesticks_response = cls(
            adjusted_end_ts=adjusted_end_ts,
            market_candlesticks=market_candlesticks,
            market_tickers=market_tickers,
        )

        model_get_event_candlesticks_response.additional_properties = d
        return model_get_event_candlesticks_response

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
