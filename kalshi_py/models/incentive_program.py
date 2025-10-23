import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncentiveProgram")


@_attrs_define
class IncentiveProgram:
    """
    Attributes:
        discount_factor_bps (Union[Unset, int]):
        end_date (Union[Unset, datetime.datetime]):
        event_ticker (Union[Unset, str]):
        id (Union[Unset, str]):
        incentive_type (Union[Unset, str]):
        market_ticker (Union[Unset, str]):
        paid_out (Union[Unset, bool]):
        period_reward (Union[Unset, int]): Period reward in centicents.
        series_ticker (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):
        target_size (Union[Unset, int]):
    """

    discount_factor_bps: Union[Unset, int] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    event_ticker: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    incentive_type: Union[Unset, str] = UNSET
    market_ticker: Union[Unset, str] = UNSET
    paid_out: Union[Unset, bool] = UNSET
    period_reward: Union[Unset, int] = UNSET
    series_ticker: Union[Unset, str] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    target_size: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discount_factor_bps = self.discount_factor_bps

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        event_ticker = self.event_ticker

        id = self.id

        incentive_type = self.incentive_type

        market_ticker = self.market_ticker

        paid_out = self.paid_out

        period_reward = self.period_reward

        series_ticker = self.series_ticker

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        target_size = self.target_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if discount_factor_bps is not UNSET:
            field_dict["discount_factor_bps"] = discount_factor_bps
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if event_ticker is not UNSET:
            field_dict["event_ticker"] = event_ticker
        if id is not UNSET:
            field_dict["id"] = id
        if incentive_type is not UNSET:
            field_dict["incentive_type"] = incentive_type
        if market_ticker is not UNSET:
            field_dict["market_ticker"] = market_ticker
        if paid_out is not UNSET:
            field_dict["paid_out"] = paid_out
        if period_reward is not UNSET:
            field_dict["period_reward"] = period_reward
        if series_ticker is not UNSET:
            field_dict["series_ticker"] = series_ticker
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if target_size is not UNSET:
            field_dict["target_size"] = target_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        discount_factor_bps = d.pop("discount_factor_bps", UNSET)

        _end_date = d.pop("end_date", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        event_ticker = d.pop("event_ticker", UNSET)

        id = d.pop("id", UNSET)

        incentive_type = d.pop("incentive_type", UNSET)

        market_ticker = d.pop("market_ticker", UNSET)

        paid_out = d.pop("paid_out", UNSET)

        period_reward = d.pop("period_reward", UNSET)

        series_ticker = d.pop("series_ticker", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        target_size = d.pop("target_size", UNSET)

        incentive_program = cls(
            discount_factor_bps=discount_factor_bps,
            end_date=end_date,
            event_ticker=event_ticker,
            id=id,
            incentive_type=incentive_type,
            market_ticker=market_ticker,
            paid_out=paid_out,
            period_reward=period_reward,
            series_ticker=series_ticker,
            start_date=start_date,
            target_size=target_size,
        )

        incentive_program.additional_properties = d
        return incentive_program

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
