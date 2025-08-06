from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_get_event_metadata_response_settlement_sources_item import (
        GithubComKalshiExchangeInfraSvcApi2ModelGetEventMetadataResponseSettlementSourcesItem,
    )


T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelGetEventMetadataResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelGetEventMetadataResponse:
    """
    Attributes:
        image_url (Union[Unset, str]):
        settlement_sources (Union[Unset,
            list['GithubComKalshiExchangeInfraSvcApi2ModelGetEventMetadataResponseSettlementSourcesItem']]):
    """

    image_url: Union[Unset, str] = UNSET
    settlement_sources: Union[
        Unset, list["GithubComKalshiExchangeInfraSvcApi2ModelGetEventMetadataResponseSettlementSourcesItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_url = self.image_url

        settlement_sources: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.settlement_sources, Unset):
            settlement_sources = []
            for settlement_sources_item_data in self.settlement_sources:
                settlement_sources_item = settlement_sources_item_data.to_dict()
                settlement_sources.append(settlement_sources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if settlement_sources is not UNSET:
            field_dict["settlement_sources"] = settlement_sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_get_event_metadata_response_settlement_sources_item import (
            GithubComKalshiExchangeInfraSvcApi2ModelGetEventMetadataResponseSettlementSourcesItem,
        )

        d = dict(src_dict)
        image_url = d.pop("image_url", UNSET)

        settlement_sources = []
        _settlement_sources = d.pop("settlement_sources", UNSET)
        for settlement_sources_item_data in _settlement_sources or []:
            settlement_sources_item = (
                GithubComKalshiExchangeInfraSvcApi2ModelGetEventMetadataResponseSettlementSourcesItem.from_dict(
                    settlement_sources_item_data
                )
            )

            settlement_sources.append(settlement_sources_item)

        github_com_kalshi_exchange_infra_svc_api_2_model_get_event_metadata_response = cls(
            image_url=image_url,
            settlement_sources=settlement_sources,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_get_event_metadata_response.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_get_event_metadata_response

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
