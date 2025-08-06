from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_get_multivariate_event_collection_lookup_history_response_lookup_points_item import (
        GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionLookupHistoryResponseLookupPointsItem,
    )


T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionLookupHistoryResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionLookupHistoryResponse:
    """
    Attributes:
        lookup_points (Union[Unset, list['GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionLookupHi
            storyResponseLookupPointsItem']]): List of recent lookup points in the collection.
    """

    lookup_points: Union[
        Unset,
        list[
            "GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionLookupHistoryResponseLookupPointsItem"
        ],
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lookup_points: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.lookup_points, Unset):
            lookup_points = []
            for lookup_points_item_data in self.lookup_points:
                lookup_points_item = lookup_points_item_data.to_dict()
                lookup_points.append(lookup_points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lookup_points is not UNSET:
            field_dict["lookup_points"] = lookup_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_get_multivariate_event_collection_lookup_history_response_lookup_points_item import (
            GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionLookupHistoryResponseLookupPointsItem,
        )

        d = dict(src_dict)
        lookup_points = []
        _lookup_points = d.pop("lookup_points", UNSET)
        for lookup_points_item_data in _lookup_points or []:
            lookup_points_item = GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionLookupHistoryResponseLookupPointsItem.from_dict(
                lookup_points_item_data
            )

            lookup_points.append(lookup_points_item)

        github_com_kalshi_exchange_infra_svc_api_2_model_get_multivariate_event_collection_lookup_history_response = (
            cls(
                lookup_points=lookup_points,
            )
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_get_multivariate_event_collection_lookup_history_response.additional_properties = d
        return (
            github_com_kalshi_exchange_infra_svc_api_2_model_get_multivariate_event_collection_lookup_history_response
        )

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
