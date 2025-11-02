from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.percentile_point import PercentilePoint


T = TypeVar("T", bound="ForecastPercentilesPoint")


@_attrs_define
class ForecastPercentilesPoint:
    """
    Attributes:
        event_ticker (str): The event ticker this forecast is for.
        end_period_ts (int): Unix timestamp for the inclusive end of the forecast period.
        period_interval (int): Length of the forecast period in minutes.
        percentile_points (list['PercentilePoint']): Array of forecast values at different percentiles.
    """

    event_ticker: str
    end_period_ts: int
    period_interval: int
    percentile_points: list["PercentilePoint"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_ticker = self.event_ticker

        end_period_ts = self.end_period_ts

        period_interval = self.period_interval

        percentile_points = []
        for percentile_points_item_data in self.percentile_points:
            percentile_points_item = percentile_points_item_data.to_dict()
            percentile_points.append(percentile_points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_ticker": event_ticker,
                "end_period_ts": end_period_ts,
                "period_interval": period_interval,
                "percentile_points": percentile_points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.percentile_point import PercentilePoint

        d = dict(src_dict)
        event_ticker = d.pop("event_ticker")

        end_period_ts = d.pop("end_period_ts")

        period_interval = d.pop("period_interval")

        percentile_points = []
        _percentile_points = d.pop("percentile_points")
        for percentile_points_item_data in _percentile_points:
            percentile_points_item = PercentilePoint.from_dict(percentile_points_item_data)

            percentile_points.append(percentile_points_item)

        forecast_percentiles_point = cls(
            event_ticker=event_ticker,
            end_period_ts=end_period_ts,
            period_interval=period_interval,
            percentile_points=percentile_points,
        )

        forecast_percentiles_point.additional_properties = d
        return forecast_percentiles_point

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
