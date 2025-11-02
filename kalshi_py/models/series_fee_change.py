import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.series_fee_change_fee_type import SeriesFeeChangeFeeType

T = TypeVar("T", bound="SeriesFeeChange")


@_attrs_define
class SeriesFeeChange:
    """
    Attributes:
        id (str): Unique identifier for this fee change
        series_ticker (str): Series ticker this fee change applies to
        fee_type (SeriesFeeChangeFeeType): New fee type for the series
        fee_multiplier (float): New fee multiplier for the series
        scheduled_ts (datetime.datetime): Timestamp when this fee change is scheduled to take effect
    """

    id: str
    series_ticker: str
    fee_type: SeriesFeeChangeFeeType
    fee_multiplier: float
    scheduled_ts: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        series_ticker = self.series_ticker

        fee_type = self.fee_type.value

        fee_multiplier = self.fee_multiplier

        scheduled_ts = self.scheduled_ts.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "series_ticker": series_ticker,
                "fee_type": fee_type,
                "fee_multiplier": fee_multiplier,
                "scheduled_ts": scheduled_ts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        series_ticker = d.pop("series_ticker")

        fee_type = SeriesFeeChangeFeeType(d.pop("fee_type"))

        fee_multiplier = d.pop("fee_multiplier")

        scheduled_ts = isoparse(d.pop("scheduled_ts"))

        series_fee_change = cls(
            id=id,
            series_ticker=series_ticker,
            fee_type=fee_type,
            fee_multiplier=fee_multiplier,
            scheduled_ts=scheduled_ts,
        )

        series_fee_change.additional_properties = d
        return series_fee_change

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
