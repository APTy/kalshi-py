from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_order_group_summary import ModelOrderGroupSummary


T = TypeVar("T", bound="ModelGetOrderGroupsResponse")


@_attrs_define
class ModelGetOrderGroupsResponse:
    """
    Attributes:
        order_groups (Union[Unset, list['ModelOrderGroupSummary']]):
    """

    order_groups: Union[Unset, list["ModelOrderGroupSummary"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.order_groups, Unset):
            order_groups = []
            for componentsschemasmodel_order_group_summary_list_item_data in self.order_groups:
                componentsschemasmodel_order_group_summary_list_item = (
                    componentsschemasmodel_order_group_summary_list_item_data.to_dict()
                )
                order_groups.append(componentsschemasmodel_order_group_summary_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_groups is not UNSET:
            field_dict["order_groups"] = order_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_order_group_summary import ModelOrderGroupSummary

        d = dict(src_dict)
        order_groups = []
        _order_groups = d.pop("order_groups", UNSET)
        for componentsschemasmodel_order_group_summary_list_item_data in _order_groups or []:
            componentsschemasmodel_order_group_summary_list_item = ModelOrderGroupSummary.from_dict(
                componentsschemasmodel_order_group_summary_list_item_data
            )

            order_groups.append(componentsschemasmodel_order_group_summary_list_item)

        model_get_order_groups_response = cls(
            order_groups=order_groups,
        )

        model_get_order_groups_response.additional_properties = d
        return model_get_order_groups_response

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
