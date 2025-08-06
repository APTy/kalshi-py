from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelCreateQuoteRequest")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelCreateQuoteRequest:
    """
    Attributes:
        no_bid (Union[Unset, list[int]]):
        rest_remainder (Union[Unset, bool]): Whether to rest the remainder of the quote after execution.
        rfq_id (Union[Unset, str]):
        yes_bid (Union[Unset, list[int]]):
    """

    no_bid: Union[Unset, list[int]] = UNSET
    rest_remainder: Union[Unset, bool] = UNSET
    rfq_id: Union[Unset, str] = UNSET
    yes_bid: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        no_bid: Union[Unset, list[int]] = UNSET
        if not isinstance(self.no_bid, Unset):
            no_bid = self.no_bid

        rest_remainder = self.rest_remainder

        rfq_id = self.rfq_id

        yes_bid: Union[Unset, list[int]] = UNSET
        if not isinstance(self.yes_bid, Unset):
            yes_bid = self.yes_bid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if no_bid is not UNSET:
            field_dict["no_bid"] = no_bid
        if rest_remainder is not UNSET:
            field_dict["rest_remainder"] = rest_remainder
        if rfq_id is not UNSET:
            field_dict["rfq_id"] = rfq_id
        if yes_bid is not UNSET:
            field_dict["yes_bid"] = yes_bid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        no_bid = cast(list[int], d.pop("no_bid", UNSET))

        rest_remainder = d.pop("rest_remainder", UNSET)

        rfq_id = d.pop("rfq_id", UNSET)

        yes_bid = cast(list[int], d.pop("yes_bid", UNSET))

        github_com_kalshi_exchange_infra_svc_api_2_model_create_quote_request = cls(
            no_bid=no_bid,
            rest_remainder=rest_remainder,
            rfq_id=rfq_id,
            yes_bid=yes_bid,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_create_quote_request.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_create_quote_request

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
