from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.market_candlestick import MarketCandlestick


T = TypeVar("T", bound="GetMarketCandlesticksResponse")


@_attrs_define
class GetMarketCandlesticksResponse:
    """
    Attributes:
        ticker (str): Unique identifier for the market.
        candlesticks (list['MarketCandlestick']): Array of candlestick data points for the specified time range.
    """

    ticker: str
    candlesticks: list["MarketCandlestick"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticker = self.ticker

        candlesticks = []
        for candlesticks_item_data in self.candlesticks:
            candlesticks_item = candlesticks_item_data.to_dict()
            candlesticks.append(candlesticks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticker": ticker,
                "candlesticks": candlesticks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.market_candlestick import MarketCandlestick

        d = dict(src_dict)
        ticker = d.pop("ticker")

        candlesticks = []
        _candlesticks = d.pop("candlesticks")
        for candlesticks_item_data in _candlesticks:
            candlesticks_item = MarketCandlestick.from_dict(candlesticks_item_data)

            candlesticks.append(candlesticks_item)

        get_market_candlesticks_response = cls(
            ticker=ticker,
            candlesticks=candlesticks,
        )

        get_market_candlesticks_response.additional_properties = d
        return get_market_candlesticks_response

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
