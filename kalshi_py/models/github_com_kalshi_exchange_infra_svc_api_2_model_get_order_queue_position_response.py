from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelGetOrderQueuePositionResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelGetOrderQueuePositionResponse:
    """
    Attributes:
        queue_position (Union[Unset, int]): The position of the order in the queue.
    """

    queue_position: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queue_position = self.queue_position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if queue_position is not UNSET:
            field_dict["queue_position"] = queue_position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        queue_position = d.pop("queue_position", UNSET)

        github_com_kalshi_exchange_infra_svc_api_2_model_get_order_queue_position_response = cls(
            queue_position=queue_position,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_get_order_queue_position_response.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_get_order_queue_position_response

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
