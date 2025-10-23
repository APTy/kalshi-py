from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_create_order_request_action import ModelCreateOrderRequestAction
from ..models.model_create_order_request_side import ModelCreateOrderRequestSide
from ..models.model_create_order_request_time_in_force import ModelCreateOrderRequestTimeInForce
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelCreateOrderRequest")


@_attrs_define
class ModelCreateOrderRequest:
    """
    Attributes:
        action (Union[Unset, ModelCreateOrderRequestAction]): Specifies if this is a buy or sell order.
        buy_max_cost (Union[Unset, int]):
        cancel_order_on_pause (Union[Unset, bool]): If this flag is set to true, the order will be canceled if the order
            is open and trading on the exchange is paused for any reason.
        client_order_id (Union[Unset, str]):
        count (Union[Unset, int]): Number of contracts to be bought or sold.
        expiration_ts (Union[Unset, int]): Expiration time of the order, in unix seconds. If not supplied, the order
            won't expire until explicitly cancelled (GTC). If the time is in the past, the order will attempt to fill and
            cancel any remainder (IOC). If the time is in the future, the unfilled quantity will expire at the specified
            time.
        no_price (Union[Unset, int]):
        no_price_dollars (Union[Unset, str]): Fixed point representation of a subpenny dollar amount e.g. 1.2345
            indicates $1.23 and 45/100 of a cent. Example: 0.2300.
        order_group_id (Union[Unset, str]):
        post_only (Union[Unset, bool]): If this flag is set to true, an order will be rejected if it crosses the spread
            and executes.
        self_trade_prevention_type (Union[Unset, str]):
        sell_position_capped (Union[Unset, bool]): SellPositionCapped prevents sell orders from exceeding your current
            position. This option can only be used with Immediate-or-Cancel (IoC) orders.
        sell_position_floor (Union[Unset, int]): SellPositionFloor will not let you flip position for a market order if
            set to 0. Deprecated: Use sell_position_capped instead.
        side (Union[Unset, ModelCreateOrderRequestSide]): Specifies if this is a 'yes' or 'no' order.
        ticker (Union[Unset, str]): The ticker of the market the order will be placed in.
        time_in_force (Union[Unset, ModelCreateOrderRequestTimeInForce]): Currently only 'fill_or_kill' and
            'immediate_or_cancel' are supported. When not specified, defaults to GTC (Good Till Canceled) if no
            expiration_ts is provided, or GTT (Good Till Time) if expiration_ts is provided.
        yes_price (Union[Unset, int]):
        yes_price_dollars (Union[Unset, str]): Fixed point representation of a subpenny dollar amount e.g. 1.2345
            indicates $1.23 and 45/100 of a cent. Example: 0.2300.
    """

    action: Union[Unset, ModelCreateOrderRequestAction] = UNSET
    buy_max_cost: Union[Unset, int] = UNSET
    cancel_order_on_pause: Union[Unset, bool] = UNSET
    client_order_id: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    expiration_ts: Union[Unset, int] = UNSET
    no_price: Union[Unset, int] = UNSET
    no_price_dollars: Union[Unset, str] = UNSET
    order_group_id: Union[Unset, str] = UNSET
    post_only: Union[Unset, bool] = UNSET
    self_trade_prevention_type: Union[Unset, str] = UNSET
    sell_position_capped: Union[Unset, bool] = UNSET
    sell_position_floor: Union[Unset, int] = UNSET
    side: Union[Unset, ModelCreateOrderRequestSide] = UNSET
    ticker: Union[Unset, str] = UNSET
    time_in_force: Union[Unset, ModelCreateOrderRequestTimeInForce] = UNSET
    yes_price: Union[Unset, int] = UNSET
    yes_price_dollars: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        buy_max_cost = self.buy_max_cost

        cancel_order_on_pause = self.cancel_order_on_pause

        client_order_id = self.client_order_id

        count = self.count

        expiration_ts = self.expiration_ts

        no_price = self.no_price

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

        yes_price = self.yes_price

        yes_price_dollars = self.yes_price_dollars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if buy_max_cost is not UNSET:
            field_dict["buy_max_cost"] = buy_max_cost
        if cancel_order_on_pause is not UNSET:
            field_dict["cancel_order_on_pause"] = cancel_order_on_pause
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
        if yes_price is not UNSET:
            field_dict["yes_price"] = yes_price
        if yes_price_dollars is not UNSET:
            field_dict["yes_price_dollars"] = yes_price_dollars

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _action = d.pop("action", UNSET)
        action: Union[Unset, ModelCreateOrderRequestAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = ModelCreateOrderRequestAction(_action)

        buy_max_cost = d.pop("buy_max_cost", UNSET)

        cancel_order_on_pause = d.pop("cancel_order_on_pause", UNSET)

        client_order_id = d.pop("client_order_id", UNSET)

        count = d.pop("count", UNSET)

        expiration_ts = d.pop("expiration_ts", UNSET)

        no_price = d.pop("no_price", UNSET)

        no_price_dollars = d.pop("no_price_dollars", UNSET)

        order_group_id = d.pop("order_group_id", UNSET)

        post_only = d.pop("post_only", UNSET)

        self_trade_prevention_type = d.pop("self_trade_prevention_type", UNSET)

        sell_position_capped = d.pop("sell_position_capped", UNSET)

        sell_position_floor = d.pop("sell_position_floor", UNSET)

        _side = d.pop("side", UNSET)
        side: Union[Unset, ModelCreateOrderRequestSide]
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = ModelCreateOrderRequestSide(_side)

        ticker = d.pop("ticker", UNSET)

        _time_in_force = d.pop("time_in_force", UNSET)
        time_in_force: Union[Unset, ModelCreateOrderRequestTimeInForce]
        if isinstance(_time_in_force, Unset):
            time_in_force = UNSET
        else:
            time_in_force = ModelCreateOrderRequestTimeInForce(_time_in_force)

        yes_price = d.pop("yes_price", UNSET)

        yes_price_dollars = d.pop("yes_price_dollars", UNSET)

        model_create_order_request = cls(
            action=action,
            buy_max_cost=buy_max_cost,
            cancel_order_on_pause=cancel_order_on_pause,
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
            yes_price=yes_price,
            yes_price_dollars=yes_price_dollars,
        )

        model_create_order_request.additional_properties = d
        return model_create_order_request

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
