from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_accept_quote_request_accepted_side import (
    GithubComKalshiExchangeInfraSvcApi2ModelAcceptQuoteRequestAcceptedSide,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelAcceptQuoteRequest")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelAcceptQuoteRequest:
    """
    Attributes:
        accepted_side (Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelAcceptQuoteRequestAcceptedSide]): The side
            of the quote to accept (yes or no).
    """

    accepted_side: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelAcceptQuoteRequestAcceptedSide] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepted_side: Union[Unset, str] = UNSET
        if not isinstance(self.accepted_side, Unset):
            accepted_side = self.accepted_side.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accepted_side is not UNSET:
            field_dict["accepted_side"] = accepted_side

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _accepted_side = d.pop("accepted_side", UNSET)
        accepted_side: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelAcceptQuoteRequestAcceptedSide]
        if isinstance(_accepted_side, Unset):
            accepted_side = UNSET
        else:
            accepted_side = GithubComKalshiExchangeInfraSvcApi2ModelAcceptQuoteRequestAcceptedSide(_accepted_side)

        github_com_kalshi_exchange_infra_svc_api_2_model_accept_quote_request = cls(
            accepted_side=accepted_side,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_accept_quote_request.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_accept_quote_request

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
