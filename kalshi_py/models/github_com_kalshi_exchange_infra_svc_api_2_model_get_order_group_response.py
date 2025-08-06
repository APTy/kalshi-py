from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelGetOrderGroupResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelGetOrderGroupResponse:
    """
    Attributes:
        is_auto_cancel_enabled (Union[Unset, bool]): Whether auto-cancel is enabled for this order group.
        orders (Union[Unset, list[str]]): List of order IDs that belong to this order group.
    """

    is_auto_cancel_enabled: Union[Unset, bool] = UNSET
    orders: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_auto_cancel_enabled = self.is_auto_cancel_enabled

        orders: Union[Unset, list[str]] = UNSET
        if not isinstance(self.orders, Unset):
            orders = self.orders

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_auto_cancel_enabled is not UNSET:
            field_dict["is_auto_cancel_enabled"] = is_auto_cancel_enabled
        if orders is not UNSET:
            field_dict["orders"] = orders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_auto_cancel_enabled = d.pop("is_auto_cancel_enabled", UNSET)

        orders = cast(list[str], d.pop("orders", UNSET))

        github_com_kalshi_exchange_infra_svc_api_2_model_get_order_group_response = cls(
            is_auto_cancel_enabled=is_auto_cancel_enabled,
            orders=orders,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_get_order_group_response.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_get_order_group_response

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
