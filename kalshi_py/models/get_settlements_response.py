from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.settlement import Settlement


T = TypeVar("T", bound="GetSettlementsResponse")


@_attrs_define
class GetSettlementsResponse:
    """
    Attributes:
        settlements (list['Settlement']):
        cursor (Union[Unset, str]):
    """

    settlements: list["Settlement"]
    cursor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        settlements = []
        for settlements_item_data in self.settlements:
            settlements_item = settlements_item_data.to_dict()
            settlements.append(settlements_item)

        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "settlements": settlements,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.settlement import Settlement

        d = dict(src_dict)
        settlements = []
        _settlements = d.pop("settlements")
        for settlements_item_data in _settlements:
            settlements_item = Settlement.from_dict(settlements_item_data)

            settlements.append(settlements_item)

        cursor = d.pop("cursor", UNSET)

        get_settlements_response = cls(
            settlements=settlements,
            cursor=cursor,
        )

        get_settlements_response.additional_properties = d
        return get_settlements_response

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
