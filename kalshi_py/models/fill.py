import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.fill_action import FillAction
from ..models.fill_side import FillSide
from ..types import UNSET, Unset

T = TypeVar("T", bound="Fill")


@_attrs_define
class Fill:
    """
    Attributes:
        fill_id (Union[Unset, str]): Unique identifier for this fill
        trade_id (Union[Unset, str]): Unique identifier for this fill (legacy field name, same as fill_id)
        order_id (Union[Unset, str]): Unique identifier for the order that resulted in this fill
        client_order_id (Union[Unset, str]): Client-provided identifier for the order that resulted in this fill
        ticker (Union[Unset, str]): Unique identifier for the market
        market_ticker (Union[Unset, str]): Unique identifier for the market (legacy field name, same as ticker)
        side (Union[Unset, FillSide]): Specifies if this is a 'yes' or 'no' fill
        action (Union[Unset, FillAction]): Specifies if this is a buy or sell order
        count (Union[Unset, int]): Number of contracts bought or sold in this fill
        price (Union[Unset, float]): Fill price (deprecated - use yes_price or no_price)
        yes_price (Union[Unset, int]): Fill price for the yes side in cents
        no_price (Union[Unset, int]): Fill price for the no side in cents
        yes_price_fixed (Union[Unset, str]): Fill price for the yes side in fixed point dollars
        no_price_fixed (Union[Unset, str]): Fill price for the no side in fixed point dollars
        is_taker (Union[Unset, bool]): If true, this fill was a taker (removed liquidity from the order book)
        created_time (Union[Unset, datetime.datetime]): Timestamp when this fill was executed
        ts (Union[Unset, int]): Unix timestamp when this fill was executed (legacy field name)
    """

    fill_id: Union[Unset, str] = UNSET
    trade_id: Union[Unset, str] = UNSET
    order_id: Union[Unset, str] = UNSET
    client_order_id: Union[Unset, str] = UNSET
    ticker: Union[Unset, str] = UNSET
    market_ticker: Union[Unset, str] = UNSET
    side: Union[Unset, FillSide] = UNSET
    action: Union[Unset, FillAction] = UNSET
    count: Union[Unset, int] = UNSET
    price: Union[Unset, float] = UNSET
    yes_price: Union[Unset, int] = UNSET
    no_price: Union[Unset, int] = UNSET
    yes_price_fixed: Union[Unset, str] = UNSET
    no_price_fixed: Union[Unset, str] = UNSET
    is_taker: Union[Unset, bool] = UNSET
    created_time: Union[Unset, datetime.datetime] = UNSET
    ts: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fill_id = self.fill_id

        trade_id = self.trade_id

        order_id = self.order_id

        client_order_id = self.client_order_id

        ticker = self.ticker

        market_ticker = self.market_ticker

        side: Union[Unset, str] = UNSET
        if not isinstance(self.side, Unset):
            side = self.side.value

        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        count = self.count

        price = self.price

        yes_price = self.yes_price

        no_price = self.no_price

        yes_price_fixed = self.yes_price_fixed

        no_price_fixed = self.no_price_fixed

        is_taker = self.is_taker

        created_time: Union[Unset, str] = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        ts = self.ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fill_id is not UNSET:
            field_dict["fill_id"] = fill_id
        if trade_id is not UNSET:
            field_dict["trade_id"] = trade_id
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if client_order_id is not UNSET:
            field_dict["client_order_id"] = client_order_id
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if market_ticker is not UNSET:
            field_dict["market_ticker"] = market_ticker
        if side is not UNSET:
            field_dict["side"] = side
        if action is not UNSET:
            field_dict["action"] = action
        if count is not UNSET:
            field_dict["count"] = count
        if price is not UNSET:
            field_dict["price"] = price
        if yes_price is not UNSET:
            field_dict["yes_price"] = yes_price
        if no_price is not UNSET:
            field_dict["no_price"] = no_price
        if yes_price_fixed is not UNSET:
            field_dict["yes_price_fixed"] = yes_price_fixed
        if no_price_fixed is not UNSET:
            field_dict["no_price_fixed"] = no_price_fixed
        if is_taker is not UNSET:
            field_dict["is_taker"] = is_taker
        if created_time is not UNSET:
            field_dict["created_time"] = created_time
        if ts is not UNSET:
            field_dict["ts"] = ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fill_id = d.pop("fill_id", UNSET)

        trade_id = d.pop("trade_id", UNSET)

        order_id = d.pop("order_id", UNSET)

        client_order_id = d.pop("client_order_id", UNSET)

        ticker = d.pop("ticker", UNSET)

        market_ticker = d.pop("market_ticker", UNSET)

        _side = d.pop("side", UNSET)
        side: Union[Unset, FillSide]
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = FillSide(_side)

        _action = d.pop("action", UNSET)
        action: Union[Unset, FillAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = FillAction(_action)

        count = d.pop("count", UNSET)

        price = d.pop("price", UNSET)

        yes_price = d.pop("yes_price", UNSET)

        no_price = d.pop("no_price", UNSET)

        yes_price_fixed = d.pop("yes_price_fixed", UNSET)

        no_price_fixed = d.pop("no_price_fixed", UNSET)

        is_taker = d.pop("is_taker", UNSET)

        _created_time = d.pop("created_time", UNSET)
        created_time: Union[Unset, datetime.datetime]
        if isinstance(_created_time, Unset):
            created_time = UNSET
        else:
            created_time = isoparse(_created_time)

        ts = d.pop("ts", UNSET)

        fill = cls(
            fill_id=fill_id,
            trade_id=trade_id,
            order_id=order_id,
            client_order_id=client_order_id,
            ticker=ticker,
            market_ticker=market_ticker,
            side=side,
            action=action,
            count=count,
            price=price,
            yes_price=yes_price,
            no_price=no_price,
            yes_price_fixed=yes_price_fixed,
            no_price_fixed=no_price_fixed,
            is_taker=is_taker,
            created_time=created_time,
            ts=ts,
        )

        fill.additional_properties = d
        return fill

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
