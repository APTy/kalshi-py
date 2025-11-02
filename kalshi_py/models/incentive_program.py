import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.incentive_program_incentive_type import IncentiveProgramIncentiveType
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncentiveProgram")


@_attrs_define
class IncentiveProgram:
    """
    Attributes:
        id (str): Unique identifier for the incentive program
        market_ticker (str): The ticker symbol of the market associated with this incentive program
        incentive_type (IncentiveProgramIncentiveType): Type of incentive program
        start_date (datetime.datetime): Start date of the incentive program
        end_date (datetime.datetime): End date of the incentive program
        period_reward (int): Total reward for the period in centi-cents
        paid_out (bool): Whether the incentive has been paid out
        discount_factor_bps (Union[None, Unset, int]): Discount factor in basis points (optional)
        target_size (Union[None, Unset, int]): Target size for the incentive program (optional)
    """

    id: str
    market_ticker: str
    incentive_type: IncentiveProgramIncentiveType
    start_date: datetime.datetime
    end_date: datetime.datetime
    period_reward: int
    paid_out: bool
    discount_factor_bps: Union[None, Unset, int] = UNSET
    target_size: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        market_ticker = self.market_ticker

        incentive_type = self.incentive_type.value

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        period_reward = self.period_reward

        paid_out = self.paid_out

        discount_factor_bps: Union[None, Unset, int]
        if isinstance(self.discount_factor_bps, Unset):
            discount_factor_bps = UNSET
        else:
            discount_factor_bps = self.discount_factor_bps

        target_size: Union[None, Unset, int]
        if isinstance(self.target_size, Unset):
            target_size = UNSET
        else:
            target_size = self.target_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "market_ticker": market_ticker,
                "incentive_type": incentive_type,
                "start_date": start_date,
                "end_date": end_date,
                "period_reward": period_reward,
                "paid_out": paid_out,
            }
        )
        if discount_factor_bps is not UNSET:
            field_dict["discount_factor_bps"] = discount_factor_bps
        if target_size is not UNSET:
            field_dict["target_size"] = target_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        market_ticker = d.pop("market_ticker")

        incentive_type = IncentiveProgramIncentiveType(d.pop("incentive_type"))

        start_date = isoparse(d.pop("start_date"))

        end_date = isoparse(d.pop("end_date"))

        period_reward = d.pop("period_reward")

        paid_out = d.pop("paid_out")

        def _parse_discount_factor_bps(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        discount_factor_bps = _parse_discount_factor_bps(d.pop("discount_factor_bps", UNSET))

        def _parse_target_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        target_size = _parse_target_size(d.pop("target_size", UNSET))

        incentive_program = cls(
            id=id,
            market_ticker=market_ticker,
            incentive_type=incentive_type,
            start_date=start_date,
            end_date=end_date,
            period_reward=period_reward,
            paid_out=paid_out,
            discount_factor_bps=discount_factor_bps,
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
