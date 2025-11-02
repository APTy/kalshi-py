import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.order_action import OrderAction
from ..models.order_self_trade_prevention_type import OrderSelfTradePreventionType
from ..models.order_side import OrderSide
from ..models.order_status import OrderStatus
from ..models.order_type import OrderType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Order")


@_attrs_define
class Order:
    """
    Attributes:
        order_id (str):
        user_id (str): Unique identifier for users
        client_order_id (str):
        ticker (str):
        side (OrderSide):
        action (OrderAction):
        type_ (OrderType):
        status (OrderStatus):
        yes_price (float):
        no_price (float):
        yes_price_dollars (str): The yes price for this order in fixed-point dollars Example: 0.5000.
        no_price_dollars (str): The no price for this order in fixed-point dollars Example: 0.5000.
        fill_count (int): The number of contracts that have been filled
        remaining_count (int):
        initial_count (int): The initial size of the order (contract units)
        taker_fees (int): Fees paid on filled taker contracts, in cents
        maker_fees (int): Fees paid on filled maker contracts, in cents
        taker_fill_cost (int): The cost of filled taker orders in cents
        maker_fill_cost (int): The cost of filled maker orders in cents
        taker_fill_cost_dollars (str): The cost of filled taker orders in dollars
        maker_fill_cost_dollars (str): The cost of filled maker orders in dollars
        queue_position (int): **DEPRECATED**: This field is deprecated and will always return 0. Please use the GET
            /portfolio/orders/{order_id}/queue_position endpoint instead
        taker_fees_dollars (Union[None, Unset, str]): Fees paid on filled taker contracts, in dollars
        maker_fees_dollars (Union[None, Unset, str]): Fees paid on filled maker contracts, in dollars
        expiration_time (Union[None, Unset, datetime.datetime]):
        created_time (Union[None, Unset, datetime.datetime]):
        last_update_time (Union[None, Unset, datetime.datetime]): The last update to an order (modify, cancel, fill)
        self_trade_prevention_type (Union[Unset, OrderSelfTradePreventionType]): The self-trade prevention type for this
            order
        order_group_id (Union[None, UUID, Unset]): The order group this order is part of
        cancel_order_on_pause (Union[Unset, bool]): If this flag is set to true, the order will be canceled if the order
            is open and trading on the exchange is paused for any reason.
    """

    order_id: str
    user_id: str
    client_order_id: str
    ticker: str
    side: OrderSide
    action: OrderAction
    type_: OrderType
    status: OrderStatus
    yes_price: float
    no_price: float
    yes_price_dollars: str
    no_price_dollars: str
    fill_count: int
    remaining_count: int
    initial_count: int
    taker_fees: int
    maker_fees: int
    taker_fill_cost: int
    maker_fill_cost: int
    taker_fill_cost_dollars: str
    maker_fill_cost_dollars: str
    queue_position: int
    taker_fees_dollars: Union[None, Unset, str] = UNSET
    maker_fees_dollars: Union[None, Unset, str] = UNSET
    expiration_time: Union[None, Unset, datetime.datetime] = UNSET
    created_time: Union[None, Unset, datetime.datetime] = UNSET
    last_update_time: Union[None, Unset, datetime.datetime] = UNSET
    self_trade_prevention_type: Union[Unset, OrderSelfTradePreventionType] = UNSET
    order_group_id: Union[None, UUID, Unset] = UNSET
    cancel_order_on_pause: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        user_id = self.user_id

        client_order_id = self.client_order_id

        ticker = self.ticker

        side = self.side.value

        action = self.action.value

        type_ = self.type_.value

        status = self.status.value

        yes_price = self.yes_price

        no_price = self.no_price

        yes_price_dollars = self.yes_price_dollars

        no_price_dollars = self.no_price_dollars

        fill_count = self.fill_count

        remaining_count = self.remaining_count

        initial_count = self.initial_count

        taker_fees = self.taker_fees

        maker_fees = self.maker_fees

        taker_fill_cost = self.taker_fill_cost

        maker_fill_cost = self.maker_fill_cost

        taker_fill_cost_dollars = self.taker_fill_cost_dollars

        maker_fill_cost_dollars = self.maker_fill_cost_dollars

        queue_position = self.queue_position

        taker_fees_dollars: Union[None, Unset, str]
        if isinstance(self.taker_fees_dollars, Unset):
            taker_fees_dollars = UNSET
        else:
            taker_fees_dollars = self.taker_fees_dollars

        maker_fees_dollars: Union[None, Unset, str]
        if isinstance(self.maker_fees_dollars, Unset):
            maker_fees_dollars = UNSET
        else:
            maker_fees_dollars = self.maker_fees_dollars

        expiration_time: Union[None, Unset, str]
        if isinstance(self.expiration_time, Unset):
            expiration_time = UNSET
        elif isinstance(self.expiration_time, datetime.datetime):
            expiration_time = self.expiration_time.isoformat()
        else:
            expiration_time = self.expiration_time

        created_time: Union[None, Unset, str]
        if isinstance(self.created_time, Unset):
            created_time = UNSET
        elif isinstance(self.created_time, datetime.datetime):
            created_time = self.created_time.isoformat()
        else:
            created_time = self.created_time

        last_update_time: Union[None, Unset, str]
        if isinstance(self.last_update_time, Unset):
            last_update_time = UNSET
        elif isinstance(self.last_update_time, datetime.datetime):
            last_update_time = self.last_update_time.isoformat()
        else:
            last_update_time = self.last_update_time

        self_trade_prevention_type: Union[Unset, str] = UNSET
        if not isinstance(self.self_trade_prevention_type, Unset):
            self_trade_prevention_type = self.self_trade_prevention_type.value

        order_group_id: Union[None, Unset, str]
        if isinstance(self.order_group_id, Unset):
            order_group_id = UNSET
        elif isinstance(self.order_group_id, UUID):
            order_group_id = str(self.order_group_id)
        else:
            order_group_id = self.order_group_id

        cancel_order_on_pause = self.cancel_order_on_pause

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_id": order_id,
                "user_id": user_id,
                "client_order_id": client_order_id,
                "ticker": ticker,
                "side": side,
                "action": action,
                "type": type_,
                "status": status,
                "yes_price": yes_price,
                "no_price": no_price,
                "yes_price_dollars": yes_price_dollars,
                "no_price_dollars": no_price_dollars,
                "fill_count": fill_count,
                "remaining_count": remaining_count,
                "initial_count": initial_count,
                "taker_fees": taker_fees,
                "maker_fees": maker_fees,
                "taker_fill_cost": taker_fill_cost,
                "maker_fill_cost": maker_fill_cost,
                "taker_fill_cost_dollars": taker_fill_cost_dollars,
                "maker_fill_cost_dollars": maker_fill_cost_dollars,
                "queue_position": queue_position,
            }
        )
        if taker_fees_dollars is not UNSET:
            field_dict["taker_fees_dollars"] = taker_fees_dollars
        if maker_fees_dollars is not UNSET:
            field_dict["maker_fees_dollars"] = maker_fees_dollars
        if expiration_time is not UNSET:
            field_dict["expiration_time"] = expiration_time
        if created_time is not UNSET:
            field_dict["created_time"] = created_time
        if last_update_time is not UNSET:
            field_dict["last_update_time"] = last_update_time
        if self_trade_prevention_type is not UNSET:
            field_dict["self_trade_prevention_type"] = self_trade_prevention_type
        if order_group_id is not UNSET:
            field_dict["order_group_id"] = order_group_id
        if cancel_order_on_pause is not UNSET:
            field_dict["cancel_order_on_pause"] = cancel_order_on_pause

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_id = d.pop("order_id")

        user_id = d.pop("user_id")

        client_order_id = d.pop("client_order_id")

        ticker = d.pop("ticker")

        side = OrderSide(d.pop("side"))

        action = OrderAction(d.pop("action"))

        type_ = OrderType(d.pop("type"))

        status = OrderStatus(d.pop("status"))

        yes_price = d.pop("yes_price")

        no_price = d.pop("no_price")

        yes_price_dollars = d.pop("yes_price_dollars")

        no_price_dollars = d.pop("no_price_dollars")

        fill_count = d.pop("fill_count")

        remaining_count = d.pop("remaining_count")

        initial_count = d.pop("initial_count")

        taker_fees = d.pop("taker_fees")

        maker_fees = d.pop("maker_fees")

        taker_fill_cost = d.pop("taker_fill_cost")

        maker_fill_cost = d.pop("maker_fill_cost")

        taker_fill_cost_dollars = d.pop("taker_fill_cost_dollars")

        maker_fill_cost_dollars = d.pop("maker_fill_cost_dollars")

        queue_position = d.pop("queue_position")

        def _parse_taker_fees_dollars(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        taker_fees_dollars = _parse_taker_fees_dollars(d.pop("taker_fees_dollars", UNSET))

        def _parse_maker_fees_dollars(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        maker_fees_dollars = _parse_maker_fees_dollars(d.pop("maker_fees_dollars", UNSET))

        def _parse_expiration_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiration_time_type_0 = isoparse(data)

                return expiration_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        expiration_time = _parse_expiration_time(d.pop("expiration_time", UNSET))

        def _parse_created_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_time_type_0 = isoparse(data)

                return created_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_time = _parse_created_time(d.pop("created_time", UNSET))

        def _parse_last_update_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_update_time_type_0 = isoparse(data)

                return last_update_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_update_time = _parse_last_update_time(d.pop("last_update_time", UNSET))

        _self_trade_prevention_type = d.pop("self_trade_prevention_type", UNSET)
        self_trade_prevention_type: Union[Unset, OrderSelfTradePreventionType]
        if isinstance(_self_trade_prevention_type, Unset):
            self_trade_prevention_type = UNSET
        else:
            self_trade_prevention_type = OrderSelfTradePreventionType(_self_trade_prevention_type)

        def _parse_order_group_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                order_group_id_type_0 = UUID(data)

                return order_group_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        order_group_id = _parse_order_group_id(d.pop("order_group_id", UNSET))

        cancel_order_on_pause = d.pop("cancel_order_on_pause", UNSET)

        order = cls(
            order_id=order_id,
            user_id=user_id,
            client_order_id=client_order_id,
            ticker=ticker,
            side=side,
            action=action,
            type_=type_,
            status=status,
            yes_price=yes_price,
            no_price=no_price,
            yes_price_dollars=yes_price_dollars,
            no_price_dollars=no_price_dollars,
            fill_count=fill_count,
            remaining_count=remaining_count,
            initial_count=initial_count,
            taker_fees=taker_fees,
            maker_fees=maker_fees,
            taker_fill_cost=taker_fill_cost,
            maker_fill_cost=maker_fill_cost,
            taker_fill_cost_dollars=taker_fill_cost_dollars,
            maker_fill_cost_dollars=maker_fill_cost_dollars,
            queue_position=queue_position,
            taker_fees_dollars=taker_fees_dollars,
            maker_fees_dollars=maker_fees_dollars,
            expiration_time=expiration_time,
            created_time=created_time,
            last_update_time=last_update_time,
            self_trade_prevention_type=self_trade_prevention_type,
            order_group_id=order_group_id,
            cancel_order_on_pause=cancel_order_on_pause,
        )

        order.additional_properties = d
        return order

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
