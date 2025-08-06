from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_create_order_request_action import (
    GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestAction,
)
from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_create_order_request_side import (
    GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestSide,
)
from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_create_order_request_time_in_force import (
    GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestTimeInForce,
)
from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_create_order_request_type import (
    GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequest")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequest:
    """
    Attributes:
        action (Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestAction]): Specifies if this is a
            buy or sell order.
        buy_max_cost (Union[Unset, int]):
        client_order_id (Union[Unset, str]):
        count (Union[Unset, int]): Number of contracts to be bought or sold.
        expiration_ts (Union[Unset, int]): Expiration time of the order, in unix seconds. If not supplied, the order
            won't expire until explicitly cancelled (GTC). If the time is in the past, the order will attempt to fill and
            cancel any remainder (IOC). If the time is in the future, the unfilled quantity will expire at the specified
            time.
        no_price (Union[Unset, int]):
        no_price_dollars (Union[Unset, list[int]]):
        order_group_id (Union[Unset, str]):
        post_only (Union[Unset, bool]): If this flag is set to true, an order will be rejected if it crosses the spread
            and executes.
        self_trade_prevention_type (Union[Unset, str]):
        sell_position_capped (Union[Unset, bool]): SellPositionCapped prevents sell orders from exceeding your current
            position. This option can only be used with Immediate-or-Cancel (IoC) orders.
        sell_position_floor (Union[Unset, int]): SellPositionFloor will not let you flip position for a market order if
            set to 0. Deprecated: Use sell_position_capped instead.
        side (Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestSide]): Specifies if this is a
            'yes' or 'no' order.
        ticker (Union[Unset, str]): The ticker of the market the order will be placed in.
        time_in_force (Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestTimeInForce]): Currently
            only 'fill_or_kill' and 'immediate_or_cancel' are supported. Other time in forces are controlled through
            expiration_ts.
        type_ (Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestType]): Specifies if this is a
            'market' or a 'limit' order. Note that either the Yes Price or the No Price must be provided for limit orders.
        yes_price (Union[Unset, int]):
        yes_price_dollars (Union[Unset, list[int]]):
    """

    action: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestAction] = UNSET
    buy_max_cost: Union[Unset, int] = UNSET
    client_order_id: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    expiration_ts: Union[Unset, int] = UNSET
    no_price: Union[Unset, int] = UNSET
    no_price_dollars: Union[Unset, list[int]] = UNSET
    order_group_id: Union[Unset, str] = UNSET
    post_only: Union[Unset, bool] = UNSET
    self_trade_prevention_type: Union[Unset, str] = UNSET
    sell_position_capped: Union[Unset, bool] = UNSET
    sell_position_floor: Union[Unset, int] = UNSET
    side: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestSide] = UNSET
    ticker: Union[Unset, str] = UNSET
    time_in_force: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestTimeInForce] = UNSET
    type_: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestType] = UNSET
    yes_price: Union[Unset, int] = UNSET
    yes_price_dollars: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        buy_max_cost = self.buy_max_cost

        client_order_id = self.client_order_id

        count = self.count

        expiration_ts = self.expiration_ts

        no_price = self.no_price

        no_price_dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.no_price_dollars, Unset):
            no_price_dollars = self.no_price_dollars

        order_group_id = self.order_group_id

        post_only = self.post_only

        self_trade_prevention_type = self.self_trade_prevention_type

        sell_position_capped = self.sell_position_capped

        sell_position_floor = self.sell_position_floor

        side: Union[Unset, str] = UNSET
        if not isinstance(self.side, Unset):
            side = self.side.value

        ticker = self.ticker

        time_in_force: Union[Unset, str] = UNSET
        if not isinstance(self.time_in_force, Unset):
            time_in_force = self.time_in_force.value

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        yes_price = self.yes_price

        yes_price_dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.yes_price_dollars, Unset):
            yes_price_dollars = self.yes_price_dollars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if buy_max_cost is not UNSET:
            field_dict["buy_max_cost"] = buy_max_cost
        if client_order_id is not UNSET:
            field_dict["client_order_id"] = client_order_id
        if count is not UNSET:
            field_dict["count"] = count
        if expiration_ts is not UNSET:
            field_dict["expiration_ts"] = expiration_ts
        if no_price is not UNSET:
            field_dict["no_price"] = no_price
        if no_price_dollars is not UNSET:
            field_dict["no_price_dollars"] = no_price_dollars
        if order_group_id is not UNSET:
            field_dict["order_group_id"] = order_group_id
        if post_only is not UNSET:
            field_dict["post_only"] = post_only
        if self_trade_prevention_type is not UNSET:
            field_dict["self_trade_prevention_type"] = self_trade_prevention_type
        if sell_position_capped is not UNSET:
            field_dict["sell_position_capped"] = sell_position_capped
        if sell_position_floor is not UNSET:
            field_dict["sell_position_floor"] = sell_position_floor
        if side is not UNSET:
            field_dict["side"] = side
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if time_in_force is not UNSET:
            field_dict["time_in_force"] = time_in_force
        if type_ is not UNSET:
            field_dict["type"] = type_
        if yes_price is not UNSET:
            field_dict["yes_price"] = yes_price
        if yes_price_dollars is not UNSET:
            field_dict["yes_price_dollars"] = yes_price_dollars

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _action = d.pop("action", UNSET)
        action: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestAction(_action)

        buy_max_cost = d.pop("buy_max_cost", UNSET)

        client_order_id = d.pop("client_order_id", UNSET)

        count = d.pop("count", UNSET)

        expiration_ts = d.pop("expiration_ts", UNSET)

        no_price = d.pop("no_price", UNSET)

        no_price_dollars = cast(list[int], d.pop("no_price_dollars", UNSET))

        order_group_id = d.pop("order_group_id", UNSET)

        post_only = d.pop("post_only", UNSET)

        self_trade_prevention_type = d.pop("self_trade_prevention_type", UNSET)

        sell_position_capped = d.pop("sell_position_capped", UNSET)

        sell_position_floor = d.pop("sell_position_floor", UNSET)

        _side = d.pop("side", UNSET)
        side: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestSide]
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestSide(_side)

        ticker = d.pop("ticker", UNSET)

        _time_in_force = d.pop("time_in_force", UNSET)
        time_in_force: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestTimeInForce]
        if isinstance(_time_in_force, Unset):
            time_in_force = UNSET
        else:
            time_in_force = GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestTimeInForce(_time_in_force)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequestType(_type_)

        yes_price = d.pop("yes_price", UNSET)

        yes_price_dollars = cast(list[int], d.pop("yes_price_dollars", UNSET))

        github_com_kalshi_exchange_infra_svc_api_2_model_create_order_request = cls(
            action=action,
            buy_max_cost=buy_max_cost,
            client_order_id=client_order_id,
            count=count,
            expiration_ts=expiration_ts,
            no_price=no_price,
            no_price_dollars=no_price_dollars,
            order_group_id=order_group_id,
            post_only=post_only,
            self_trade_prevention_type=self_trade_prevention_type,
            sell_position_capped=sell_position_capped,
            sell_position_floor=sell_position_floor,
            side=side,
            ticker=ticker,
            time_in_force=time_in_force,
            type_=type_,
            yes_price=yes_price,
            yes_price_dollars=yes_price_dollars,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_create_order_request.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_create_order_request

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
