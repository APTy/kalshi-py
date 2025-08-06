from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WeeklyScheduleMondayItem")


@_attrs_define
class WeeklyScheduleMondayItem:
    """
    Attributes:
        close_time (Union[Unset, str]): Closing time in ET (Eastern Time) format HH:MM.
        open_time (Union[Unset, str]): Opening time in ET (Eastern Time) format HH:MM.
    """

    close_time: Union[Unset, str] = UNSET
    open_time: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        close_time = self.close_time

        open_time = self.open_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if close_time is not UNSET:
            field_dict["close_time"] = close_time
        if open_time is not UNSET:
            field_dict["open_time"] = open_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        close_time = d.pop("close_time", UNSET)

        open_time = d.pop("open_time", UNSET)

        weekly_schedule_monday_item = cls(
            close_time=close_time,
            open_time=open_time,
        )

        weekly_schedule_monday_item.additional_properties = d
        return weekly_schedule_monday_item

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
