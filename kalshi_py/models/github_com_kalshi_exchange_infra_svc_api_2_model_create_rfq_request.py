from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelCreateRFQRequest")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelCreateRFQRequest:
    """
    Attributes:
        contracts (Union[Unset, int]): The number of contracts for the RFQ.
        market_ticker (Union[Unset, str]): The ticker of the market for which to create an RFQ.
        rest_remainder (Union[Unset, bool]): Whether to rest the remainder of the RFQ after execution.
    """

    contracts: Union[Unset, int] = UNSET
    market_ticker: Union[Unset, str] = UNSET
    rest_remainder: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contracts = self.contracts

        market_ticker = self.market_ticker

        rest_remainder = self.rest_remainder

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contracts is not UNSET:
            field_dict["contracts"] = contracts
        if market_ticker is not UNSET:
            field_dict["market_ticker"] = market_ticker
        if rest_remainder is not UNSET:
            field_dict["rest_remainder"] = rest_remainder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contracts = d.pop("contracts", UNSET)

        market_ticker = d.pop("market_ticker", UNSET)

        rest_remainder = d.pop("rest_remainder", UNSET)

        github_com_kalshi_exchange_infra_svc_api_2_model_create_rfq_request = cls(
            contracts=contracts,
            market_ticker=market_ticker,
            rest_remainder=rest_remainder,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_create_rfq_request.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_create_rfq_request

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
