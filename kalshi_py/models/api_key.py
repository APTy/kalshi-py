import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiKey")


@_attrs_define
class ApiKey:
    """
    Attributes:
        api_key_id (Union[Unset, str]): Unique identifier for the API key.
        created_ts (Union[Unset, datetime.datetime]): Timestamp when the API key was created.
        name (Union[Unset, str]): User-provided name for the API key.
    """

    api_key_id: Union[Unset, str] = UNSET
    created_ts: Union[Unset, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key_id = self.api_key_id

        created_ts: Union[Unset, str] = UNSET
        if not isinstance(self.created_ts, Unset):
            created_ts = self.created_ts.isoformat()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key_id is not UNSET:
            field_dict["api_key_id"] = api_key_id
        if created_ts is not UNSET:
            field_dict["created_ts"] = created_ts
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key_id = d.pop("api_key_id", UNSET)

        _created_ts = d.pop("created_ts", UNSET)
        created_ts: Union[Unset, datetime.datetime]
        if isinstance(_created_ts, Unset):
            created_ts = UNSET
        else:
            created_ts = isoparse(_created_ts)

        name = d.pop("name", UNSET)

        api_key = cls(
            api_key_id=api_key_id,
            created_ts=created_ts,
            name=name,
        )

        api_key.additional_properties = d
        return api_key

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
