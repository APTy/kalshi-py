import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.structured_target_details import StructuredTargetDetails


T = TypeVar("T", bound="StructuredTarget")


@_attrs_define
class StructuredTarget:
    """
    Attributes:
        id (Union[Unset, str]): Unique identifier for the structured target.
        name (Union[Unset, str]): Name of the structured target.
        type_ (Union[Unset, str]): Type of the structured target.
        details (Union[Unset, StructuredTargetDetails]): Additional details about the structured target. Contains
            flexible JSON data specific to the target type.
        source_id (Union[Unset, str]): External source identifier for the structured target, if available (e.g., third-
            party data provider ID).
        last_updated_ts (Union[Unset, datetime.datetime]): Timestamp when this structured target was last updated.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    details: Union[Unset, "StructuredTargetDetails"] = UNSET
    source_id: Union[Unset, str] = UNSET
    last_updated_ts: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_

        details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        source_id = self.source_id

        last_updated_ts: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_ts, Unset):
            last_updated_ts = self.last_updated_ts.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if details is not UNSET:
            field_dict["details"] = details
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if last_updated_ts is not UNSET:
            field_dict["last_updated_ts"] = last_updated_ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.structured_target_details import StructuredTargetDetails

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        _details = d.pop("details", UNSET)
        details: Union[Unset, StructuredTargetDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = StructuredTargetDetails.from_dict(_details)

        source_id = d.pop("source_id", UNSET)

        _last_updated_ts = d.pop("last_updated_ts", UNSET)
        last_updated_ts: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_ts, Unset):
            last_updated_ts = UNSET
        else:
            last_updated_ts = isoparse(_last_updated_ts)

        structured_target = cls(
            id=id,
            name=name,
            type_=type_,
            details=details,
            source_id=source_id,
            last_updated_ts=last_updated_ts,
        )

        structured_target.additional_properties = d
        return structured_target

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
