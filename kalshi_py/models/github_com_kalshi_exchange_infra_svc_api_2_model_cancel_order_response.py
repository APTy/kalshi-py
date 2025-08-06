from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_order import (
        GithubComKalshiExchangeInfraSvcApi2ModelOrder,
    )


T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelCancelOrderResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelCancelOrderResponse:
    """
    Attributes:
        order (Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelOrder]):
        reduced_by (Union[Unset, int]): How much the count of the order was reduced by because of this operation.
    """

    order: Union[Unset, "GithubComKalshiExchangeInfraSvcApi2ModelOrder"] = UNSET
    reduced_by: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        reduced_by = self.reduced_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order is not UNSET:
            field_dict["order"] = order
        if reduced_by is not UNSET:
            field_dict["reduced_by"] = reduced_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_order import (
            GithubComKalshiExchangeInfraSvcApi2ModelOrder,
        )

        d = dict(src_dict)
        _order = d.pop("order", UNSET)
        order: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = GithubComKalshiExchangeInfraSvcApi2ModelOrder.from_dict(_order)

        reduced_by = d.pop("reduced_by", UNSET)

        github_com_kalshi_exchange_infra_svc_api_2_model_cancel_order_response = cls(
            order=order,
            reduced_by=reduced_by,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_cancel_order_response.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_cancel_order_response

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
