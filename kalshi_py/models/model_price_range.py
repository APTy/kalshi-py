from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelPriceRange")


@_attrs_define
class ModelPriceRange:
    """Represents a range of prices with a specific tick size.

    Example:
        {'start': '0.00', 'end': '1.00', 'step': '0.01'}

    Attributes:
        start (str): Starting price for this range in dollars. Example: 0.00.
        end (str): Ending price for this range in dollars. Example: 1.00.
        step (str): Price step/tick size for this range in dollars. Example: 0.01.
    """

    start: str
    end: str
    step: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start

        end = self.end

        step = self.step

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "end": end,
                "step": step,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start = d.pop("start")

        end = d.pop("end")

        step = d.pop("step")

        model_price_range = cls(
            start=start,
            end=end,
            step=step,
        )

        model_price_range.additional_properties = d
        return model_price_range

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
