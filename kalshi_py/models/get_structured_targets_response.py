from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.structured_target import StructuredTarget


T = TypeVar("T", bound="GetStructuredTargetsResponse")


@_attrs_define
class GetStructuredTargetsResponse:
    """
    Attributes:
        structured_targets (Union[Unset, list['StructuredTarget']]):
        cursor (Union[Unset, str]): Pagination cursor for the next page. Empty if there are no more results.
    """

    structured_targets: Union[Unset, list["StructuredTarget"]] = UNSET
    cursor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        structured_targets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.structured_targets, Unset):
            structured_targets = []
            for structured_targets_item_data in self.structured_targets:
                structured_targets_item = structured_targets_item_data.to_dict()
                structured_targets.append(structured_targets_item)

        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if structured_targets is not UNSET:
            field_dict["structured_targets"] = structured_targets
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.structured_target import StructuredTarget

        d = dict(src_dict)
        structured_targets = []
        _structured_targets = d.pop("structured_targets", UNSET)
        for structured_targets_item_data in _structured_targets or []:
            structured_targets_item = StructuredTarget.from_dict(structured_targets_item_data)

            structured_targets.append(structured_targets_item)

        cursor = d.pop("cursor", UNSET)

        get_structured_targets_response = cls(
            structured_targets=structured_targets,
            cursor=cursor,
        )

        get_structured_targets_response.additional_properties = d
        return get_structured_targets_response

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
