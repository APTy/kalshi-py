from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupRequest")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupRequest:
    """
    Attributes:
        contracts_limit (Union[Unset, int]): Specifies the maximum number of contracts that can be matched within this
            group.
    """

    contracts_limit: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contracts_limit = self.contracts_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contracts_limit is not UNSET:
            field_dict["contracts_limit"] = contracts_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contracts_limit = d.pop("contracts_limit", UNSET)

        github_com_kalshi_exchange_infra_svc_api_2_model_create_order_group_request = cls(
            contracts_limit=contracts_limit,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_create_order_group_request.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_create_order_group_request

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
