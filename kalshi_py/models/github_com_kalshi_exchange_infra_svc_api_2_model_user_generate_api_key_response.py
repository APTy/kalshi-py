from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyResponse:
    """
    Attributes:
        api_key_id (Union[Unset, str]): Unique identifier for the newly generated API key.
        private_key (Union[Unset, str]): RSA private key in PEM format. This must be stored securely and cannot be
            retrieved again after this response.
    """

    api_key_id: Union[Unset, str] = UNSET
    private_key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key_id = self.api_key_id

        private_key = self.private_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key_id is not UNSET:
            field_dict["api_key_id"] = api_key_id
        if private_key is not UNSET:
            field_dict["private_key"] = private_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key_id = d.pop("api_key_id", UNSET)

        private_key = d.pop("private_key", UNSET)

        github_com_kalshi_exchange_infra_svc_api_2_model_user_generate_api_key_response = cls(
            api_key_id=api_key_id,
            private_key=private_key,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_user_generate_api_key_response.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_user_generate_api_key_response

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
