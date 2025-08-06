from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.common_exchange_metadata_schedule_maintenance_windows_item import (
        CommonExchangeMetadataScheduleMaintenanceWindowsItem,
    )
    from ..models.common_exchange_metadata_schedule_standard_hours_item import (
        CommonExchangeMetadataScheduleStandardHoursItem,
    )


T = TypeVar("T", bound="CommonExchangeMetadataSchedule")


@_attrs_define
class CommonExchangeMetadataSchedule:
    """
    Attributes:
        maintenance_windows (Union[Unset, list['CommonExchangeMetadataScheduleMaintenanceWindowsItem']]): Scheduled
            maintenance windows, during which the exchange may be unavailable.
        standard_hours (Union[Unset, list['CommonExchangeMetadataScheduleStandardHoursItem']]): The standard operating
            hours of the exchange. All times are expressed in ET. Outside of these times trading will be unavailable.
    """

    maintenance_windows: Union[Unset, list["CommonExchangeMetadataScheduleMaintenanceWindowsItem"]] = UNSET
    standard_hours: Union[Unset, list["CommonExchangeMetadataScheduleStandardHoursItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        maintenance_windows: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.maintenance_windows, Unset):
            maintenance_windows = []
            for maintenance_windows_item_data in self.maintenance_windows:
                maintenance_windows_item = maintenance_windows_item_data.to_dict()
                maintenance_windows.append(maintenance_windows_item)

        standard_hours: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.standard_hours, Unset):
            standard_hours = []
            for standard_hours_item_data in self.standard_hours:
                standard_hours_item = standard_hours_item_data.to_dict()
                standard_hours.append(standard_hours_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if maintenance_windows is not UNSET:
            field_dict["maintenance_windows"] = maintenance_windows
        if standard_hours is not UNSET:
            field_dict["standard_hours"] = standard_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.common_exchange_metadata_schedule_maintenance_windows_item import (
            CommonExchangeMetadataScheduleMaintenanceWindowsItem,
        )
        from ..models.common_exchange_metadata_schedule_standard_hours_item import (
            CommonExchangeMetadataScheduleStandardHoursItem,
        )

        d = dict(src_dict)
        maintenance_windows = []
        _maintenance_windows = d.pop("maintenance_windows", UNSET)
        for maintenance_windows_item_data in _maintenance_windows or []:
            maintenance_windows_item = CommonExchangeMetadataScheduleMaintenanceWindowsItem.from_dict(
                maintenance_windows_item_data
            )

            maintenance_windows.append(maintenance_windows_item)

        standard_hours = []
        _standard_hours = d.pop("standard_hours", UNSET)
        for standard_hours_item_data in _standard_hours or []:
            standard_hours_item = CommonExchangeMetadataScheduleStandardHoursItem.from_dict(standard_hours_item_data)

            standard_hours.append(standard_hours_item)

        common_exchange_metadata_schedule = cls(
            maintenance_windows=maintenance_windows,
            standard_hours=standard_hours,
        )

        common_exchange_metadata_schedule.additional_properties = d
        return common_exchange_metadata_schedule

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
