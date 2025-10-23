from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_common_api_json_error import (
        GithubComKalshiExchangeInfraCommonApiJSONError,
    )


T = TypeVar("T", bound="ControllersWebcontrollerErrorResponse")


@_attrs_define
class ControllersWebcontrollerErrorResponse:
    """
    Attributes:
        error (Union[Unset, GithubComKalshiExchangeInfraCommonApiJSONError]):
    """

    error: Union[Unset, "GithubComKalshiExchangeInfraCommonApiJSONError"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_common_api_json_error import (
            GithubComKalshiExchangeInfraCommonApiJSONError,
        )

        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: Union[Unset, GithubComKalshiExchangeInfraCommonApiJSONError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = GithubComKalshiExchangeInfraCommonApiJSONError.from_dict(_error)

        controllers_webcontroller_error_response = cls(
            error=error,
        )

        controllers_webcontroller_error_response.additional_properties = d
        return controllers_webcontroller_error_response

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
