from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.forecast_percentiles_point import ForecastPercentilesPoint


T = TypeVar("T", bound="GetEventForecastPercentilesHistoryResponse")


@_attrs_define
class GetEventForecastPercentilesHistoryResponse:
    """
    Attributes:
        forecast_history (list['ForecastPercentilesPoint']): Array of forecast percentile data points over time.
    """

    forecast_history: list["ForecastPercentilesPoint"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        forecast_history = []
        for forecast_history_item_data in self.forecast_history:
            forecast_history_item = forecast_history_item_data.to_dict()
            forecast_history.append(forecast_history_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "forecast_history": forecast_history,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.forecast_percentiles_point import ForecastPercentilesPoint

        d = dict(src_dict)
        forecast_history = []
        _forecast_history = d.pop("forecast_history")
        for forecast_history_item_data in _forecast_history:
            forecast_history_item = ForecastPercentilesPoint.from_dict(forecast_history_item_data)

            forecast_history.append(forecast_history_item)

        get_event_forecast_percentiles_history_response = cls(
            forecast_history=forecast_history,
        )

        get_event_forecast_percentiles_history_response.additional_properties = d
        return get_event_forecast_percentiles_history_response

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
