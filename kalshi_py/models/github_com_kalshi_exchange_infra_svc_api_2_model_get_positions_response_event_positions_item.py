from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponseEventPositionsItem")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponseEventPositionsItem:
    """
    Attributes:
        event_exposure (Union[Unset, int]):
        event_exposure_dollars (Union[Unset, list[int]]):
        event_ticker (Union[Unset, str]): Unique identifier for events.
        fees_paid (Union[Unset, int]):
        fees_paid_dollars (Union[Unset, list[int]]):
        realized_pnl (Union[Unset, int]):
        realized_pnl_dollars (Union[Unset, list[int]]):
        resting_order_count (Union[Unset, int]): Aggregate size of resting orders in contract units.
        total_cost (Union[Unset, int]):
        total_cost_dollars (Union[Unset, list[int]]):
    """

    event_exposure: Union[Unset, int] = UNSET
    event_exposure_dollars: Union[Unset, list[int]] = UNSET
    event_ticker: Union[Unset, str] = UNSET
    fees_paid: Union[Unset, int] = UNSET
    fees_paid_dollars: Union[Unset, list[int]] = UNSET
    realized_pnl: Union[Unset, int] = UNSET
    realized_pnl_dollars: Union[Unset, list[int]] = UNSET
    resting_order_count: Union[Unset, int] = UNSET
    total_cost: Union[Unset, int] = UNSET
    total_cost_dollars: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_exposure = self.event_exposure

        event_exposure_dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.event_exposure_dollars, Unset):
            event_exposure_dollars = self.event_exposure_dollars

        event_ticker = self.event_ticker

        fees_paid = self.fees_paid

        fees_paid_dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.fees_paid_dollars, Unset):
            fees_paid_dollars = self.fees_paid_dollars

        realized_pnl = self.realized_pnl

        realized_pnl_dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.realized_pnl_dollars, Unset):
            realized_pnl_dollars = self.realized_pnl_dollars

        resting_order_count = self.resting_order_count

        total_cost = self.total_cost

        total_cost_dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.total_cost_dollars, Unset):
            total_cost_dollars = self.total_cost_dollars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_exposure is not UNSET:
            field_dict["event_exposure"] = event_exposure
        if event_exposure_dollars is not UNSET:
            field_dict["event_exposure_dollars"] = event_exposure_dollars
        if event_ticker is not UNSET:
            field_dict["event_ticker"] = event_ticker
        if fees_paid is not UNSET:
            field_dict["fees_paid"] = fees_paid
        if fees_paid_dollars is not UNSET:
            field_dict["fees_paid_dollars"] = fees_paid_dollars
        if realized_pnl is not UNSET:
            field_dict["realized_pnl"] = realized_pnl
        if realized_pnl_dollars is not UNSET:
            field_dict["realized_pnl_dollars"] = realized_pnl_dollars
        if resting_order_count is not UNSET:
            field_dict["resting_order_count"] = resting_order_count
        if total_cost is not UNSET:
            field_dict["total_cost"] = total_cost
        if total_cost_dollars is not UNSET:
            field_dict["total_cost_dollars"] = total_cost_dollars

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_exposure = d.pop("event_exposure", UNSET)

        event_exposure_dollars = cast(list[int], d.pop("event_exposure_dollars", UNSET))

        event_ticker = d.pop("event_ticker", UNSET)

        fees_paid = d.pop("fees_paid", UNSET)

        fees_paid_dollars = cast(list[int], d.pop("fees_paid_dollars", UNSET))

        realized_pnl = d.pop("realized_pnl", UNSET)

        realized_pnl_dollars = cast(list[int], d.pop("realized_pnl_dollars", UNSET))

        resting_order_count = d.pop("resting_order_count", UNSET)

        total_cost = d.pop("total_cost", UNSET)

        total_cost_dollars = cast(list[int], d.pop("total_cost_dollars", UNSET))

        github_com_kalshi_exchange_infra_svc_api_2_model_get_positions_response_event_positions_item = cls(
            event_exposure=event_exposure,
            event_exposure_dollars=event_exposure_dollars,
            event_ticker=event_ticker,
            fees_paid=fees_paid,
            fees_paid_dollars=fees_paid_dollars,
            realized_pnl=realized_pnl,
            realized_pnl_dollars=realized_pnl_dollars,
            resting_order_count=resting_order_count,
            total_cost=total_cost,
            total_cost_dollars=total_cost_dollars,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_get_positions_response_event_positions_item.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_get_positions_response_event_positions_item

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
