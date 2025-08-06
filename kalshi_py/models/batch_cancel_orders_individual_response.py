from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_common_api_json_error import (
        GithubComKalshiExchangeInfraCommonApiJSONError,
    )
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_order import (
        GithubComKalshiExchangeInfraSvcApi2ModelOrder,
    )


T = TypeVar("T", bound="BatchCancelOrdersIndividualResponse")


@_attrs_define
class BatchCancelOrdersIndividualResponse:
    """
    Attributes:
        error (Union[Unset, GithubComKalshiExchangeInfraCommonApiJSONError]):
        order (Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelOrder]):
        order_id (Union[Unset, str]):
        reduced_by (Union[Unset, int]): The number of contracts that were successfully canceled from this order.
    """

    error: Union[Unset, "GithubComKalshiExchangeInfraCommonApiJSONError"] = UNSET
    order: Union[Unset, "GithubComKalshiExchangeInfraSvcApi2ModelOrder"] = UNSET
    order_id: Union[Unset, str] = UNSET
    reduced_by: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        order: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        order_id = self.order_id

        reduced_by = self.reduced_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if order is not UNSET:
            field_dict["order"] = order
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if reduced_by is not UNSET:
            field_dict["reduced_by"] = reduced_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_common_api_json_error import (
            GithubComKalshiExchangeInfraCommonApiJSONError,
        )
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_order import (
            GithubComKalshiExchangeInfraSvcApi2ModelOrder,
        )

        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: Union[Unset, GithubComKalshiExchangeInfraCommonApiJSONError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = GithubComKalshiExchangeInfraCommonApiJSONError.from_dict(_error)

        _order = d.pop("order", UNSET)
        order: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = GithubComKalshiExchangeInfraSvcApi2ModelOrder.from_dict(_order)

        order_id = d.pop("order_id", UNSET)

        reduced_by = d.pop("reduced_by", UNSET)

        batch_cancel_orders_individual_response = cls(
            error=error,
            order=order,
            order_id=order_id,
            reduced_by=reduced_by,
        )

        batch_cancel_orders_individual_response.additional_properties = d
        return batch_cancel_orders_individual_response

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
