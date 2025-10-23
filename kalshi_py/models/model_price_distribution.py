from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelPriceDistribution")


@_attrs_define
class ModelPriceDistribution:
    """
    Attributes:
        close (Union[Unset, int]):
        close_dollars (Union[Unset, str]): Fixed point representation of a subpenny dollar amount e.g. 1.2345 indicates
            $1.23 and 45/100 of a cent. Example: 0.2300.
        high (Union[Unset, int]):
        high_dollars (Union[Unset, str]): Fixed point representation of a subpenny dollar amount e.g. 1.2345 indicates
            $1.23 and 45/100 of a cent. Example: 0.2300.
        low (Union[Unset, int]):
        low_dollars (Union[Unset, str]): Fixed point representation of a subpenny dollar amount e.g. 1.2345 indicates
            $1.23 and 45/100 of a cent. Example: 0.2300.
        mean (Union[Unset, int]):
        mean_dollars (Union[Unset, str]): Fixed point representation of a subpenny dollar amount e.g. 1.2345 indicates
            $1.23 and 45/100 of a cent. Example: 0.2300.
        open_ (Union[Unset, int]):
        open_dollars (Union[Unset, str]): Fixed point representation of a subpenny dollar amount e.g. 1.2345 indicates
            $1.23 and 45/100 of a cent. Example: 0.2300.
        previous (Union[Unset, int]):
        previous_dollars (Union[Unset, str]): Fixed point representation of a subpenny dollar amount e.g. 1.2345
            indicates $1.23 and 45/100 of a cent. Example: 0.2300.
    """

    close: Union[Unset, int] = UNSET
    close_dollars: Union[Unset, str] = UNSET
    high: Union[Unset, int] = UNSET
    high_dollars: Union[Unset, str] = UNSET
    low: Union[Unset, int] = UNSET
    low_dollars: Union[Unset, str] = UNSET
    mean: Union[Unset, int] = UNSET
    mean_dollars: Union[Unset, str] = UNSET
    open_: Union[Unset, int] = UNSET
    open_dollars: Union[Unset, str] = UNSET
    previous: Union[Unset, int] = UNSET
    previous_dollars: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        close = self.close

        close_dollars = self.close_dollars

        high = self.high

        high_dollars = self.high_dollars

        low = self.low

        low_dollars = self.low_dollars

        mean = self.mean

        mean_dollars = self.mean_dollars

        open_ = self.open_

        open_dollars = self.open_dollars

        previous = self.previous

        previous_dollars = self.previous_dollars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if close is not UNSET:
            field_dict["close"] = close
        if close_dollars is not UNSET:
            field_dict["close_dollars"] = close_dollars
        if high is not UNSET:
            field_dict["high"] = high
        if high_dollars is not UNSET:
            field_dict["high_dollars"] = high_dollars
        if low is not UNSET:
            field_dict["low"] = low
        if low_dollars is not UNSET:
            field_dict["low_dollars"] = low_dollars
        if mean is not UNSET:
            field_dict["mean"] = mean
        if mean_dollars is not UNSET:
            field_dict["mean_dollars"] = mean_dollars
        if open_ is not UNSET:
            field_dict["open"] = open_
        if open_dollars is not UNSET:
            field_dict["open_dollars"] = open_dollars
        if previous is not UNSET:
            field_dict["previous"] = previous
        if previous_dollars is not UNSET:
            field_dict["previous_dollars"] = previous_dollars

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        close = d.pop("close", UNSET)

        close_dollars = d.pop("close_dollars", UNSET)

        high = d.pop("high", UNSET)

        high_dollars = d.pop("high_dollars", UNSET)

        low = d.pop("low", UNSET)

        low_dollars = d.pop("low_dollars", UNSET)

        mean = d.pop("mean", UNSET)

        mean_dollars = d.pop("mean_dollars", UNSET)

        open_ = d.pop("open", UNSET)

        open_dollars = d.pop("open_dollars", UNSET)

        previous = d.pop("previous", UNSET)

        previous_dollars = d.pop("previous_dollars", UNSET)

        model_price_distribution = cls(
            close=close,
            close_dollars=close_dollars,
            high=high,
            high_dollars=high_dollars,
            low=low,
            low_dollars=low_dollars,
            mean=mean,
            mean_dollars=mean_dollars,
            open_=open_,
            open_dollars=open_dollars,
            previous=previous,
            previous_dollars=previous_dollars,
        )

        model_price_distribution.additional_properties = d
        return model_price_distribution

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
