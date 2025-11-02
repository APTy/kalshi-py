from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetPortfolioRestingOrderTotalValueResponse")


@_attrs_define
class GetPortfolioRestingOrderTotalValueResponse:
    """
    Attributes:
        total_resting_order_value (int): Total value of resting orders in cents
    """

    total_resting_order_value: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_resting_order_value = self.total_resting_order_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_resting_order_value": total_resting_order_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_resting_order_value = d.pop("total_resting_order_value")

        get_portfolio_resting_order_total_value_response = cls(
            total_resting_order_value=total_resting_order_value,
        )

        get_portfolio_resting_order_total_value_response.additional_properties = d
        return get_portfolio_resting_order_total_value_response

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
