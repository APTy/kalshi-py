import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="MaintenanceWindow")


@_attrs_define
class MaintenanceWindow:
    """
    Attributes:
        start_datetime (datetime.datetime): Start date and time of the maintenance window.
        end_datetime (datetime.datetime): End date and time of the maintenance window.
    """

    start_datetime: datetime.datetime
    end_datetime: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_datetime = self.start_datetime.isoformat()

        end_datetime = self.end_datetime.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_datetime": start_datetime,
                "end_datetime": end_datetime,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_datetime = isoparse(d.pop("start_datetime"))

        end_datetime = isoparse(d.pop("end_datetime"))

        maintenance_window = cls(
            start_datetime=start_datetime,
            end_datetime=end_datetime,
        )

        maintenance_window.additional_properties = d
        return maintenance_window

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
