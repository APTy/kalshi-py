from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.order_queue_position import OrderQueuePosition


T = TypeVar("T", bound="GetOrderQueuePositionsResponse")


@_attrs_define
class GetOrderQueuePositionsResponse:
    """
    Attributes:
        queue_positions (list['OrderQueuePosition']): Queue positions for all matching orders
    """

    queue_positions: list["OrderQueuePosition"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queue_positions = []
        for queue_positions_item_data in self.queue_positions:
            queue_positions_item = queue_positions_item_data.to_dict()
            queue_positions.append(queue_positions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queue_positions": queue_positions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_queue_position import OrderQueuePosition

        d = dict(src_dict)
        queue_positions = []
        _queue_positions = d.pop("queue_positions")
        for queue_positions_item_data in _queue_positions:
            queue_positions_item = OrderQueuePosition.from_dict(queue_positions_item_data)

            queue_positions.append(queue_positions_item)

        get_order_queue_positions_response = cls(
            queue_positions=queue_positions,
        )

        get_order_queue_positions_response.additional_properties = d
        return get_order_queue_positions_response

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
