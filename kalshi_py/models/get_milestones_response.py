from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.milestone import Milestone


T = TypeVar("T", bound="GetMilestonesResponse")


@_attrs_define
class GetMilestonesResponse:
    """
    Attributes:
        milestones (list['Milestone']): List of milestones.
        cursor (Union[Unset, str]): Cursor for pagination.
    """

    milestones: list["Milestone"]
    cursor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        milestones = []
        for milestones_item_data in self.milestones:
            milestones_item = milestones_item_data.to_dict()
            milestones.append(milestones_item)

        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "milestones": milestones,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.milestone import Milestone

        d = dict(src_dict)
        milestones = []
        _milestones = d.pop("milestones")
        for milestones_item_data in _milestones:
            milestones_item = Milestone.from_dict(milestones_item_data)

            milestones.append(milestones_item)

        cursor = d.pop("cursor", UNSET)

        get_milestones_response = cls(
            milestones=milestones,
            cursor=cursor,
        )

        get_milestones_response.additional_properties = d
        return get_milestones_response

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
