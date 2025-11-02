import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.settlement_market_result import SettlementMarketResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="Settlement")


@_attrs_define
class Settlement:
    """
    Attributes:
        ticker (str): The ticker symbol of the market that was settled.
        market_result (SettlementMarketResult): The outcome of the market settlement. 'yes' = market resolved to YES,
            'no' = market resolved to NO, 'scalar' = scalar market settled at a specific value, 'void' = market was
            voided/cancelled and all positions returned at original cost.
        yes_count (int): Number of YES contracts owned at the time of settlement.
        yes_total_cost (int): Total cost basis of all YES contracts in cents.
        no_count (int): Number of NO contracts owned at the time of settlement.
        no_total_cost (int): Total cost basis of all NO contracts in cents.
        revenue (int): Total revenue earned from this settlement in cents (winning contracts pay out 100 cents each).
        settled_time (datetime.datetime): Timestamp when the market was settled and payouts were processed.
        value (Union[None, Unset, int]): Payout of a single yes contract in cents.
    """

    ticker: str
    market_result: SettlementMarketResult
    yes_count: int
    yes_total_cost: int
    no_count: int
    no_total_cost: int
    revenue: int
    settled_time: datetime.datetime
    value: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticker = self.ticker

        market_result = self.market_result.value

        yes_count = self.yes_count

        yes_total_cost = self.yes_total_cost

        no_count = self.no_count

        no_total_cost = self.no_total_cost

        revenue = self.revenue

        settled_time = self.settled_time.isoformat()

        value: Union[None, Unset, int]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticker": ticker,
                "market_result": market_result,
                "yes_count": yes_count,
                "yes_total_cost": yes_total_cost,
                "no_count": no_count,
                "no_total_cost": no_total_cost,
                "revenue": revenue,
                "settled_time": settled_time,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ticker = d.pop("ticker")

        market_result = SettlementMarketResult(d.pop("market_result"))

        yes_count = d.pop("yes_count")

        yes_total_cost = d.pop("yes_total_cost")

        no_count = d.pop("no_count")

        no_total_cost = d.pop("no_total_cost")

        revenue = d.pop("revenue")

        settled_time = isoparse(d.pop("settled_time"))

        def _parse_value(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        value = _parse_value(d.pop("value", UNSET))

        settlement = cls(
            ticker=ticker,
            market_result=market_result,
            yes_count=yes_count,
            yes_total_cost=yes_total_cost,
            no_count=no_count,
            no_total_cost=no_total_cost,
            revenue=revenue,
            settled_time=settled_time,
            value=value,
        )

        settlement.additional_properties = d
        return settlement

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
