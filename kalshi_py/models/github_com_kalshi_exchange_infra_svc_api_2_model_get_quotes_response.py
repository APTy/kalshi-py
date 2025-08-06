from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_get_quotes_response_quotes_item import (
        GithubComKalshiExchangeInfraSvcApi2ModelGetQuotesResponseQuotesItem,
    )


T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelGetQuotesResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelGetQuotesResponse:
    """
    Attributes:
        cursor (Union[Unset, str]): Cursor for pagination to get the next page of results.
        quotes (Union[Unset, list['GithubComKalshiExchangeInfraSvcApi2ModelGetQuotesResponseQuotesItem']]): List of
            quotes matching the query criteria.
    """

    cursor: Union[Unset, str] = UNSET
    quotes: Union[Unset, list["GithubComKalshiExchangeInfraSvcApi2ModelGetQuotesResponseQuotesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursor = self.cursor

        quotes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.quotes, Unset):
            quotes = []
            for quotes_item_data in self.quotes:
                quotes_item = quotes_item_data.to_dict()
                quotes.append(quotes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if quotes is not UNSET:
            field_dict["quotes"] = quotes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_get_quotes_response_quotes_item import (
            GithubComKalshiExchangeInfraSvcApi2ModelGetQuotesResponseQuotesItem,
        )

        d = dict(src_dict)
        cursor = d.pop("cursor", UNSET)

        quotes = []
        _quotes = d.pop("quotes", UNSET)
        for quotes_item_data in _quotes or []:
            quotes_item = GithubComKalshiExchangeInfraSvcApi2ModelGetQuotesResponseQuotesItem.from_dict(
                quotes_item_data
            )

            quotes.append(quotes_item)

        github_com_kalshi_exchange_infra_svc_api_2_model_get_quotes_response = cls(
            cursor=cursor,
            quotes=quotes,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_get_quotes_response.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_get_quotes_response

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
