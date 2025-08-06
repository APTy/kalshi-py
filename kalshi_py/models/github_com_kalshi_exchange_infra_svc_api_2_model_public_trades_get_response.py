from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_public_trade import (
        GithubComKalshiExchangeInfraSvcApi2ModelPublicTrade,
    )


T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelPublicTradesGetResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelPublicTradesGetResponse:
    """
    Attributes:
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in the pagination. Use
            the value returned here in the cursor query parameter for this end-point to get the next page containing limit
            records. An empty value of this field indicates there is no next page.
        trades (Union[Unset, list['GithubComKalshiExchangeInfraSvcApi2ModelPublicTrade']]):
    """

    cursor: Union[Unset, str] = UNSET
    trades: Union[Unset, list["GithubComKalshiExchangeInfraSvcApi2ModelPublicTrade"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursor = self.cursor

        trades: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.trades, Unset):
            trades = []
            for (
                componentsschemasgithub_com_kalshi_exchange_infra_svc_api_2_model_public_trade_list_item_data
            ) in self.trades:
                componentsschemasgithub_com_kalshi_exchange_infra_svc_api_2_model_public_trade_list_item = componentsschemasgithub_com_kalshi_exchange_infra_svc_api_2_model_public_trade_list_item_data.to_dict()
                trades.append(componentsschemasgithub_com_kalshi_exchange_infra_svc_api_2_model_public_trade_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if trades is not UNSET:
            field_dict["trades"] = trades

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_public_trade import (
            GithubComKalshiExchangeInfraSvcApi2ModelPublicTrade,
        )

        d = dict(src_dict)
        cursor = d.pop("cursor", UNSET)

        trades = []
        _trades = d.pop("trades", UNSET)
        for componentsschemasgithub_com_kalshi_exchange_infra_svc_api_2_model_public_trade_list_item_data in (
            _trades or []
        ):
            componentsschemasgithub_com_kalshi_exchange_infra_svc_api_2_model_public_trade_list_item = (
                GithubComKalshiExchangeInfraSvcApi2ModelPublicTrade.from_dict(
                    componentsschemasgithub_com_kalshi_exchange_infra_svc_api_2_model_public_trade_list_item_data
                )
            )

            trades.append(componentsschemasgithub_com_kalshi_exchange_infra_svc_api_2_model_public_trade_list_item)

        github_com_kalshi_exchange_infra_svc_api_2_model_public_trades_get_response = cls(
            cursor=cursor,
            trades=trades,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_public_trades_get_response.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_public_trades_get_response

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
