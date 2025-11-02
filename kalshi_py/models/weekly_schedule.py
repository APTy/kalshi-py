import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.daily_schedule import DailySchedule


T = TypeVar("T", bound="WeeklySchedule")


@_attrs_define
class WeeklySchedule:
    """
    Attributes:
        start_time (datetime.datetime): Start date and time for when this weekly schedule is effective.
        end_time (datetime.datetime): End date and time for when this weekly schedule is no longer effective.
        monday (list['DailySchedule']): Trading hours for Monday. May contain multiple sessions.
        tuesday (list['DailySchedule']): Trading hours for Tuesday. May contain multiple sessions.
        wednesday (list['DailySchedule']): Trading hours for Wednesday. May contain multiple sessions.
        thursday (list['DailySchedule']): Trading hours for Thursday. May contain multiple sessions.
        friday (list['DailySchedule']): Trading hours for Friday. May contain multiple sessions.
        saturday (list['DailySchedule']): Trading hours for Saturday. May contain multiple sessions.
        sunday (list['DailySchedule']): Trading hours for Sunday. May contain multiple sessions.
    """

    start_time: datetime.datetime
    end_time: datetime.datetime
    monday: list["DailySchedule"]
    tuesday: list["DailySchedule"]
    wednesday: list["DailySchedule"]
    thursday: list["DailySchedule"]
    friday: list["DailySchedule"]
    saturday: list["DailySchedule"]
    sunday: list["DailySchedule"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        monday = []
        for monday_item_data in self.monday:
            monday_item = monday_item_data.to_dict()
            monday.append(monday_item)

        tuesday = []
        for tuesday_item_data in self.tuesday:
            tuesday_item = tuesday_item_data.to_dict()
            tuesday.append(tuesday_item)

        wednesday = []
        for wednesday_item_data in self.wednesday:
            wednesday_item = wednesday_item_data.to_dict()
            wednesday.append(wednesday_item)

        thursday = []
        for thursday_item_data in self.thursday:
            thursday_item = thursday_item_data.to_dict()
            thursday.append(thursday_item)

        friday = []
        for friday_item_data in self.friday:
            friday_item = friday_item_data.to_dict()
            friday.append(friday_item)

        saturday = []
        for saturday_item_data in self.saturday:
            saturday_item = saturday_item_data.to_dict()
            saturday.append(saturday_item)

        sunday = []
        for sunday_item_data in self.sunday:
            sunday_item = sunday_item_data.to_dict()
            sunday.append(sunday_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_time": start_time,
                "end_time": end_time,
                "monday": monday,
                "tuesday": tuesday,
                "wednesday": wednesday,
                "thursday": thursday,
                "friday": friday,
                "saturday": saturday,
                "sunday": sunday,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.daily_schedule import DailySchedule

        d = dict(src_dict)
        start_time = isoparse(d.pop("start_time"))

        end_time = isoparse(d.pop("end_time"))

        monday = []
        _monday = d.pop("monday")
        for monday_item_data in _monday:
            monday_item = DailySchedule.from_dict(monday_item_data)

            monday.append(monday_item)

        tuesday = []
        _tuesday = d.pop("tuesday")
        for tuesday_item_data in _tuesday:
            tuesday_item = DailySchedule.from_dict(tuesday_item_data)

            tuesday.append(tuesday_item)

        wednesday = []
        _wednesday = d.pop("wednesday")
        for wednesday_item_data in _wednesday:
            wednesday_item = DailySchedule.from_dict(wednesday_item_data)

            wednesday.append(wednesday_item)

        thursday = []
        _thursday = d.pop("thursday")
        for thursday_item_data in _thursday:
            thursday_item = DailySchedule.from_dict(thursday_item_data)

            thursday.append(thursday_item)

        friday = []
        _friday = d.pop("friday")
        for friday_item_data in _friday:
            friday_item = DailySchedule.from_dict(friday_item_data)

            friday.append(friday_item)

        saturday = []
        _saturday = d.pop("saturday")
        for saturday_item_data in _saturday:
            saturday_item = DailySchedule.from_dict(saturday_item_data)

            saturday.append(saturday_item)

        sunday = []
        _sunday = d.pop("sunday")
        for sunday_item_data in _sunday:
            sunday_item = DailySchedule.from_dict(sunday_item_data)

            sunday.append(sunday_item)

        weekly_schedule = cls(
            start_time=start_time,
            end_time=end_time,
            monday=monday,
            tuesday=tuesday,
            wednesday=wednesday,
            thursday=thursday,
            friday=friday,
            saturday=saturday,
            sunday=sunday,
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
