from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GenerateApiKeyResponse")


@_attrs_define
class GenerateApiKeyResponse:
    """
    Attributes:
        api_key_id (str): Unique identifier for the newly generated API key
        private_key (str): RSA private key in PEM format. This must be stored securely and cannot be retrieved again
            after this response
    """

    api_key_id: str
    private_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key_id = self.api_key_id

        private_key = self.private_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_key_id": api_key_id,
                "private_key": private_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key_id = d.pop("api_key_id")

        private_key = d.pop("private_key")

        generate_api_key_response = cls(
            api_key_id=api_key_id,
            private_key=private_key,
        )

        generate_api_key_response.additional_properties = d
        return generate_api_key_response

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
