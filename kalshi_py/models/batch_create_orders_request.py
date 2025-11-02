from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_order_request import CreateOrderRequest


T = TypeVar("T", bound="BatchCreateOrdersRequest")


@_attrs_define
class BatchCreateOrdersRequest:
    """
    Attributes:
        orders (list['CreateOrderRequest']):
    """

    orders: list["CreateOrderRequest"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        orders = []
        for orders_item_data in self.orders:
            orders_item = orders_item_data.to_dict()
            orders.append(orders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orders": orders,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_order_request import CreateOrderRequest

        d = dict(src_dict)
        orders = []
        _orders = d.pop("orders")
        for orders_item_data in _orders:
            orders_item = CreateOrderRequest.from_dict(orders_item_data)

            orders.append(orders_item)

        batch_create_orders_request = cls(
            orders=orders,
        )

        batch_create_orders_request.additional_properties = d
        return batch_create_orders_request

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
