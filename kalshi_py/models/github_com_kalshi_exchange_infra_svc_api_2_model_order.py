from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelOrder")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelOrder:
    """
    Attributes:
        action (Union[Unset, str]):
        client_order_id (Union[Unset, str]):
        created_time (Union[Unset, Any]):
        expiration_time (Union[Unset, Any]):
        fill_count (Union[Unset, int]): The size of filled orders (maker + taker).
        initial_count (Union[Unset, int]): The initial size of the order (contract units).
        last_update_time (Union[Unset, Any]):
        maker_fees (Union[Unset, int]):
        maker_fill_cost (Union[Unset, int]):
        no_price (Union[Unset, int]):
        no_price_dollars (Union[Unset, list[int]]):
        order_group_id (Union[Unset, str]):
        order_id (Union[Unset, str]): Unique identifier for orders.
        queue_position (Union[Unset, int]): Position in the priority queue at a given price level.
        remaining_count (Union[Unset, int]): The size of the remaining resting orders (contract units).
        self_trade_prevention_type (Union[Unset, str]):
        side (Union[Unset, str]):
        status (Union[Unset, str]):
        taker_fees (Union[Unset, int]):
        taker_fill_cost (Union[Unset, int]):
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
    fill_count: Union[Unset, int] = UNSET
    initial_count: Union[Unset, int] = UNSET
    last_update_time: Union[Unset, Any] = UNSET
    maker_fees: Union[Unset, int] = UNSET
    maker_fill_cost: Union[Unset, int] = UNSET
    no_price: Union[Unset, int] = UNSET
    no_price_dollars: Union[Unset, list[int]] = UNSET
    order_group_id: Union[Unset, str] = UNSET
    order_id: Union[Unset, str] = UNSET
    queue_position: Union[Unset, int] = UNSET
    remaining_count: Union[Unset, int] = UNSET
    self_trade_prevention_type: Union[Unset, str] = UNSET
    side: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    taker_fees: Union[Unset, int] = UNSET
    taker_fill_cost: Union[Unset, int] = UNSET
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

        fill_count = self.fill_count

        initial_count = self.initial_count

        last_update_time = self.last_update_time

        maker_fees = self.maker_fees

        maker_fill_cost = self.maker_fill_cost

        no_price = self.no_price

        no_price_dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.no_price_dollars, Unset):
            no_price_dollars = self.no_price_dollars

        order_group_id = self.order_group_id

        order_id = self.order_id

        queue_position = self.queue_position

        remaining_count = self.remaining_count

        self_trade_prevention_type = self.self_trade_prevention_type

        side = self.side

        status = self.status

        taker_fees = self.taker_fees

        taker_fill_cost = self.taker_fill_cost

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
        if fill_count is not UNSET:
            field_dict["fill_count"] = fill_count
        if initial_count is not UNSET:
            field_dict["initial_count"] = initial_count
        if last_update_time is not UNSET:
            field_dict["last_update_time"] = last_update_time
        if maker_fees is not UNSET:
            field_dict["maker_fees"] = maker_fees
        if maker_fill_cost is not UNSET:
            field_dict["maker_fill_cost"] = maker_fill_cost
        if no_price is not UNSET:
            field_dict["no_price"] = no_price
        if no_price_dollars is not UNSET:
            field_dict["no_price_dollars"] = no_price_dollars
        if order_group_id is not UNSET:
            field_dict["order_group_id"] = order_group_id
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if queue_position is not UNSET:
            field_dict["queue_position"] = queue_position
        if remaining_count is not UNSET:
            field_dict["remaining_count"] = remaining_count
        if self_trade_prevention_type is not UNSET:
            field_dict["self_trade_prevention_type"] = self_trade_prevention_type
        if side is not UNSET:
            field_dict["side"] = side
        if status is not UNSET:
            field_dict["status"] = status
        if taker_fees is not UNSET:
            field_dict["taker_fees"] = taker_fees
        if taker_fill_cost is not UNSET:
            field_dict["taker_fill_cost"] = taker_fill_cost
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

        fill_count = d.pop("fill_count", UNSET)

        initial_count = d.pop("initial_count", UNSET)

        last_update_time = d.pop("last_update_time", UNSET)

        maker_fees = d.pop("maker_fees", UNSET)

        maker_fill_cost = d.pop("maker_fill_cost", UNSET)

        no_price = d.pop("no_price", UNSET)

        no_price_dollars = cast(list[int], d.pop("no_price_dollars", UNSET))

        order_group_id = d.pop("order_group_id", UNSET)

        order_id = d.pop("order_id", UNSET)

        queue_position = d.pop("queue_position", UNSET)

        remaining_count = d.pop("remaining_count", UNSET)

        self_trade_prevention_type = d.pop("self_trade_prevention_type", UNSET)

        side = d.pop("side", UNSET)

        status = d.pop("status", UNSET)

        taker_fees = d.pop("taker_fees", UNSET)

        taker_fill_cost = d.pop("taker_fill_cost", UNSET)

        ticker = d.pop("ticker", UNSET)

        type_ = d.pop("type", UNSET)

        user_id = d.pop("user_id", UNSET)

        yes_price = d.pop("yes_price", UNSET)

        yes_price_dollars = cast(list[int], d.pop("yes_price_dollars", UNSET))

        github_com_kalshi_exchange_infra_svc_api_2_model_order = cls(
            action=action,
            client_order_id=client_order_id,
            created_time=created_time,
            expiration_time=expiration_time,
            fill_count=fill_count,
            initial_count=initial_count,
            last_update_time=last_update_time,
            maker_fees=maker_fees,
            maker_fill_cost=maker_fill_cost,
            no_price=no_price,
            no_price_dollars=no_price_dollars,
            order_group_id=order_group_id,
            order_id=order_id,
            queue_position=queue_position,
            remaining_count=remaining_count,
            self_trade_prevention_type=self_trade_prevention_type,
            side=side,
            status=status,
            taker_fees=taker_fees,
            taker_fill_cost=taker_fill_cost,
            ticker=ticker,
            type_=type_,
            user_id=user_id,
            yes_price=yes_price,
            yes_price_dollars=yes_price_dollars,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_order.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_order

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
