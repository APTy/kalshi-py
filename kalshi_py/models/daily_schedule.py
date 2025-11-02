from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DailySchedule")


@_attrs_define
class DailySchedule:
    """
    Attributes:
        open_time (str): Opening time in ET (Eastern Time) format HH:MM.
        close_time (str): Closing time in ET (Eastern Time) format HH:MM.
    """

    open_time: str
    close_time: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_time = self.open_time

        close_time = self.close_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "open_time": open_time,
                "close_time": close_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        open_time = d.pop("open_time")

        close_time = d.pop("close_time")

        daily_schedule = cls(
            open_time=open_time,
            close_time=close_time,
        )

        daily_schedule.additional_properties = d
        return daily_schedule

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
