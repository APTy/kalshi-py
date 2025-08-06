from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_common_api_json_error import (
        GithubComKalshiExchangeInfraCommonApiJSONError,
    )
    from ..models.model_order_confirmation import ModelOrderConfirmation


T = TypeVar("T", bound="ModelBatchCreateOrdersResponseOrdersItem")


@_attrs_define
class ModelBatchCreateOrdersResponseOrdersItem:
    """
    Attributes:
        client_order_id (Union[Unset, str]):
        error (Union[Unset, GithubComKalshiExchangeInfraCommonApiJSONError]):
        order (Union[Unset, ModelOrderConfirmation]):
    """

    client_order_id: Union[Unset, str] = UNSET
    error: Union[Unset, "GithubComKalshiExchangeInfraCommonApiJSONError"] = UNSET
    order: Union[Unset, "ModelOrderConfirmation"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_order_id = self.client_order_id

        error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        order: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_order_id is not UNSET:
            field_dict["client_order_id"] = client_order_id
        if error is not UNSET:
            field_dict["error"] = error
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_common_api_json_error import (
            GithubComKalshiExchangeInfraCommonApiJSONError,
        )
        from ..models.model_order_confirmation import ModelOrderConfirmation

        d = dict(src_dict)
        client_order_id = d.pop("client_order_id", UNSET)

        _error = d.pop("error", UNSET)
        error: Union[Unset, GithubComKalshiExchangeInfraCommonApiJSONError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = GithubComKalshiExchangeInfraCommonApiJSONError.from_dict(_error)

        _order = d.pop("order", UNSET)
        order: Union[Unset, ModelOrderConfirmation]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = ModelOrderConfirmation.from_dict(_order)

        model_batch_create_orders_response_orders_item = cls(
            client_order_id=client_order_id,
            error=error,
            order=order,
        )

        model_batch_create_orders_response_orders_item.additional_properties = d
        return model_batch_create_orders_response_orders_item

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
