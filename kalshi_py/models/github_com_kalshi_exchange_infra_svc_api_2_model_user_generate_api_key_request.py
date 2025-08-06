from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyRequest")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyRequest:
    """
    Attributes:
        name (Union[Unset, str]): Name for the API key. This helps identify the key's purpose.
    """

    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        github_com_kalshi_exchange_infra_svc_api_2_model_user_generate_api_key_request = cls(
            name=name,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_user_generate_api_key_request.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_user_generate_api_key_request

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
