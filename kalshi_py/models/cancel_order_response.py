from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.order import Order


T = TypeVar("T", bound="CancelOrderResponse")


@_attrs_define
class CancelOrderResponse:
    """
    Attributes:
        order (Order):
        reduced_by (int):
    """

    order: "Order"
    reduced_by: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order = self.order.to_dict()

        reduced_by = self.reduced_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order": order,
                "reduced_by": reduced_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order import Order

        d = dict(src_dict)
        order = Order.from_dict(d.pop("order"))

        reduced_by = d.pop("reduced_by")

        cancel_order_response = cls(
            order=order,
            reduced_by=reduced_by,
        )

        cancel_order_response.additional_properties = d
        return cancel_order_response

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
