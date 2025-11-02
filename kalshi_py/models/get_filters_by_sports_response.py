from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_filters_by_sports_response_filters_by_sports import GetFiltersBySportsResponseFiltersBySports


T = TypeVar("T", bound="GetFiltersBySportsResponse")


@_attrs_define
class GetFiltersBySportsResponse:
    """
    Attributes:
        filters_by_sports (GetFiltersBySportsResponseFiltersBySports): Mapping of sports to their filter details
        sport_ordering (list[str]): Ordered list of sports for display
    """

    filters_by_sports: "GetFiltersBySportsResponseFiltersBySports"
    sport_ordering: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filters_by_sports = self.filters_by_sports.to_dict()

        sport_ordering = self.sport_ordering

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters_by_sports": filters_by_sports,
                "sport_ordering": sport_ordering,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_filters_by_sports_response_filters_by_sports import GetFiltersBySportsResponseFiltersBySports

        d = dict(src_dict)
        filters_by_sports = GetFiltersBySportsResponseFiltersBySports.from_dict(d.pop("filters_by_sports"))

        sport_ordering = cast(list[str], d.pop("sport_ordering"))

        get_filters_by_sports_response = cls(
            filters_by_sports=filters_by_sports,
            sport_ordering=sport_ordering,
        )

        get_filters_by_sports_response.additional_properties = d
        return get_filters_by_sports_response

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
