from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelUserCreateApiKeyResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelUserCreateApiKeyResponse:
    """
    Attributes:
        api_key_id (Union[Unset, str]): Unique identifier for the newly created API key.
    """

    api_key_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key_id = self.api_key_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key_id is not UNSET:
            field_dict["api_key_id"] = api_key_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key_id = d.pop("api_key_id", UNSET)

        github_com_kalshi_exchange_infra_svc_api_2_model_user_create_api_key_response = cls(
            api_key_id=api_key_id,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_user_create_api_key_response.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_user_create_api_key_response

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
