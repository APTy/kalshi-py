from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.maintenance_window import MaintenanceWindow
    from ..models.weekly_schedule import WeeklySchedule


T = TypeVar("T", bound="Schedule")


@_attrs_define
class Schedule:
    """
    Attributes:
        standard_hours (list['WeeklySchedule']): The standard operating hours of the exchange. All times are expressed
            in ET. Outside of these times trading will be unavailable.
        maintenance_windows (list['MaintenanceWindow']): Scheduled maintenance windows, during which the exchange may be
            unavailable.
    """

    standard_hours: list["WeeklySchedule"]
    maintenance_windows: list["MaintenanceWindow"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        standard_hours = []
        for standard_hours_item_data in self.standard_hours:
            standard_hours_item = standard_hours_item_data.to_dict()
            standard_hours.append(standard_hours_item)

        maintenance_windows = []
        for maintenance_windows_item_data in self.maintenance_windows:
            maintenance_windows_item = maintenance_windows_item_data.to_dict()
            maintenance_windows.append(maintenance_windows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "standard_hours": standard_hours,
                "maintenance_windows": maintenance_windows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.maintenance_window import MaintenanceWindow
        from ..models.weekly_schedule import WeeklySchedule

        d = dict(src_dict)
        standard_hours = []
        _standard_hours = d.pop("standard_hours")
        for standard_hours_item_data in _standard_hours:
            standard_hours_item = WeeklySchedule.from_dict(standard_hours_item_data)

            standard_hours.append(standard_hours_item)

        maintenance_windows = []
        _maintenance_windows = d.pop("maintenance_windows")
        for maintenance_windows_item_data in _maintenance_windows:
            maintenance_windows_item = MaintenanceWindow.from_dict(maintenance_windows_item_data)

            maintenance_windows.append(maintenance_windows_item)

        schedule = cls(
            standard_hours=standard_hours,
            maintenance_windows=maintenance_windows,
        )

        schedule.additional_properties = d
        return schedule

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
