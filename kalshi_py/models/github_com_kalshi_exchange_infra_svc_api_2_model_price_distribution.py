from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelPriceDistribution")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelPriceDistribution:
    """
    Attributes:
        close (Union[Unset, int]):
        close_dollars (Union[Unset, list[int]]):
        high (Union[Unset, int]):
        high_dollars (Union[Unset, list[int]]):
        low (Union[Unset, int]):
        low_dollars (Union[Unset, list[int]]):
        mean (Union[Unset, int]):
        mean_dollars (Union[Unset, list[int]]):
        open_ (Union[Unset, int]):
        open_dollars (Union[Unset, list[int]]):
        previous (Union[Unset, int]):
        previous_dollars (Union[Unset, list[int]]):
    """

    close: Union[Unset, int] = UNSET
    close_dollars: Union[Unset, list[int]] = UNSET
    high: Union[Unset, int] = UNSET
    high_dollars: Union[Unset, list[int]] = UNSET
    low: Union[Unset, int] = UNSET
    low_dollars: Union[Unset, list[int]] = UNSET
    mean: Union[Unset, int] = UNSET
    mean_dollars: Union[Unset, list[int]] = UNSET
    open_: Union[Unset, int] = UNSET
    open_dollars: Union[Unset, list[int]] = UNSET
    previous: Union[Unset, int] = UNSET
    previous_dollars: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        close = self.close

        close_dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.close_dollars, Unset):
            close_dollars = self.close_dollars

        high = self.high

        high_dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.high_dollars, Unset):
            high_dollars = self.high_dollars

        low = self.low

        low_dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.low_dollars, Unset):
            low_dollars = self.low_dollars

        mean = self.mean

        mean_dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.mean_dollars, Unset):
            mean_dollars = self.mean_dollars

        open_ = self.open_

        open_dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.open_dollars, Unset):
            open_dollars = self.open_dollars

        previous = self.previous

        previous_dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.previous_dollars, Unset):
            previous_dollars = self.previous_dollars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if close is not UNSET:
            field_dict["close"] = close
        if close_dollars is not UNSET:
            field_dict["close_dollars"] = close_dollars
        if high is not UNSET:
            field_dict["high"] = high
        if high_dollars is not UNSET:
            field_dict["high_dollars"] = high_dollars
        if low is not UNSET:
            field_dict["low"] = low
        if low_dollars is not UNSET:
            field_dict["low_dollars"] = low_dollars
        if mean is not UNSET:
            field_dict["mean"] = mean
        if mean_dollars is not UNSET:
            field_dict["mean_dollars"] = mean_dollars
        if open_ is not UNSET:
            field_dict["open"] = open_
        if open_dollars is not UNSET:
            field_dict["open_dollars"] = open_dollars
        if previous is not UNSET:
            field_dict["previous"] = previous
        if previous_dollars is not UNSET:
            field_dict["previous_dollars"] = previous_dollars

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        close = d.pop("close", UNSET)

        close_dollars = cast(list[int], d.pop("close_dollars", UNSET))

        high = d.pop("high", UNSET)

        high_dollars = cast(list[int], d.pop("high_dollars", UNSET))

        low = d.pop("low", UNSET)

        low_dollars = cast(list[int], d.pop("low_dollars", UNSET))

        mean = d.pop("mean", UNSET)

        mean_dollars = cast(list[int], d.pop("mean_dollars", UNSET))

        open_ = d.pop("open", UNSET)

        open_dollars = cast(list[int], d.pop("open_dollars", UNSET))

        previous = d.pop("previous", UNSET)

        previous_dollars = cast(list[int], d.pop("previous_dollars", UNSET))

        github_com_kalshi_exchange_infra_svc_api_2_model_price_distribution = cls(
            close=close,
            close_dollars=close_dollars,
            high=high,
            high_dollars=high_dollars,
            low=low,
            low_dollars=low_dollars,
            mean=mean,
            mean_dollars=mean_dollars,
            open_=open_,
            open_dollars=open_dollars,
            previous=previous,
            previous_dollars=previous_dollars,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_price_distribution.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_price_distribution

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
