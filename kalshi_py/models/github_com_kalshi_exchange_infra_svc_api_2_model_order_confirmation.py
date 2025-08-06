from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelOrderConfirmation")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelOrderConfirmation:
    """
    Attributes:
        action (Union[Unset, str]):
        client_order_id (Union[Unset, str]):
        created_time (Union[Unset, Any]):
        expiration_time (Union[Unset, Any]):
        no_price (Union[Unset, int]):
        no_price_dollars (Union[Unset, list[int]]):
        order_group_id (Union[Unset, str]):
        order_id (Union[Unset, str]): Unique identifier for orders.
        self_trade_prevention_type (Union[Unset, str]):
        side (Union[Unset, str]):
        status (Union[Unset, str]):
        ticker (Union[Unset, str]): Unique identifier for markets.
        type_ (Union[Unset, str]):
        user_id (Union[Unset, str]): Unique identifier for users.
        yes_price (Union[Unset, int]):
        yes_price_dollars (Union[Unset, list[int]]):
    """

    action: Union[Unset, str] = UNSET
    client_order_id: Union[Unset, str] = UNSET
    created_time: Union[Unset, Any] = UNSET
    expiration_time: Union[Unset, Any] = UNSET
    no_price: Union[Unset, int] = UNSET
    no_price_dollars: Union[Unset, list[int]] = UNSET
    order_group_id: Union[Unset, str] = UNSET
    order_id: Union[Unset, str] = UNSET
    self_trade_prevention_type: Union[Unset, str] = UNSET
    side: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    ticker: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    yes_price: Union[Unset, int] = UNSET
    yes_price_dollars: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        client_order_id = self.client_order_id

        created_time = self.created_time

        expiration_time = self.expiration_time

        no_price = self.no_price

        no_price_dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.no_price_dollars, Unset):
            no_price_dollars = self.no_price_dollars

        order_group_id = self.order_group_id

        order_id = self.order_id

        self_trade_prevention_type = self.self_trade_prevention_type

        side = self.side

        status = self.status

        ticker = self.ticker

        type_ = self.type_

        user_id = self.user_id

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
        if created_time is not UNSET:
            field_dict["created_time"] = created_time
        if expiration_time is not UNSET:
            field_dict["expiration_time"] = expiration_time
        if no_price is not UNSET:
            field_dict["no_price"] = no_price
        if no_price_dollars is not UNSET:
            field_dict["no_price_dollars"] = no_price_dollars
        if order_group_id is not UNSET:
            field_dict["order_group_id"] = order_group_id
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if self_trade_prevention_type is not UNSET:
            field_dict["self_trade_prevention_type"] = self_trade_prevention_type
        if side is not UNSET:
            field_dict["side"] = side
        if status is not UNSET:
            field_dict["status"] = status
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if type_ is not UNSET:
            field_dict["type"] = type_
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if yes_price is not UNSET:
            field_dict["yes_price"] = yes_price
        if yes_price_dollars is not UNSET:
            field_dict["yes_price_dollars"] = yes_price_dollars

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        client_order_id = d.pop("client_order_id", UNSET)

        created_time = d.pop("created_time", UNSET)

        expiration_time = d.pop("expiration_time", UNSET)

        no_price = d.pop("no_price", UNSET)

        no_price_dollars = cast(list[int], d.pop("no_price_dollars", UNSET))

        order_group_id = d.pop("order_group_id", UNSET)

        order_id = d.pop("order_id", UNSET)

        self_trade_prevention_type = d.pop("self_trade_prevention_type", UNSET)

        side = d.pop("side", UNSET)

        status = d.pop("status", UNSET)

        ticker = d.pop("ticker", UNSET)

        type_ = d.pop("type", UNSET)

        user_id = d.pop("user_id", UNSET)

        yes_price = d.pop("yes_price", UNSET)

        yes_price_dollars = cast(list[int], d.pop("yes_price_dollars", UNSET))

        github_com_kalshi_exchange_infra_svc_api_2_model_order_confirmation = cls(
            action=action,
            client_order_id=client_order_id,
            created_time=created_time,
            expiration_time=expiration_time,
            no_price=no_price,
            no_price_dollars=no_price_dollars,
            order_group_id=order_group_id,
            order_id=order_id,
            self_trade_prevention_type=self_trade_prevention_type,
            side=side,
            status=status,
            ticker=ticker,
            type_=type_,
            user_id=user_id,
            yes_price=yes_price,
            yes_price_dollars=yes_price_dollars,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_order_confirmation.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_order_confirmation

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
