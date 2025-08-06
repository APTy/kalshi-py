import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Announcement")


@_attrs_define
class Announcement:
    """
    Attributes:
        delivery_time (Union[Unset, datetime.datetime]): The time the announcement was delivered.
        message (Union[Unset, str]): The message contained within the announcement.
        status (Union[Unset, str]):
        type_ (Union[Unset, str]):
    """

    delivery_time: Union[Unset, datetime.datetime] = UNSET
    message: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delivery_time: Union[Unset, str] = UNSET
        if not isinstance(self.delivery_time, Unset):
            delivery_time = self.delivery_time.isoformat()

        message = self.message

        status = self.status

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delivery_time is not UNSET:
            field_dict["delivery_time"] = delivery_time
        if message is not UNSET:
            field_dict["message"] = message
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _delivery_time = d.pop("delivery_time", UNSET)
        delivery_time: Union[Unset, datetime.datetime]
        if isinstance(_delivery_time, Unset):
            delivery_time = UNSET
        else:
            delivery_time = isoparse(_delivery_time)

        message = d.pop("message", UNSET)

        status = d.pop("status", UNSET)

        type_ = d.pop("type", UNSET)

        announcement = cls(
            delivery_time=delivery_time,
            message=message,
            status=status,
            type_=type_,
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
