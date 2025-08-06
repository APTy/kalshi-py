from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelFill")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelFill:
    """
    Attributes:
        action (Union[Unset, str]):
        count (Union[Unset, int]): Number of contracts bought or sold in this fill.
        created_time (Union[Unset, Any]):
        is_taker (Union[Unset, bool]): If true, this fill was a taker (removed liquidity from the order book).
        no_price (Union[Unset, int]):
        no_price_fixed (Union[Unset, list[int]]):
        order_id (Union[Unset, str]):
        side (Union[Unset, str]):
        ticker (Union[Unset, str]): Unique identifier for the market.
        trade_id (Union[Unset, str]):
        yes_price (Union[Unset, int]):
        yes_price_fixed (Union[Unset, list[int]]):
    """

    action: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    created_time: Union[Unset, Any] = UNSET
    is_taker: Union[Unset, bool] = UNSET
    no_price: Union[Unset, int] = UNSET
    no_price_fixed: Union[Unset, list[int]] = UNSET
    order_id: Union[Unset, str] = UNSET
    side: Union[Unset, str] = UNSET
    ticker: Union[Unset, str] = UNSET
    trade_id: Union[Unset, str] = UNSET
    yes_price: Union[Unset, int] = UNSET
    yes_price_fixed: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        count = self.count

        created_time = self.created_time

        is_taker = self.is_taker

        no_price = self.no_price

        no_price_fixed: Union[Unset, list[int]] = UNSET
        if not isinstance(self.no_price_fixed, Unset):
            no_price_fixed = self.no_price_fixed

        order_id = self.order_id

        side = self.side

        ticker = self.ticker

        trade_id = self.trade_id

        yes_price = self.yes_price

        yes_price_fixed: Union[Unset, list[int]] = UNSET
        if not isinstance(self.yes_price_fixed, Unset):
            yes_price_fixed = self.yes_price_fixed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if count is not UNSET:
            field_dict["count"] = count
        if created_time is not UNSET:
            field_dict["created_time"] = created_time
        if is_taker is not UNSET:
            field_dict["is_taker"] = is_taker
        if no_price is not UNSET:
            field_dict["no_price"] = no_price
        if no_price_fixed is not UNSET:
            field_dict["no_price_fixed"] = no_price_fixed
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if side is not UNSET:
            field_dict["side"] = side
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if trade_id is not UNSET:
            field_dict["trade_id"] = trade_id
        if yes_price is not UNSET:
            field_dict["yes_price"] = yes_price
        if yes_price_fixed is not UNSET:
            field_dict["yes_price_fixed"] = yes_price_fixed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        count = d.pop("count", UNSET)

        created_time = d.pop("created_time", UNSET)

        is_taker = d.pop("is_taker", UNSET)

        no_price = d.pop("no_price", UNSET)

        no_price_fixed = cast(list[int], d.pop("no_price_fixed", UNSET))

        order_id = d.pop("order_id", UNSET)

        side = d.pop("side", UNSET)

        ticker = d.pop("ticker", UNSET)

        trade_id = d.pop("trade_id", UNSET)

        yes_price = d.pop("yes_price", UNSET)

        yes_price_fixed = cast(list[int], d.pop("yes_price_fixed", UNSET))

        github_com_kalshi_exchange_infra_svc_api_2_model_fill = cls(
            action=action,
            count=count,
            created_time=created_time,
            is_taker=is_taker,
            no_price=no_price,
            no_price_fixed=no_price_fixed,
            order_id=order_id,
            side=side,
            ticker=ticker,
            trade_id=trade_id,
            yes_price=yes_price,
            yes_price_fixed=yes_price_fixed,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_fill.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_fill

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
