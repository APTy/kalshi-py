from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.svc_api_2_model_order_book import SvcApi2ModelOrderBook


T = TypeVar("T", bound="SvcApi2ModelGetMarketOrderbookResponse")


@_attrs_define
class SvcApi2ModelGetMarketOrderbookResponse:
    """
    Attributes:
        orderbook (Union[Unset, SvcApi2ModelOrderBook]):
    """

    orderbook: Union[Unset, "SvcApi2ModelOrderBook"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        orderbook: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.orderbook, Unset):
            orderbook = self.orderbook.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if orderbook is not UNSET:
            field_dict["orderbook"] = orderbook

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.svc_api_2_model_order_book import SvcApi2ModelOrderBook

        d = dict(src_dict)
        _orderbook = d.pop("orderbook", UNSET)
        orderbook: Union[Unset, SvcApi2ModelOrderBook]
        if isinstance(_orderbook, Unset):
            orderbook = UNSET
        else:
            orderbook = SvcApi2ModelOrderBook.from_dict(_orderbook)

        svc_api_2_model_get_market_orderbook_response = cls(
            orderbook=orderbook,
        )

        svc_api_2_model_get_market_orderbook_response.additional_properties = d
        return svc_api_2_model_get_market_orderbook_response

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
