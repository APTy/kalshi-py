import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_common_exchange_metadata_daily_schedule import (
        GithubComKalshiExchangeInfraCommonExchangeMetadataDailySchedule,
    )
    from ..models.weekly_schedule_monday_item import WeeklyScheduleMondayItem


T = TypeVar("T", bound="WeeklySchedule")


@_attrs_define
class WeeklySchedule:
    """
    Attributes:
        end_time (Union[Unset, datetime.datetime]): End date and time for when this weekly schedule is no longer
            effective.
        friday (Union[Unset, list['GithubComKalshiExchangeInfraCommonExchangeMetadataDailySchedule']]): Trading hours
            for Friday. May contain multiple sessions.
        monday (Union[Unset, list['WeeklyScheduleMondayItem']]): Trading hours for Monday. May contain multiple
            sessions.
        saturday (Union[Unset, list['GithubComKalshiExchangeInfraCommonExchangeMetadataDailySchedule']]): Trading hours
            for Saturday. May contain multiple sessions.
        start_time (Union[Unset, datetime.datetime]): Start date and time for when this weekly schedule is effective.
        sunday (Union[Unset, list['GithubComKalshiExchangeInfraCommonExchangeMetadataDailySchedule']]): Trading hours
            for Sunday. May contain multiple sessions.
        thursday (Union[Unset, list['GithubComKalshiExchangeInfraCommonExchangeMetadataDailySchedule']]): Trading hours
            for Thursday. May contain multiple sessions.
        tuesday (Union[Unset, list['GithubComKalshiExchangeInfraCommonExchangeMetadataDailySchedule']]): Trading hours
            for Tuesday. May contain multiple sessions.
        wednesday (Union[Unset, list['GithubComKalshiExchangeInfraCommonExchangeMetadataDailySchedule']]): Trading hours
            for Wednesday. May contain multiple sessions.
    """

    end_time: Union[Unset, datetime.datetime] = UNSET
    friday: Union[Unset, list["GithubComKalshiExchangeInfraCommonExchangeMetadataDailySchedule"]] = UNSET
    monday: Union[Unset, list["WeeklyScheduleMondayItem"]] = UNSET
    saturday: Union[Unset, list["GithubComKalshiExchangeInfraCommonExchangeMetadataDailySchedule"]] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    sunday: Union[Unset, list["GithubComKalshiExchangeInfraCommonExchangeMetadataDailySchedule"]] = UNSET
    thursday: Union[Unset, list["GithubComKalshiExchangeInfraCommonExchangeMetadataDailySchedule"]] = UNSET
    tuesday: Union[Unset, list["GithubComKalshiExchangeInfraCommonExchangeMetadataDailySchedule"]] = UNSET
    wednesday: Union[Unset, list["GithubComKalshiExchangeInfraCommonExchangeMetadataDailySchedule"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        friday: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.friday, Unset):
            friday = []
            for friday_item_data in self.friday:
                friday_item = friday_item_data.to_dict()
                friday.append(friday_item)

        monday: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.monday, Unset):
            monday = []
            for monday_item_data in self.monday:
                monday_item = monday_item_data.to_dict()
                monday.append(monday_item)

        saturday: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.saturday, Unset):
            saturday = []
            for saturday_item_data in self.saturday:
                saturday_item = saturday_item_data.to_dict()
                saturday.append(saturday_item)

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        sunday: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sunday, Unset):
            sunday = []
            for sunday_item_data in self.sunday:
                sunday_item = sunday_item_data.to_dict()
                sunday.append(sunday_item)

        thursday: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.thursday, Unset):
            thursday = []
            for thursday_item_data in self.thursday:
                thursday_item = thursday_item_data.to_dict()
                thursday.append(thursday_item)

        tuesday: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tuesday, Unset):
            tuesday = []
            for tuesday_item_data in self.tuesday:
                tuesday_item = tuesday_item_data.to_dict()
                tuesday.append(tuesday_item)

        wednesday: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.wednesday, Unset):
            wednesday = []
            for wednesday_item_data in self.wednesday:
                wednesday_item = wednesday_item_data.to_dict()
                wednesday.append(wednesday_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if friday is not UNSET:
            field_dict["friday"] = friday
        if monday is not UNSET:
            field_dict["monday"] = monday
        if saturday is not UNSET:
            field_dict["saturday"] = saturday
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if sunday is not UNSET:
            field_dict["sunday"] = sunday
        if thursday is not UNSET:
            field_dict["thursday"] = thursday
        if tuesday is not UNSET:
            field_dict["tuesday"] = tuesday
        if wednesday is not UNSET:
            field_dict["wednesday"] = wednesday

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_common_exchange_metadata_daily_schedule import (
            GithubComKalshiExchangeInfraCommonExchangeMetadataDailySchedule,
        )
        from ..models.weekly_schedule_monday_item import WeeklyScheduleMondayItem

        d = dict(src_dict)
        _end_time = d.pop("end_time", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        friday = []
        _friday = d.pop("friday", UNSET)
        for friday_item_data in _friday or []:
            friday_item = GithubComKalshiExchangeInfraCommonExchangeMetadataDailySchedule.from_dict(friday_item_data)

            friday.append(friday_item)

        monday = []
        _monday = d.pop("monday", UNSET)
        for monday_item_data in _monday or []:
            monday_item = WeeklyScheduleMondayItem.from_dict(monday_item_data)

            monday.append(monday_item)

        saturday = []
        _saturday = d.pop("saturday", UNSET)
        for saturday_item_data in _saturday or []:
            saturday_item = GithubComKalshiExchangeInfraCommonExchangeMetadataDailySchedule.from_dict(
                saturday_item_data
            )

            saturday.append(saturday_item)

        _start_time = d.pop("start_time", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        sunday = []
        _sunday = d.pop("sunday", UNSET)
        for sunday_item_data in _sunday or []:
            sunday_item = GithubComKalshiExchangeInfraCommonExchangeMetadataDailySchedule.from_dict(sunday_item_data)

            sunday.append(sunday_item)

        thursday = []
        _thursday = d.pop("thursday", UNSET)
        for thursday_item_data in _thursday or []:
            thursday_item = GithubComKalshiExchangeInfraCommonExchangeMetadataDailySchedule.from_dict(
                thursday_item_data
            )

            thursday.append(thursday_item)

        tuesday = []
        _tuesday = d.pop("tuesday", UNSET)
        for tuesday_item_data in _tuesday or []:
            tuesday_item = GithubComKalshiExchangeInfraCommonExchangeMetadataDailySchedule.from_dict(tuesday_item_data)

            tuesday.append(tuesday_item)

        wednesday = []
        _wednesday = d.pop("wednesday", UNSET)
        for wednesday_item_data in _wednesday or []:
            wednesday_item = GithubComKalshiExchangeInfraCommonExchangeMetadataDailySchedule.from_dict(
                wednesday_item_data
            )

            wednesday.append(wednesday_item)

        weekly_schedule = cls(
            end_time=end_time,
            friday=friday,
            monday=monday,
            saturday=saturday,
            start_time=start_time,
            sunday=sunday,
            thursday=thursday,
            tuesday=tuesday,
            wednesday=wednesday,
        )

        weekly_schedule.additional_properties = d
        return weekly_schedule

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
