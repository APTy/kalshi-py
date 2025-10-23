from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelPublicTrade")


@_attrs_define
class ModelPublicTrade:
    """
    Attributes:
        count (Union[Unset, int]): Number of contracts bought or sold in this trade.
        created_time (Union[Unset, Any]):
        no_price (Union[Unset, int]):
        no_price_dollars (Union[Unset, str]): Fixed point representation of a subpenny dollar amount e.g. 1.2345
            indicates $1.23 and 45/100 of a cent. Example: 0.2300.
        taker_side (Union[Unset, str]):
        ticker (Union[Unset, str]): Unique identifier for the market.
        trade_id (Union[Unset, str]):
        yes_price (Union[Unset, int]):
        yes_price_dollars (Union[Unset, str]): Fixed point representation of a subpenny dollar amount e.g. 1.2345
            indicates $1.23 and 45/100 of a cent. Example: 0.2300.
    """

    count: Union[Unset, int] = UNSET
    created_time: Union[Unset, Any] = UNSET
    no_price: Union[Unset, int] = UNSET
    no_price_dollars: Union[Unset, str] = UNSET
    taker_side: Union[Unset, str] = UNSET
    ticker: Union[Unset, str] = UNSET
    trade_id: Union[Unset, str] = UNSET
    yes_price: Union[Unset, int] = UNSET
    yes_price_dollars: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        created_time = self.created_time

        no_price = self.no_price

        no_price_dollars = self.no_price_dollars

        taker_side = self.taker_side

        ticker = self.ticker

        trade_id = self.trade_id

        yes_price = self.yes_price

        yes_price_dollars = self.yes_price_dollars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if created_time is not UNSET:
            field_dict["created_time"] = created_time
        if no_price is not UNSET:
            field_dict["no_price"] = no_price
        if no_price_dollars is not UNSET:
            field_dict["no_price_dollars"] = no_price_dollars
        if taker_side is not UNSET:
            field_dict["taker_side"] = taker_side
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if trade_id is not UNSET:
            field_dict["trade_id"] = trade_id
        if yes_price is not UNSET:
            field_dict["yes_price"] = yes_price
        if yes_price_dollars is not UNSET:
            field_dict["yes_price_dollars"] = yes_price_dollars

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        created_time = d.pop("created_time", UNSET)

        no_price = d.pop("no_price", UNSET)

        no_price_dollars = d.pop("no_price_dollars", UNSET)

        taker_side = d.pop("taker_side", UNSET)

        ticker = d.pop("ticker", UNSET)

        trade_id = d.pop("trade_id", UNSET)

        yes_price = d.pop("yes_price", UNSET)

        yes_price_dollars = d.pop("yes_price_dollars", UNSET)

        model_public_trade = cls(
            count=count,
            created_time=created_time,
            no_price=no_price,
            no_price_dollars=no_price_dollars,
            taker_side=taker_side,
            ticker=ticker,
            trade_id=trade_id,
            yes_price=yes_price,
            yes_price_dollars=yes_price_dollars,
        )

        model_public_trade.additional_properties = d
        return model_public_trade

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
