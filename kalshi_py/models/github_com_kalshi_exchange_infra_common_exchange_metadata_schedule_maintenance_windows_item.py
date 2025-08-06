import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraCommonExchangeMetadataScheduleMaintenanceWindowsItem")


@_attrs_define
class GithubComKalshiExchangeInfraCommonExchangeMetadataScheduleMaintenanceWindowsItem:
    """
    Attributes:
        end_datetime (Union[Unset, datetime.datetime]): End date and time of the maintenance window.
        start_datetime (Union[Unset, datetime.datetime]): Start date and time of the maintenance window.
    """

    end_datetime: Union[Unset, datetime.datetime] = UNSET
    start_datetime: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_datetime: Union[Unset, str] = UNSET
        if not isinstance(self.end_datetime, Unset):
            end_datetime = self.end_datetime.isoformat()

        start_datetime: Union[Unset, str] = UNSET
        if not isinstance(self.start_datetime, Unset):
            start_datetime = self.start_datetime.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_datetime is not UNSET:
            field_dict["end_datetime"] = end_datetime
        if start_datetime is not UNSET:
            field_dict["start_datetime"] = start_datetime

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _end_datetime = d.pop("end_datetime", UNSET)
        end_datetime: Union[Unset, datetime.datetime]
        if isinstance(_end_datetime, Unset):
            end_datetime = UNSET
        else:
            end_datetime = isoparse(_end_datetime)

        _start_datetime = d.pop("start_datetime", UNSET)
        start_datetime: Union[Unset, datetime.datetime]
        if isinstance(_start_datetime, Unset):
            start_datetime = UNSET
        else:
            start_datetime = isoparse(_start_datetime)

        github_com_kalshi_exchange_infra_common_exchange_metadata_schedule_maintenance_windows_item = cls(
            end_datetime=end_datetime,
            start_datetime=start_datetime,
        )

        github_com_kalshi_exchange_infra_common_exchange_metadata_schedule_maintenance_windows_item.additional_properties = d
        return github_com_kalshi_exchange_infra_common_exchange_metadata_schedule_maintenance_windows_item

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
