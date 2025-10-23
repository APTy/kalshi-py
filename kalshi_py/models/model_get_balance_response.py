from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelGetBalanceResponse")


@_attrs_define
class ModelGetBalanceResponse:
    """
    Attributes:
        balance (Union[Unset, int]):
        portfolio_value (Union[Unset, int]):
        updated_ts (Union[Unset, int]): Timestamp of the last update to the balance.
    """

    balance: Union[Unset, int] = UNSET
    portfolio_value: Union[Unset, int] = UNSET
    updated_ts: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance = self.balance

        portfolio_value = self.portfolio_value

        updated_ts = self.updated_ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if balance is not UNSET:
            field_dict["balance"] = balance
        if portfolio_value is not UNSET:
            field_dict["portfolio_value"] = portfolio_value
        if updated_ts is not UNSET:
            field_dict["updated_ts"] = updated_ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        balance = d.pop("balance", UNSET)

        portfolio_value = d.pop("portfolio_value", UNSET)

        updated_ts = d.pop("updated_ts", UNSET)

        model_get_balance_response = cls(
            balance=balance,
            portfolio_value=portfolio_value,
            updated_ts=updated_ts,
        )

        model_get_balance_response.additional_properties = d
        return model_get_balance_response

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
