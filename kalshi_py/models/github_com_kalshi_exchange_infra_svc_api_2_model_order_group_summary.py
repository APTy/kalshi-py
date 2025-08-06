from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelOrderGroupSummary")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelOrderGroupSummary:
    """
    Attributes:
        id (Union[Unset, str]):
        is_auto_cancel_enabled (Union[Unset, bool]): Whether auto-cancel is enabled for this order group.
    """

    id: Union[Unset, str] = UNSET
    is_auto_cancel_enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_auto_cancel_enabled = self.is_auto_cancel_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_auto_cancel_enabled is not UNSET:
            field_dict["is_auto_cancel_enabled"] = is_auto_cancel_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        is_auto_cancel_enabled = d.pop("is_auto_cancel_enabled", UNSET)

        github_com_kalshi_exchange_infra_svc_api_2_model_order_group_summary = cls(
            id=id,
            is_auto_cancel_enabled=is_auto_cancel_enabled,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_order_group_summary.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_order_group_summary

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
