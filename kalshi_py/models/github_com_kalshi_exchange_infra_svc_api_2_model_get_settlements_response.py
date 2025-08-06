from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_get_settlements_response_settlements_item import (
        GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponseSettlementsItem,
    )


T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponse:
    """
    Attributes:
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in the pagination. Use
            the value returned here in the cursor query parameter for this end-point to get the next page containing limit
            records. An empty value of this field indicates there is no next page.
        settlements (Union[Unset,
            list['GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponseSettlementsItem']]): Settlement summaries
            for all markets the user participated in.
    """

    cursor: Union[Unset, str] = UNSET
    settlements: Union[Unset, list["GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponseSettlementsItem"]] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursor = self.cursor

        settlements: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.settlements, Unset):
            settlements = []
            for settlements_item_data in self.settlements:
                settlements_item = settlements_item_data.to_dict()
                settlements.append(settlements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if settlements is not UNSET:
            field_dict["settlements"] = settlements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_get_settlements_response_settlements_item import (
            GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponseSettlementsItem,
        )

        d = dict(src_dict)
        cursor = d.pop("cursor", UNSET)

        settlements = []
        _settlements = d.pop("settlements", UNSET)
        for settlements_item_data in _settlements or []:
            settlements_item = GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponseSettlementsItem.from_dict(
                settlements_item_data
            )

            settlements.append(settlements_item)

        github_com_kalshi_exchange_infra_svc_api_2_model_get_settlements_response = cls(
            cursor=cursor,
            settlements=settlements,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_get_settlements_response.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_get_settlements_response

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
