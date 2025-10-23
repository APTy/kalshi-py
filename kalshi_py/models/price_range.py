from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PriceRange")


@_attrs_define
class PriceRange:
    """
    Attributes:
        end (Union[Unset, str]): Fixed point representation of a subpenny dollar amount e.g. 1.2345 indicates $1.23 and
            45/100 of a cent. Example: 0.2300.
        start (Union[Unset, str]): Fixed point representation of a subpenny dollar amount e.g. 1.2345 indicates $1.23
            and 45/100 of a cent. Example: 0.2300.
        step (Union[Unset, str]): Fixed point representation of a subpenny dollar amount e.g. 1.2345 indicates $1.23 and
            45/100 of a cent. Example: 0.2300.
    """

    end: Union[Unset, str] = UNSET
    start: Union[Unset, str] = UNSET
    step: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end

        start = self.start

        step = self.step

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end is not UNSET:
            field_dict["end"] = end
        if start is not UNSET:
            field_dict["start"] = start
        if step is not UNSET:
            field_dict["step"] = step

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end = d.pop("end", UNSET)

        start = d.pop("start", UNSET)

        step = d.pop("step", UNSET)

        price_range = cls(
            end=end,
            start=start,
            step=step,
        )

        price_range.additional_properties = d
        return price_range

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
