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
        ticker (str): The event ticker.
        is_yes_only (bool): Whether only the 'yes' side can be used for this event.
        active_quoters (list[str]): List of active quoters for this event.
        size_max (Union[None, Unset, int]): Maximum number of markets from this event (inclusive). Null means no limit.
        size_min (Union[None, Unset, int]): Minimum number of markets from this event (inclusive). Null means no limit.
    """

    ticker: str
    is_yes_only: bool
    active_quoters: list[str]
    size_max: Union[None, Unset, int] = UNSET
    size_min: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticker = self.ticker

        is_yes_only = self.is_yes_only

        active_quoters = self.active_quoters

        size_max: Union[None, Unset, int]
        if isinstance(self.size_max, Unset):
            size_max = UNSET
        else:
            size_max = self.size_max

        size_min: Union[None, Unset, int]
        if isinstance(self.size_min, Unset):
            size_min = UNSET
        else:
            size_min = self.size_min

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticker": ticker,
                "is_yes_only": is_yes_only,
                "active_quoters": active_quoters,
            }
        )
        if size_max is not UNSET:
            field_dict["size_max"] = size_max
        if size_min is not UNSET:
            field_dict["size_min"] = size_min

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ticker = d.pop("ticker")

        is_yes_only = d.pop("is_yes_only")

        active_quoters = cast(list[str], d.pop("active_quoters"))

        def _parse_size_max(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size_max = _parse_size_max(d.pop("size_max", UNSET))

        def _parse_size_min(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size_min = _parse_size_min(d.pop("size_min", UNSET))

        associated_event = cls(
            ticker=ticker,
            is_yes_only=is_yes_only,
            active_quoters=active_quoters,
            size_max=size_max,
            size_min=size_min,
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
