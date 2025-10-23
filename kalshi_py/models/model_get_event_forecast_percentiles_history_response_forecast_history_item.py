from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_get_event_forecast_percentiles_history_response_forecast_history_item_percentile_points_item import (
        ModelGetEventForecastPercentilesHistoryResponseForecastHistoryItemPercentilePointsItem,
    )


T = TypeVar("T", bound="ModelGetEventForecastPercentilesHistoryResponseForecastHistoryItem")


@_attrs_define
class ModelGetEventForecastPercentilesHistoryResponseForecastHistoryItem:
    """
    Attributes:
        end_period_ts (Union[Unset, int]):
        event_ticker (Union[Unset, str]):
        percentile_points (Union[Unset,
            list['ModelGetEventForecastPercentilesHistoryResponseForecastHistoryItemPercentilePointsItem']]):
        period_interval (Union[Unset, int]):
    """

    end_period_ts: Union[Unset, int] = UNSET
    event_ticker: Union[Unset, str] = UNSET
    percentile_points: Union[
        Unset, list["ModelGetEventForecastPercentilesHistoryResponseForecastHistoryItemPercentilePointsItem"]
    ] = UNSET
    period_interval: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_period_ts = self.end_period_ts

        event_ticker = self.event_ticker

        percentile_points: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.percentile_points, Unset):
            percentile_points = []
            for percentile_points_item_data in self.percentile_points:
                percentile_points_item = percentile_points_item_data.to_dict()
                percentile_points.append(percentile_points_item)

        period_interval = self.period_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_period_ts is not UNSET:
            field_dict["end_period_ts"] = end_period_ts
        if event_ticker is not UNSET:
            field_dict["event_ticker"] = event_ticker
        if percentile_points is not UNSET:
            field_dict["percentile_points"] = percentile_points
        if period_interval is not UNSET:
            field_dict["period_interval"] = period_interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_get_event_forecast_percentiles_history_response_forecast_history_item_percentile_points_item import (
            ModelGetEventForecastPercentilesHistoryResponseForecastHistoryItemPercentilePointsItem,
        )

        d = dict(src_dict)
        end_period_ts = d.pop("end_period_ts", UNSET)

        event_ticker = d.pop("event_ticker", UNSET)

        percentile_points = []
        _percentile_points = d.pop("percentile_points", UNSET)
        for percentile_points_item_data in _percentile_points or []:
            percentile_points_item = (
                ModelGetEventForecastPercentilesHistoryResponseForecastHistoryItemPercentilePointsItem.from_dict(
                    percentile_points_item_data
                )
            )

            percentile_points.append(percentile_points_item)

        period_interval = d.pop("period_interval", UNSET)

        model_get_event_forecast_percentiles_history_response_forecast_history_item = cls(
            end_period_ts=end_period_ts,
            event_ticker=event_ticker,
            percentile_points=percentile_points,
            period_interval=period_interval,
        )

        model_get_event_forecast_percentiles_history_response_forecast_history_item.additional_properties = d
        return model_get_event_forecast_percentiles_history_response_forecast_history_item

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
