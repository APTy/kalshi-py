from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelDecreaseOrderRequest")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelDecreaseOrderRequest:
    """
    Attributes:
        reduce_by (Union[Unset, int]): Number of contracts to decrease the order's count by. One of reduce_by or
            reduce_to must be provided.
        reduce_to (Union[Unset, int]): Number of contracts to decrease the order to. If the orders remaining count is
            lower, it does nothing. One of reduce_by or reduce_to must be provided.
    """

    reduce_by: Union[Unset, int] = UNSET
    reduce_to: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reduce_by = self.reduce_by

        reduce_to = self.reduce_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reduce_by is not UNSET:
            field_dict["reduce_by"] = reduce_by
        if reduce_to is not UNSET:
            field_dict["reduce_to"] = reduce_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reduce_by = d.pop("reduce_by", UNSET)

        reduce_to = d.pop("reduce_to", UNSET)

        github_com_kalshi_exchange_infra_svc_api_2_model_decrease_order_request = cls(
            reduce_by=reduce_by,
            reduce_to=reduce_to,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_decrease_order_request.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_decrease_order_request

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
