from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PriceDistribution")


@_attrs_define
class PriceDistribution:
    """
    Attributes:
        open_ (Union[None, Unset, int]): First traded YES contract price on the market during the candlestick period (in
            cents). May be null if there was no trade during the period.
        open_dollars (Union[None, Unset, str]): First traded YES contract price on the market during the candlestick
            period (in dollars). May be null if there was no trade during the period.
        low (Union[None, Unset, int]): Lowest traded YES contract price on the market during the candlestick period (in
            cents). May be null if there was no trade during the period.
        low_dollars (Union[None, Unset, str]): Lowest traded YES contract price on the market during the candlestick
            period (in dollars). May be null if there was no trade during the period.
        high (Union[None, Unset, int]): Highest traded YES contract price on the market during the candlestick period
            (in cents). May be null if there was no trade during the period.
        high_dollars (Union[None, Unset, str]): Highest traded YES contract price on the market during the candlestick
            period (in dollars). May be null if there was no trade during the period.
        close (Union[None, Unset, int]): Last traded YES contract price on the market during the candlestick period (in
            cents). May be null if there was no trade during the period.
        close_dollars (Union[None, Unset, str]): Last traded YES contract price on the market during the candlestick
            period (in dollars). May be null if there was no trade during the period.
        mean (Union[None, Unset, int]): Mean traded YES contract price on the market during the candlestick period (in
            cents). May be null if there was no trade during the period.
        mean_dollars (Union[None, Unset, str]): Mean traded YES contract price on the market during the candlestick
            period (in dollars). May be null if there was no trade during the period.
        previous (Union[None, Unset, int]): Last traded YES contract price on the market before the candlestick period
            (in cents). May be null if there were no trades before the period.
        previous_dollars (Union[None, Unset, str]): Last traded YES contract price on the market before the candlestick
            period (in dollars). May be null if there were no trades before the period.
        min_ (Union[None, Unset, int]): Minimum close price of any market during the candlestick period (in cents).
        min_dollars (Union[None, Unset, str]): Minimum close price of any market during the candlestick period (in
            dollars).
        max_ (Union[None, Unset, int]): Maximum close price of any market during the candlestick period (in cents).
        max_dollars (Union[None, Unset, str]): Maximum close price of any market during the candlestick period (in
            dollars).
    """

    open_: Union[None, Unset, int] = UNSET
    open_dollars: Union[None, Unset, str] = UNSET
    low: Union[None, Unset, int] = UNSET
    low_dollars: Union[None, Unset, str] = UNSET
    high: Union[None, Unset, int] = UNSET
    high_dollars: Union[None, Unset, str] = UNSET
    close: Union[None, Unset, int] = UNSET
    close_dollars: Union[None, Unset, str] = UNSET
    mean: Union[None, Unset, int] = UNSET
    mean_dollars: Union[None, Unset, str] = UNSET
    previous: Union[None, Unset, int] = UNSET
    previous_dollars: Union[None, Unset, str] = UNSET
    min_: Union[None, Unset, int] = UNSET
    min_dollars: Union[None, Unset, str] = UNSET
    max_: Union[None, Unset, int] = UNSET
    max_dollars: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_: Union[None, Unset, int]
        if isinstance(self.open_, Unset):
            open_ = UNSET
        else:
            open_ = self.open_

        open_dollars: Union[None, Unset, str]
        if isinstance(self.open_dollars, Unset):
            open_dollars = UNSET
        else:
            open_dollars = self.open_dollars

        low: Union[None, Unset, int]
        if isinstance(self.low, Unset):
            low = UNSET
        else:
            low = self.low

        low_dollars: Union[None, Unset, str]
        if isinstance(self.low_dollars, Unset):
            low_dollars = UNSET
        else:
            low_dollars = self.low_dollars

        high: Union[None, Unset, int]
        if isinstance(self.high, Unset):
            high = UNSET
        else:
            high = self.high

        high_dollars: Union[None, Unset, str]
        if isinstance(self.high_dollars, Unset):
            high_dollars = UNSET
        else:
            high_dollars = self.high_dollars

        close: Union[None, Unset, int]
        if isinstance(self.close, Unset):
            close = UNSET
        else:
            close = self.close

        close_dollars: Union[None, Unset, str]
        if isinstance(self.close_dollars, Unset):
            close_dollars = UNSET
        else:
            close_dollars = self.close_dollars

        mean: Union[None, Unset, int]
        if isinstance(self.mean, Unset):
            mean = UNSET
        else:
            mean = self.mean

        mean_dollars: Union[None, Unset, str]
        if isinstance(self.mean_dollars, Unset):
            mean_dollars = UNSET
        else:
            mean_dollars = self.mean_dollars

        previous: Union[None, Unset, int]
        if isinstance(self.previous, Unset):
            previous = UNSET
        else:
            previous = self.previous

        previous_dollars: Union[None, Unset, str]
        if isinstance(self.previous_dollars, Unset):
            previous_dollars = UNSET
        else:
            previous_dollars = self.previous_dollars

        min_: Union[None, Unset, int]
        if isinstance(self.min_, Unset):
            min_ = UNSET
        else:
            min_ = self.min_

        min_dollars: Union[None, Unset, str]
        if isinstance(self.min_dollars, Unset):
            min_dollars = UNSET
        else:
            min_dollars = self.min_dollars

        max_: Union[None, Unset, int]
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        max_dollars: Union[None, Unset, str]
        if isinstance(self.max_dollars, Unset):
            max_dollars = UNSET
        else:
            max_dollars = self.max_dollars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if open_ is not UNSET:
            field_dict["open"] = open_
        if open_dollars is not UNSET:
            field_dict["open_dollars"] = open_dollars
        if low is not UNSET:
            field_dict["low"] = low
        if low_dollars is not UNSET:
            field_dict["low_dollars"] = low_dollars
        if high is not UNSET:
            field_dict["high"] = high
        if high_dollars is not UNSET:
            field_dict["high_dollars"] = high_dollars
        if close is not UNSET:
            field_dict["close"] = close
        if close_dollars is not UNSET:
            field_dict["close_dollars"] = close_dollars
        if mean is not UNSET:
            field_dict["mean"] = mean
        if mean_dollars is not UNSET:
            field_dict["mean_dollars"] = mean_dollars
        if previous is not UNSET:
            field_dict["previous"] = previous
        if previous_dollars is not UNSET:
            field_dict["previous_dollars"] = previous_dollars
        if min_ is not UNSET:
            field_dict["min"] = min_
        if min_dollars is not UNSET:
            field_dict["min_dollars"] = min_dollars
        if max_ is not UNSET:
            field_dict["max"] = max_
        if max_dollars is not UNSET:
            field_dict["max_dollars"] = max_dollars

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_open_(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        open_ = _parse_open_(d.pop("open", UNSET))

        def _parse_open_dollars(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        open_dollars = _parse_open_dollars(d.pop("open_dollars", UNSET))

        def _parse_low(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        low = _parse_low(d.pop("low", UNSET))

        def _parse_low_dollars(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        low_dollars = _parse_low_dollars(d.pop("low_dollars", UNSET))

        def _parse_high(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        high = _parse_high(d.pop("high", UNSET))

        def _parse_high_dollars(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        high_dollars = _parse_high_dollars(d.pop("high_dollars", UNSET))

        def _parse_close(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        close = _parse_close(d.pop("close", UNSET))

        def _parse_close_dollars(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        close_dollars = _parse_close_dollars(d.pop("close_dollars", UNSET))

        def _parse_mean(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        mean = _parse_mean(d.pop("mean", UNSET))

        def _parse_mean_dollars(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mean_dollars = _parse_mean_dollars(d.pop("mean_dollars", UNSET))

        def _parse_previous(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        previous = _parse_previous(d.pop("previous", UNSET))

        def _parse_previous_dollars(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        previous_dollars = _parse_previous_dollars(d.pop("previous_dollars", UNSET))

        def _parse_min_(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        min_ = _parse_min_(d.pop("min", UNSET))

        def _parse_min_dollars(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        min_dollars = _parse_min_dollars(d.pop("min_dollars", UNSET))

        def _parse_max_(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_ = _parse_max_(d.pop("max", UNSET))

        def _parse_max_dollars(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        max_dollars = _parse_max_dollars(d.pop("max_dollars", UNSET))

        price_distribution = cls(
            open_=open_,
            open_dollars=open_dollars,
            low=low,
            low_dollars=low_dollars,
            high=high,
            high_dollars=high_dollars,
            close=close,
            close_dollars=close_dollars,
            mean=mean,
            mean_dollars=mean_dollars,
            previous=previous,
            previous_dollars=previous_dollars,
            min_=min_,
            min_dollars=min_dollars,
            max_=max_,
            max_dollars=max_dollars,
        )

        price_distribution.additional_properties = d
        return price_distribution

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
