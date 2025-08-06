from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_amend_order_request_action import (
    GithubComKalshiExchangeInfraSvcApi2ModelAmendOrderRequestAction,
)
from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_amend_order_request_side import (
    GithubComKalshiExchangeInfraSvcApi2ModelAmendOrderRequestSide,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelAmendOrderRequest")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelAmendOrderRequest:
    """
    Attributes:
        action (Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelAmendOrderRequestAction]): Specifies if this is a
            buy or sell order. Cannot be amended and is validated against original order.
        client_order_id (Union[Unset, str]):
        count (Union[Unset, int]): New total number of contracts for the order. This is the desired final count, not a
            delta.
        no_price (Union[Unset, int]):
        no_price_dollars (Union[Unset, list[int]]):
        side (Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelAmendOrderRequestSide]): Side of the order (yes or
            no). Cannot be amended and is validated against original order.
        ticker (Union[Unset, str]): Market ticker. Cannot be amended and is validated against original order.
        updated_client_order_id (Union[Unset, str]):
        yes_price (Union[Unset, int]):
        yes_price_dollars (Union[Unset, list[int]]):
    """

    action: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelAmendOrderRequestAction] = UNSET
    client_order_id: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    no_price: Union[Unset, int] = UNSET
    no_price_dollars: Union[Unset, list[int]] = UNSET
    side: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelAmendOrderRequestSide] = UNSET
    ticker: Union[Unset, str] = UNSET
    updated_client_order_id: Union[Unset, str] = UNSET
    yes_price: Union[Unset, int] = UNSET
    yes_price_dollars: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        client_order_id = self.client_order_id

        count = self.count

        no_price = self.no_price

        no_price_dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.no_price_dollars, Unset):
            no_price_dollars = self.no_price_dollars

        side: Union[Unset, str] = UNSET
        if not isinstance(self.side, Unset):
            side = self.side.value

        ticker = self.ticker

        updated_client_order_id = self.updated_client_order_id

        yes_price = self.yes_price

        yes_price_dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.yes_price_dollars, Unset):
            yes_price_dollars = self.yes_price_dollars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if client_order_id is not UNSET:
            field_dict["client_order_id"] = client_order_id
        if count is not UNSET:
            field_dict["count"] = count
        if no_price is not UNSET:
            field_dict["no_price"] = no_price
        if no_price_dollars is not UNSET:
            field_dict["no_price_dollars"] = no_price_dollars
        if side is not UNSET:
            field_dict["side"] = side
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if updated_client_order_id is not UNSET:
            field_dict["updated_client_order_id"] = updated_client_order_id
        if yes_price is not UNSET:
            field_dict["yes_price"] = yes_price
        if yes_price_dollars is not UNSET:
            field_dict["yes_price_dollars"] = yes_price_dollars

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _action = d.pop("action", UNSET)
        action: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelAmendOrderRequestAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = GithubComKalshiExchangeInfraSvcApi2ModelAmendOrderRequestAction(_action)

        client_order_id = d.pop("client_order_id", UNSET)

        count = d.pop("count", UNSET)

        no_price = d.pop("no_price", UNSET)

        no_price_dollars = cast(list[int], d.pop("no_price_dollars", UNSET))

        _side = d.pop("side", UNSET)
        side: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelAmendOrderRequestSide]
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = GithubComKalshiExchangeInfraSvcApi2ModelAmendOrderRequestSide(_side)

        ticker = d.pop("ticker", UNSET)

        updated_client_order_id = d.pop("updated_client_order_id", UNSET)

        yes_price = d.pop("yes_price", UNSET)

        yes_price_dollars = cast(list[int], d.pop("yes_price_dollars", UNSET))

        github_com_kalshi_exchange_infra_svc_api_2_model_amend_order_request = cls(
            action=action,
            client_order_id=client_order_id,
            count=count,
            no_price=no_price,
            no_price_dollars=no_price_dollars,
            side=side,
            ticker=ticker,
            updated_client_order_id=updated_client_order_id,
            yes_price=yes_price,
            yes_price_dollars=yes_price_dollars,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_amend_order_request.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_amend_order_request

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
