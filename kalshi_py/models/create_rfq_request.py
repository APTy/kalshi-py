from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateRFQRequest")


@_attrs_define
class CreateRFQRequest:
    """
    Attributes:
        market_ticker (str): The ticker of the market for which to create an RFQ
        rest_remainder (bool): Whether to rest the remainder of the RFQ after execution
        contracts (Union[Unset, int]): The number of contracts for the RFQ
        target_cost_centi_cents (Union[Unset, int]): The target cost for the RFQ in centi-cents
    """

    market_ticker: str
    rest_remainder: bool
    contracts: Union[Unset, int] = UNSET
    target_cost_centi_cents: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        market_ticker = self.market_ticker

        rest_remainder = self.rest_remainder

        contracts = self.contracts

        target_cost_centi_cents = self.target_cost_centi_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "market_ticker": market_ticker,
                "rest_remainder": rest_remainder,
            }
        )
        if contracts is not UNSET:
            field_dict["contracts"] = contracts
        if target_cost_centi_cents is not UNSET:
            field_dict["target_cost_centi_cents"] = target_cost_centi_cents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        market_ticker = d.pop("market_ticker")

        rest_remainder = d.pop("rest_remainder")

        contracts = d.pop("contracts", UNSET)

        target_cost_centi_cents = d.pop("target_cost_centi_cents", UNSET)

        create_rfq_request = cls(
            market_ticker=market_ticker,
            rest_remainder=rest_remainder,
            contracts=contracts,
            target_cost_centi_cents=target_cost_centi_cents,
        )

        create_rfq_request.additional_properties = d
        return create_rfq_request

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
