from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelGetEventForecastPercentilesHistoryResponseForecastHistoryItemPercentilePointsItem")


@_attrs_define
class ModelGetEventForecastPercentilesHistoryResponseForecastHistoryItemPercentilePointsItem:
    """
    Attributes:
        formatted_forecast (Union[Unset, str]):
        numerical_forecast (Union[Unset, Any]):
        percentile (Union[Unset, int]):
        raw_numerical_forecast (Union[Unset, Any]):
    """

    formatted_forecast: Union[Unset, str] = UNSET
    numerical_forecast: Union[Unset, Any] = UNSET
    percentile: Union[Unset, int] = UNSET
    raw_numerical_forecast: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        formatted_forecast = self.formatted_forecast

        numerical_forecast = self.numerical_forecast

        percentile = self.percentile

        raw_numerical_forecast = self.raw_numerical_forecast

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if formatted_forecast is not UNSET:
            field_dict["formatted_forecast"] = formatted_forecast
        if numerical_forecast is not UNSET:
            field_dict["numerical_forecast"] = numerical_forecast
        if percentile is not UNSET:
            field_dict["percentile"] = percentile
        if raw_numerical_forecast is not UNSET:
            field_dict["raw_numerical_forecast"] = raw_numerical_forecast

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        formatted_forecast = d.pop("formatted_forecast", UNSET)

        numerical_forecast = d.pop("numerical_forecast", UNSET)

        percentile = d.pop("percentile", UNSET)

        raw_numerical_forecast = d.pop("raw_numerical_forecast", UNSET)

        model_get_event_forecast_percentiles_history_response_forecast_history_item_percentile_points_item = cls(
            formatted_forecast=formatted_forecast,
            numerical_forecast=numerical_forecast,
            percentile=percentile,
            raw_numerical_forecast=raw_numerical_forecast,
        )

        model_get_event_forecast_percentiles_history_response_forecast_history_item_percentile_points_item.additional_properties = d
        return model_get_event_forecast_percentiles_history_response_forecast_history_item_percentile_points_item

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
