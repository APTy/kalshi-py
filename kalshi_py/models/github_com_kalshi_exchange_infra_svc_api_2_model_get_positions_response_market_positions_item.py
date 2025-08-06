import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponseMarketPositionsItem")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponseMarketPositionsItem:
    """
    Attributes:
        fees_paid (Union[Unset, int]):
        fees_paid_dollars (Union[Unset, list[int]]):
        last_updated_ts (Union[Unset, datetime.datetime]): Last time the position is updated.
        market_exposure (Union[Unset, int]):
        market_exposure_dollars (Union[Unset, list[int]]):
        position (Union[Unset, int]): Number of contracts bought in this market. Negative means NO contracts and
            positive means YES contracts.
        realized_pnl (Union[Unset, int]):
        realized_pnl_dollars (Union[Unset, list[int]]):
        resting_orders_count (Union[Unset, int]): Aggregate size of resting orders in contract units.
        ticker (Union[Unset, str]): Unique identifier for the market.
        total_traded (Union[Unset, int]):
        total_traded_dollars (Union[Unset, list[int]]):
    """

    fees_paid: Union[Unset, int] = UNSET
    fees_paid_dollars: Union[Unset, list[int]] = UNSET
    last_updated_ts: Union[Unset, datetime.datetime] = UNSET
    market_exposure: Union[Unset, int] = UNSET
    market_exposure_dollars: Union[Unset, list[int]] = UNSET
    position: Union[Unset, int] = UNSET
    realized_pnl: Union[Unset, int] = UNSET
    realized_pnl_dollars: Union[Unset, list[int]] = UNSET
    resting_orders_count: Union[Unset, int] = UNSET
    ticker: Union[Unset, str] = UNSET
    total_traded: Union[Unset, int] = UNSET
    total_traded_dollars: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fees_paid = self.fees_paid

        fees_paid_dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.fees_paid_dollars, Unset):
            fees_paid_dollars = self.fees_paid_dollars

        last_updated_ts: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_ts, Unset):
            last_updated_ts = self.last_updated_ts.isoformat()

        market_exposure = self.market_exposure

        market_exposure_dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.market_exposure_dollars, Unset):
            market_exposure_dollars = self.market_exposure_dollars

        position = self.position

        realized_pnl = self.realized_pnl

        realized_pnl_dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.realized_pnl_dollars, Unset):
            realized_pnl_dollars = self.realized_pnl_dollars

        resting_orders_count = self.resting_orders_count

        ticker = self.ticker

        total_traded = self.total_traded

        total_traded_dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.total_traded_dollars, Unset):
            total_traded_dollars = self.total_traded_dollars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fees_paid is not UNSET:
            field_dict["fees_paid"] = fees_paid
        if fees_paid_dollars is not UNSET:
            field_dict["fees_paid_dollars"] = fees_paid_dollars
        if last_updated_ts is not UNSET:
            field_dict["last_updated_ts"] = last_updated_ts
        if market_exposure is not UNSET:
            field_dict["market_exposure"] = market_exposure
        if market_exposure_dollars is not UNSET:
            field_dict["market_exposure_dollars"] = market_exposure_dollars
        if position is not UNSET:
            field_dict["position"] = position
        if realized_pnl is not UNSET:
            field_dict["realized_pnl"] = realized_pnl
        if realized_pnl_dollars is not UNSET:
            field_dict["realized_pnl_dollars"] = realized_pnl_dollars
        if resting_orders_count is not UNSET:
            field_dict["resting_orders_count"] = resting_orders_count
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if total_traded is not UNSET:
            field_dict["total_traded"] = total_traded
        if total_traded_dollars is not UNSET:
            field_dict["total_traded_dollars"] = total_traded_dollars

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fees_paid = d.pop("fees_paid", UNSET)

        fees_paid_dollars = cast(list[int], d.pop("fees_paid_dollars", UNSET))

        _last_updated_ts = d.pop("last_updated_ts", UNSET)
        last_updated_ts: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_ts, Unset):
            last_updated_ts = UNSET
        else:
            last_updated_ts = isoparse(_last_updated_ts)

        market_exposure = d.pop("market_exposure", UNSET)

        market_exposure_dollars = cast(list[int], d.pop("market_exposure_dollars", UNSET))

        position = d.pop("position", UNSET)

        realized_pnl = d.pop("realized_pnl", UNSET)

        realized_pnl_dollars = cast(list[int], d.pop("realized_pnl_dollars", UNSET))

        resting_orders_count = d.pop("resting_orders_count", UNSET)

        ticker = d.pop("ticker", UNSET)

        total_traded = d.pop("total_traded", UNSET)

        total_traded_dollars = cast(list[int], d.pop("total_traded_dollars", UNSET))

        github_com_kalshi_exchange_infra_svc_api_2_model_get_positions_response_market_positions_item = cls(
            fees_paid=fees_paid,
            fees_paid_dollars=fees_paid_dollars,
            last_updated_ts=last_updated_ts,
            market_exposure=market_exposure,
            market_exposure_dollars=market_exposure_dollars,
            position=position,
            realized_pnl=realized_pnl,
            realized_pnl_dollars=realized_pnl_dollars,
            resting_orders_count=resting_orders_count,
            ticker=ticker,
            total_traded=total_traded,
            total_traded_dollars=total_traded_dollars,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_get_positions_response_market_positions_item.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_get_positions_response_market_positions_item

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
