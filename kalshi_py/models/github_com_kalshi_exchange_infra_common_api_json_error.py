from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraCommonApiJSONError")


@_attrs_define
class GithubComKalshiExchangeInfraCommonApiJSONError:
    """
    Attributes:
        code (Union[Unset, str]): A short identifier for the error type.
        details (Union[Unset, str]): Additional details about the error, if available.
        message (Union[Unset, str]): A human-readable description of the error.
        service (Union[Unset, str]): The name of the service that generated the error.
    """

    code: Union[Unset, str] = UNSET
    details: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    service: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        details = self.details

        message = self.message

        service = self.service

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if details is not UNSET:
            field_dict["details"] = details
        if message is not UNSET:
            field_dict["message"] = message
        if service is not UNSET:
            field_dict["service"] = service

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        details = d.pop("details", UNSET)

        message = d.pop("message", UNSET)

        service = d.pop("service", UNSET)

        github_com_kalshi_exchange_infra_common_api_json_error = cls(
            code=code,
            details=details,
            message=message,
            service=service,
        )

        github_com_kalshi_exchange_infra_common_api_json_error.additional_properties = d
        return github_com_kalshi_exchange_infra_common_api_json_error

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
