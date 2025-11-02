from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrderQueuePosition")


@_attrs_define
class OrderQueuePosition:
    """
    Attributes:
        order_id (str): The order ID
        market_ticker (str): The market ticker
        queue_position (int): The position of the order in the queue
    """

    order_id: str
    market_ticker: str
    queue_position: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        market_ticker = self.market_ticker

        queue_position = self.queue_position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_id": order_id,
                "market_ticker": market_ticker,
                "queue_position": queue_position,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_id = d.pop("order_id")

        market_ticker = d.pop("market_ticker")

        queue_position = d.pop("queue_position")

        order_queue_position = cls(
            order_id=order_id,
            market_ticker=market_ticker,
            queue_position=queue_position,
        )

        order_queue_position.additional_properties = d
        return order_queue_position

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
