from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelPublicTrade")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelPublicTrade:
    """
    Attributes:
        count (Union[Unset, int]): Number of contracts bought or sold in this trade.
        created_time (Union[Unset, Any]):
        no_price (Union[Unset, int]):
        taker_side (Union[Unset, str]):
        ticker (Union[Unset, str]): Unique identifier for the market.
        trade_id (Union[Unset, str]):
        yes_price (Union[Unset, int]):
    """

    count: Union[Unset, int] = UNSET
    created_time: Union[Unset, Any] = UNSET
    no_price: Union[Unset, int] = UNSET
    taker_side: Union[Unset, str] = UNSET
    ticker: Union[Unset, str] = UNSET
    trade_id: Union[Unset, str] = UNSET
    yes_price: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        created_time = self.created_time

        no_price = self.no_price

        taker_side = self.taker_side

        ticker = self.ticker

        trade_id = self.trade_id

        yes_price = self.yes_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if created_time is not UNSET:
            field_dict["created_time"] = created_time
        if no_price is not UNSET:
            field_dict["no_price"] = no_price
        if taker_side is not UNSET:
            field_dict["taker_side"] = taker_side
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if trade_id is not UNSET:
            field_dict["trade_id"] = trade_id
        if yes_price is not UNSET:
            field_dict["yes_price"] = yes_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        created_time = d.pop("created_time", UNSET)

        no_price = d.pop("no_price", UNSET)

        taker_side = d.pop("taker_side", UNSET)

        ticker = d.pop("ticker", UNSET)

        trade_id = d.pop("trade_id", UNSET)

        yes_price = d.pop("yes_price", UNSET)

        github_com_kalshi_exchange_infra_svc_api_2_model_public_trade = cls(
            count=count,
            created_time=created_time,
            no_price=no_price,
            taker_side=taker_side,
            ticker=ticker,
            trade_id=trade_id,
            yes_price=yes_price,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_public_trade.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_public_trade

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
