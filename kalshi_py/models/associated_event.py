from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssociatedEvent")


@_attrs_define
class AssociatedEvent:
    """
    Attributes:
        active_quoters (Union[Unset, list[str]]): List of active quoters for this event.
        is_yes_only (Union[Unset, bool]): Whether only the 'yes' side can be used for this event.
        size_max (Union[Unset, int]): Maximum number of markets from this event (inclusive). Null means no limit.
        size_min (Union[Unset, int]): Minimum number of markets from this event (inclusive). Null means no limit.
        ticker (Union[Unset, str]): The event ticker.
    """

    active_quoters: Union[Unset, list[str]] = UNSET
    is_yes_only: Union[Unset, bool] = UNSET
    size_max: Union[Unset, int] = UNSET
    size_min: Union[Unset, int] = UNSET
    ticker: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_quoters: Union[Unset, list[str]] = UNSET
        if not isinstance(self.active_quoters, Unset):
            active_quoters = self.active_quoters

        is_yes_only = self.is_yes_only

        size_max = self.size_max

        size_min = self.size_min

        ticker = self.ticker

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_quoters is not UNSET:
            field_dict["active_quoters"] = active_quoters
        if is_yes_only is not UNSET:
            field_dict["is_yes_only"] = is_yes_only
        if size_max is not UNSET:
            field_dict["size_max"] = size_max
        if size_min is not UNSET:
            field_dict["size_min"] = size_min
        if ticker is not UNSET:
            field_dict["ticker"] = ticker

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active_quoters = cast(list[str], d.pop("active_quoters", UNSET))

        is_yes_only = d.pop("is_yes_only", UNSET)

        size_max = d.pop("size_max", UNSET)

        size_min = d.pop("size_min", UNSET)

        ticker = d.pop("ticker", UNSET)

        associated_event = cls(
            active_quoters=active_quoters,
            is_yes_only=is_yes_only,
            size_max=size_max,
            size_min=size_min,
            ticker=ticker,
        )

        associated_event.additional_properties = d
        return associated_event

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
