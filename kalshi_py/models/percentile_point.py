from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PercentilePoint")


@_attrs_define
class PercentilePoint:
    """
    Attributes:
        percentile (int): The percentile value (0-10000).
        raw_numerical_forecast (float): The raw numerical forecast value.
        numerical_forecast (float): The processed numerical forecast value.
        formatted_forecast (str): The human-readable formatted forecast value.
    """

    percentile: int
    raw_numerical_forecast: float
    numerical_forecast: float
    formatted_forecast: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        percentile = self.percentile

        raw_numerical_forecast = self.raw_numerical_forecast

        numerical_forecast = self.numerical_forecast

        formatted_forecast = self.formatted_forecast

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "percentile": percentile,
                "raw_numerical_forecast": raw_numerical_forecast,
                "numerical_forecast": numerical_forecast,
                "formatted_forecast": formatted_forecast,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        percentile = d.pop("percentile")

        raw_numerical_forecast = d.pop("raw_numerical_forecast")

        numerical_forecast = d.pop("numerical_forecast")

        formatted_forecast = d.pop("formatted_forecast")

        percentile_point = cls(
            percentile=percentile,
            raw_numerical_forecast=raw_numerical_forecast,
            numerical_forecast=numerical_forecast,
            formatted_forecast=formatted_forecast,
        )

        percentile_point.additional_properties = d
        return percentile_point

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
