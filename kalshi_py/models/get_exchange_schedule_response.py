from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schedule import Schedule


T = TypeVar("T", bound="GetExchangeScheduleResponse")


@_attrs_define
class GetExchangeScheduleResponse:
    """
    Attributes:
        schedule (Schedule):
    """

    schedule: "Schedule"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule = self.schedule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule": schedule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule import Schedule

        d = dict(src_dict)
        schedule = Schedule.from_dict(d.pop("schedule"))

        get_exchange_schedule_response = cls(
            schedule=schedule,
        )

        get_exchange_schedule_response.additional_properties = d
        return get_exchange_schedule_response

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
