from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_group import OrderGroup


T = TypeVar("T", bound="GetOrderGroupsResponse")


@_attrs_define
class GetOrderGroupsResponse:
    """
    Attributes:
        order_groups (Union[Unset, list['OrderGroup']]):
        cursor (Union[Unset, str]):
    """

    order_groups: Union[Unset, list["OrderGroup"]] = UNSET
    cursor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.order_groups, Unset):
            order_groups = []
            for order_groups_item_data in self.order_groups:
                order_groups_item = order_groups_item_data.to_dict()
                order_groups.append(order_groups_item)

        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_groups is not UNSET:
            field_dict["order_groups"] = order_groups
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_group import OrderGroup

        d = dict(src_dict)
        order_groups = []
        _order_groups = d.pop("order_groups", UNSET)
        for order_groups_item_data in _order_groups or []:
            order_groups_item = OrderGroup.from_dict(order_groups_item_data)

            order_groups.append(order_groups_item)

        cursor = d.pop("cursor", UNSET)

        get_order_groups_response = cls(
            order_groups=order_groups,
            cursor=cursor,
        )

        get_order_groups_response.additional_properties = d
        return get_order_groups_response

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
