from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.lookup_point import LookupPoint


T = TypeVar("T", bound="GetMultivariateEventCollectionLookupHistoryResponse")


@_attrs_define
class GetMultivariateEventCollectionLookupHistoryResponse:
    """
    Attributes:
        lookup_points (list['LookupPoint']): List of recent lookup points in the collection.
    """

    lookup_points: list["LookupPoint"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lookup_points = []
        for lookup_points_item_data in self.lookup_points:
            lookup_points_item = lookup_points_item_data.to_dict()
            lookup_points.append(lookup_points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lookup_points": lookup_points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lookup_point import LookupPoint

        d = dict(src_dict)
        lookup_points = []
        _lookup_points = d.pop("lookup_points")
        for lookup_points_item_data in _lookup_points:
            lookup_points_item = LookupPoint.from_dict(lookup_points_item_data)

            lookup_points.append(lookup_points_item)

        get_multivariate_event_collection_lookup_history_response = cls(
            lookup_points=lookup_points,
        )

        get_multivariate_event_collection_lookup_history_response.additional_properties = d
        return get_multivariate_event_collection_lookup_history_response

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
