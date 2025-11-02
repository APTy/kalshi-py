import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.announcement_status import AnnouncementStatus
from ..models.announcement_type import AnnouncementType

T = TypeVar("T", bound="Announcement")


@_attrs_define
class Announcement:
    """
    Attributes:
        type_ (AnnouncementType): The type of the announcement.
        message (str): The message contained within the announcement.
        delivery_time (datetime.datetime): The time the announcement was delivered.
        status (AnnouncementStatus): The current status of this announcement.
    """

    type_: AnnouncementType
    message: str
    delivery_time: datetime.datetime
    status: AnnouncementStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        message = self.message

        delivery_time = self.delivery_time.isoformat()

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "message": message,
                "delivery_time": delivery_time,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = AnnouncementType(d.pop("type"))

        message = d.pop("message")

        delivery_time = isoparse(d.pop("delivery_time"))

        status = AnnouncementStatus(d.pop("status"))

        announcement = cls(
            type_=type_,
            message=message,
            delivery_time=delivery_time,
            status=status,
        )

        announcement.additional_properties = d
        return announcement

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
