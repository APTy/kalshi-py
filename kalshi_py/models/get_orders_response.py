from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.order import Order


T = TypeVar("T", bound="GetOrdersResponse")


@_attrs_define
class GetOrdersResponse:
    """
    Attributes:
        orders (list['Order']):
        cursor (str):
    """

    orders: list["Order"]
    cursor: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        orders = []
        for orders_item_data in self.orders:
            orders_item = orders_item_data.to_dict()
            orders.append(orders_item)

        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orders": orders,
                "cursor": cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order import Order

        d = dict(src_dict)
        orders = []
        _orders = d.pop("orders")
        for orders_item_data in _orders:
            orders_item = Order.from_dict(orders_item_data)

            orders.append(orders_item)

        cursor = d.pop("cursor")

        get_orders_response = cls(
            orders=orders,
            cursor=cursor,
        )

        get_orders_response.additional_properties = d
        return get_orders_response

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
