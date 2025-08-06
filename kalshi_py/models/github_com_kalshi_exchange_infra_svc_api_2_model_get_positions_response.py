from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_get_positions_response_event_positions_item import (
        GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponseEventPositionsItem,
    )
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_get_positions_response_market_positions_item import (
        GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponseMarketPositionsItem,
    )


T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponse:
    """
    Attributes:
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in the pagination. Use
            the value returned here in the cursor query parameter for this end-point to get the next page containing limit
            records. An empty value of this field indicates there is no next page.
        event_positions (Union[Unset,
            list['GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponseEventPositionsItem']]): List of event
            positions.
        market_positions (Union[Unset,
            list['GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponseMarketPositionsItem']]): List of market
            positions.
    """

    cursor: Union[Unset, str] = UNSET
    event_positions: Union[
        Unset, list["GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponseEventPositionsItem"]
    ] = UNSET
    market_positions: Union[
        Unset, list["GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponseMarketPositionsItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursor = self.cursor

        event_positions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.event_positions, Unset):
            event_positions = []
            for event_positions_item_data in self.event_positions:
                event_positions_item = event_positions_item_data.to_dict()
                event_positions.append(event_positions_item)

        market_positions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.market_positions, Unset):
            market_positions = []
            for market_positions_item_data in self.market_positions:
                market_positions_item = market_positions_item_data.to_dict()
                market_positions.append(market_positions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if event_positions is not UNSET:
            field_dict["event_positions"] = event_positions
        if market_positions is not UNSET:
            field_dict["market_positions"] = market_positions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_get_positions_response_event_positions_item import (
            GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponseEventPositionsItem,
        )
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_get_positions_response_market_positions_item import (
            GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponseMarketPositionsItem,
        )

        d = dict(src_dict)
        cursor = d.pop("cursor", UNSET)

        event_positions = []
        _event_positions = d.pop("event_positions", UNSET)
        for event_positions_item_data in _event_positions or []:
            event_positions_item = (
                GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponseEventPositionsItem.from_dict(
                    event_positions_item_data
                )
            )

            event_positions.append(event_positions_item)

        market_positions = []
        _market_positions = d.pop("market_positions", UNSET)
        for market_positions_item_data in _market_positions or []:
            market_positions_item = (
                GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponseMarketPositionsItem.from_dict(
                    market_positions_item_data
                )
            )

            market_positions.append(market_positions_item)

        github_com_kalshi_exchange_infra_svc_api_2_model_get_positions_response = cls(
            cursor=cursor,
            event_positions=event_positions,
            market_positions=market_positions,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_get_positions_response.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_get_positions_response

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
