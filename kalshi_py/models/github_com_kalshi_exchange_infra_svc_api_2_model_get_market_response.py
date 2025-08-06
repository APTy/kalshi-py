from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_market import (
        GithubComKalshiExchangeInfraSvcApi2ModelMarket,
    )


T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelGetMarketResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelGetMarketResponse:
    """
    Attributes:
        market (Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelMarket]): Contains information about a market
    """

    market: Union[Unset, "GithubComKalshiExchangeInfraSvcApi2ModelMarket"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        market: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.market, Unset):
            market = self.market.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if market is not UNSET:
            field_dict["market"] = market

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_market import (
            GithubComKalshiExchangeInfraSvcApi2ModelMarket,
        )

        d = dict(src_dict)
        _market = d.pop("market", UNSET)
        market: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = GithubComKalshiExchangeInfraSvcApi2ModelMarket.from_dict(_market)

        github_com_kalshi_exchange_infra_svc_api_2_model_get_market_response = cls(
            market=market,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_get_market_response.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_get_market_response

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
