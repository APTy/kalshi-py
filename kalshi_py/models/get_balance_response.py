from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetBalanceResponse")


@_attrs_define
class GetBalanceResponse:
    """
    Attributes:
        balance (int): Member's available balance in cents. This represents the amount available for trading.
        portfolio_value (int): Member's portfolio value in cents. This is the current value of all positions held.
        updated_ts (int): Unix timestamp of the last update to the balance.
    """

    balance: int
    portfolio_value: int
    updated_ts: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance = self.balance

        portfolio_value = self.portfolio_value

        updated_ts = self.updated_ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "balance": balance,
                "portfolio_value": portfolio_value,
                "updated_ts": updated_ts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        balance = d.pop("balance")

        portfolio_value = d.pop("portfolio_value")

        updated_ts = d.pop("updated_ts")

        get_balance_response = cls(
            balance=balance,
            portfolio_value=portfolio_value,
            updated_ts=updated_ts,
        )

        get_balance_response.additional_properties = d
        return get_balance_response

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
