from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_fill import (
        GithubComKalshiExchangeInfraSvcApi2ModelFill,
    )


T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelGetFillsResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelGetFillsResponse:
    """
    Attributes:
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in the pagination. Use
            the value returned here in the cursor query parameter for this end-point to get the next page containing limit
            records. An empty value of this field indicates there is no next page.
        fills (Union[Unset, list['GithubComKalshiExchangeInfraSvcApi2ModelFill']]):
    """

    cursor: Union[Unset, str] = UNSET
    fills: Union[Unset, list["GithubComKalshiExchangeInfraSvcApi2ModelFill"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursor = self.cursor

        fills: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fills, Unset):
            fills = []
            for componentsschemasgithub_com_kalshi_exchange_infra_svc_api_2_model_fills_item_data in self.fills:
                componentsschemasgithub_com_kalshi_exchange_infra_svc_api_2_model_fills_item = (
                    componentsschemasgithub_com_kalshi_exchange_infra_svc_api_2_model_fills_item_data.to_dict()
                )
                fills.append(componentsschemasgithub_com_kalshi_exchange_infra_svc_api_2_model_fills_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if fills is not UNSET:
            field_dict["fills"] = fills

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_fill import (
            GithubComKalshiExchangeInfraSvcApi2ModelFill,
        )

        d = dict(src_dict)
        cursor = d.pop("cursor", UNSET)

        fills = []
        _fills = d.pop("fills", UNSET)
        for componentsschemasgithub_com_kalshi_exchange_infra_svc_api_2_model_fills_item_data in _fills or []:
            componentsschemasgithub_com_kalshi_exchange_infra_svc_api_2_model_fills_item = (
                GithubComKalshiExchangeInfraSvcApi2ModelFill.from_dict(
                    componentsschemasgithub_com_kalshi_exchange_infra_svc_api_2_model_fills_item_data
                )
            )

            fills.append(componentsschemasgithub_com_kalshi_exchange_infra_svc_api_2_model_fills_item)

        github_com_kalshi_exchange_infra_svc_api_2_model_get_fills_response = cls(
            cursor=cursor,
            fills=fills,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_get_fills_response.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_get_fills_response

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
