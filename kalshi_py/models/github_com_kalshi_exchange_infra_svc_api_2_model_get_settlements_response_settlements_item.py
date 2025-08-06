from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_get_settlements_response_settlements_item_market_result import (
    GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponseSettlementsItemMarketResult,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponseSettlementsItem")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponseSettlementsItem:
    """
    Attributes:
        market_result (Union[Unset,
            GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponseSettlementsItemMarketResult]): The outcome of the
            market settlement ('yes' or 'no').
        no_count (Union[Unset, int]): Number of NO contracts owned at the time of settlement.
        no_total_cost (Union[Unset, int]):
        revenue (Union[Unset, int]):
        settled_time (Union[Unset, Any]):
        ticker (Union[Unset, str]): The ticker symbol of the market that was settled.
        yes_count (Union[Unset, int]): Number of YES contracts owned at the time of settlement.
        yes_total_cost (Union[Unset, int]):
    """

    market_result: Union[
        Unset, GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponseSettlementsItemMarketResult
    ] = UNSET
    no_count: Union[Unset, int] = UNSET
    no_total_cost: Union[Unset, int] = UNSET
    revenue: Union[Unset, int] = UNSET
    settled_time: Union[Unset, Any] = UNSET
    ticker: Union[Unset, str] = UNSET
    yes_count: Union[Unset, int] = UNSET
    yes_total_cost: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        market_result: Union[Unset, str] = UNSET
        if not isinstance(self.market_result, Unset):
            market_result = self.market_result.value

        no_count = self.no_count

        no_total_cost = self.no_total_cost

        revenue = self.revenue

        settled_time = self.settled_time

        ticker = self.ticker

        yes_count = self.yes_count

        yes_total_cost = self.yes_total_cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if market_result is not UNSET:
            field_dict["market_result"] = market_result
        if no_count is not UNSET:
            field_dict["no_count"] = no_count
        if no_total_cost is not UNSET:
            field_dict["no_total_cost"] = no_total_cost
        if revenue is not UNSET:
            field_dict["revenue"] = revenue
        if settled_time is not UNSET:
            field_dict["settled_time"] = settled_time
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if yes_count is not UNSET:
            field_dict["yes_count"] = yes_count
        if yes_total_cost is not UNSET:
            field_dict["yes_total_cost"] = yes_total_cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _market_result = d.pop("market_result", UNSET)
        market_result: Union[
            Unset, GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponseSettlementsItemMarketResult
        ]
        if isinstance(_market_result, Unset):
            market_result = UNSET
        else:
            market_result = GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponseSettlementsItemMarketResult(
                _market_result
            )

        no_count = d.pop("no_count", UNSET)

        no_total_cost = d.pop("no_total_cost", UNSET)

        revenue = d.pop("revenue", UNSET)

        settled_time = d.pop("settled_time", UNSET)

        ticker = d.pop("ticker", UNSET)

        yes_count = d.pop("yes_count", UNSET)

        yes_total_cost = d.pop("yes_total_cost", UNSET)

        github_com_kalshi_exchange_infra_svc_api_2_model_get_settlements_response_settlements_item = cls(
            market_result=market_result,
            no_count=no_count,
            no_total_cost=no_total_cost,
            revenue=revenue,
            settled_time=settled_time,
            ticker=ticker,
            yes_count=yes_count,
            yes_total_cost=yes_total_cost,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_get_settlements_response_settlements_item.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_get_settlements_response_settlements_item

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
