from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_tags_for_series_categories_response_tags_by_categories import (
        GetTagsForSeriesCategoriesResponseTagsByCategories,
    )


T = TypeVar("T", bound="GetTagsForSeriesCategoriesResponse")


@_attrs_define
class GetTagsForSeriesCategoriesResponse:
    """
    Attributes:
        tags_by_categories (GetTagsForSeriesCategoriesResponseTagsByCategories): Mapping of series categories to their
            associated tags
    """

    tags_by_categories: "GetTagsForSeriesCategoriesResponseTagsByCategories"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tags_by_categories = self.tags_by_categories.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tags_by_categories": tags_by_categories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_tags_for_series_categories_response_tags_by_categories import (
            GetTagsForSeriesCategoriesResponseTagsByCategories,
        )

        d = dict(src_dict)
        tags_by_categories = GetTagsForSeriesCategoriesResponseTagsByCategories.from_dict(d.pop("tags_by_categories"))

        get_tags_for_series_categories_response = cls(
            tags_by_categories=tags_by_categories,
        )

        get_tags_for_series_categories_response.additional_properties = d
        return get_tags_for_series_categories_response

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
