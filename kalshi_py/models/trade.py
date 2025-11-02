import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.trade_taker_side import TradeTakerSide
from ..types import UNSET, Unset

T = TypeVar("T", bound="Trade")


@_attrs_define
class Trade:
    """
    Attributes:
        trade_id (Union[Unset, str]): Unique identifier for this trade
        ticker (Union[Unset, str]): Unique identifier for the market
        price (Union[Unset, float]): Trade price (deprecated - use yes_price or no_price)
        count (Union[Unset, int]): Number of contracts bought or sold in this trade
        yes_price (Union[Unset, int]): Yes price for this trade in cents
        no_price (Union[Unset, int]): No price for this trade in cents
        yes_price_dollars (Union[Unset, str]): Yes price for this trade in dollars
        no_price_dollars (Union[Unset, str]): No price for this trade in dollars
        taker_side (Union[Unset, TradeTakerSide]): Side for the taker of this trade
        created_time (Union[Unset, datetime.datetime]): Timestamp when this trade was executed
    """

    trade_id: Union[Unset, str] = UNSET
    ticker: Union[Unset, str] = UNSET
    price: Union[Unset, float] = UNSET
    count: Union[Unset, int] = UNSET
    yes_price: Union[Unset, int] = UNSET
    no_price: Union[Unset, int] = UNSET
    yes_price_dollars: Union[Unset, str] = UNSET
    no_price_dollars: Union[Unset, str] = UNSET
    taker_side: Union[Unset, TradeTakerSide] = UNSET
    created_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trade_id = self.trade_id

        ticker = self.ticker

        price = self.price

        count = self.count

        yes_price = self.yes_price

        no_price = self.no_price

        yes_price_dollars = self.yes_price_dollars

        no_price_dollars = self.no_price_dollars

        taker_side: Union[Unset, str] = UNSET
        if not isinstance(self.taker_side, Unset):
            taker_side = self.taker_side.value

        created_time: Union[Unset, str] = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trade_id is not UNSET:
            field_dict["trade_id"] = trade_id
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if price is not UNSET:
            field_dict["price"] = price
        if count is not UNSET:
            field_dict["count"] = count
        if yes_price is not UNSET:
            field_dict["yes_price"] = yes_price
        if no_price is not UNSET:
            field_dict["no_price"] = no_price
        if yes_price_dollars is not UNSET:
            field_dict["yes_price_dollars"] = yes_price_dollars
        if no_price_dollars is not UNSET:
            field_dict["no_price_dollars"] = no_price_dollars
        if taker_side is not UNSET:
            field_dict["taker_side"] = taker_side
        if created_time is not UNSET:
            field_dict["created_time"] = created_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trade_id = d.pop("trade_id", UNSET)

        ticker = d.pop("ticker", UNSET)

        price = d.pop("price", UNSET)

        count = d.pop("count", UNSET)

        yes_price = d.pop("yes_price", UNSET)

        no_price = d.pop("no_price", UNSET)

        yes_price_dollars = d.pop("yes_price_dollars", UNSET)

        no_price_dollars = d.pop("no_price_dollars", UNSET)

        _taker_side = d.pop("taker_side", UNSET)
        taker_side: Union[Unset, TradeTakerSide]
        if isinstance(_taker_side, Unset):
            taker_side = UNSET
        else:
            taker_side = TradeTakerSide(_taker_side)

        _created_time = d.pop("created_time", UNSET)
        created_time: Union[Unset, datetime.datetime]
        if isinstance(_created_time, Unset):
            created_time = UNSET
        else:
            created_time = isoparse(_created_time)

        trade = cls(
            trade_id=trade_id,
            ticker=ticker,
            price=price,
            count=count,
            yes_price=yes_price,
            no_price=no_price,
            yes_price_dollars=yes_price_dollars,
            no_price_dollars=no_price_dollars,
            taker_side=taker_side,
            created_time=created_time,
        )

        trade.additional_properties = d
        return trade

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
