from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_common_api_json_error import (
        GithubComKalshiExchangeInfraCommonApiJSONError,
    )
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_order_confirmation import (
        GithubComKalshiExchangeInfraSvcApi2ModelOrderConfirmation,
    )


T = TypeVar("T", bound="BatchCreateOrdersIndividualResponse")


@_attrs_define
class BatchCreateOrdersIndividualResponse:
    """
    Attributes:
        client_order_id (Union[Unset, str]):
        error (Union[Unset, GithubComKalshiExchangeInfraCommonApiJSONError]):
        order (Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelOrderConfirmation]):
    """

    client_order_id: Union[Unset, str] = UNSET
    error: Union[Unset, "GithubComKalshiExchangeInfraCommonApiJSONError"] = UNSET
    order: Union[Unset, "GithubComKalshiExchangeInfraSvcApi2ModelOrderConfirmation"] = UNSET
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
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_order_confirmation import (
            GithubComKalshiExchangeInfraSvcApi2ModelOrderConfirmation,
        )

        d = dict(src_dict)
        client_order_id = d.pop("client_order_id", UNSET)

        _error = d.pop("error", UNSET)
        error: Union[Unset, GithubComKalshiExchangeInfraCommonApiJSONError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = GithubComKalshiExchangeInfraCommonApiJSONError.from_dict(_error)

        _order = d.pop("order", UNSET)
        order: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelOrderConfirmation]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = GithubComKalshiExchangeInfraSvcApi2ModelOrderConfirmation.from_dict(_order)

        batch_create_orders_individual_response = cls(
            client_order_id=client_order_id,
            error=error,
            order=order,
        )

        batch_create_orders_individual_response.additional_properties = d
        return batch_create_orders_individual_response

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
