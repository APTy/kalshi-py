from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PriceLevelDollars")


@_attrs_define
class PriceLevelDollars:
    """
    Attributes:
        count (Union[Unset, int]):
        dollars (Union[Unset, list[int]]):
    """

    count: Union[Unset, int] = UNSET
    dollars: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        dollars: Union[Unset, list[int]] = UNSET
        if not isinstance(self.dollars, Unset):
            dollars = self.dollars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["Count"] = count
        if dollars is not UNSET:
            field_dict["Dollars"] = dollars

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("Count", UNSET)

        dollars = cast(list[int], d.pop("Dollars", UNSET))

        price_level_dollars = cls(
            count=count,
            dollars=dollars,
        )

        price_level_dollars.additional_properties = d
        return price_level_dollars

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
