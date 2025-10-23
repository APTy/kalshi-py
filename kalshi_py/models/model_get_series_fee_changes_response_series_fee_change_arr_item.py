import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelGetSeriesFeeChangesResponseSeriesFeeChangeArrItem")


@_attrs_define
class ModelGetSeriesFeeChangesResponseSeriesFeeChangeArrItem:
    """
    Attributes:
        fee_multiplier (Union[Unset, float]):
        fee_type (Union[Unset, str]):
        id (Union[Unset, str]):
        scheduled_ts (Union[Unset, datetime.datetime]):
        series_ticker (Union[Unset, str]):
    """

    fee_multiplier: Union[Unset, float] = UNSET
    fee_type: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    scheduled_ts: Union[Unset, datetime.datetime] = UNSET
    series_ticker: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fee_multiplier = self.fee_multiplier

        fee_type = self.fee_type

        id = self.id

        scheduled_ts: Union[Unset, str] = UNSET
        if not isinstance(self.scheduled_ts, Unset):
            scheduled_ts = self.scheduled_ts.isoformat()

        series_ticker = self.series_ticker

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fee_multiplier is not UNSET:
            field_dict["fee_multiplier"] = fee_multiplier
        if fee_type is not UNSET:
            field_dict["fee_type"] = fee_type
        if id is not UNSET:
            field_dict["id"] = id
        if scheduled_ts is not UNSET:
            field_dict["scheduled_ts"] = scheduled_ts
        if series_ticker is not UNSET:
            field_dict["series_ticker"] = series_ticker

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fee_multiplier = d.pop("fee_multiplier", UNSET)

        fee_type = d.pop("fee_type", UNSET)

        id = d.pop("id", UNSET)

        _scheduled_ts = d.pop("scheduled_ts", UNSET)
        scheduled_ts: Union[Unset, datetime.datetime]
        if isinstance(_scheduled_ts, Unset):
            scheduled_ts = UNSET
        else:
            scheduled_ts = isoparse(_scheduled_ts)

        series_ticker = d.pop("series_ticker", UNSET)

        model_get_series_fee_changes_response_series_fee_change_arr_item = cls(
            fee_multiplier=fee_multiplier,
            fee_type=fee_type,
            id=id,
            scheduled_ts=scheduled_ts,
            series_ticker=series_ticker,
        )

        model_get_series_fee_changes_response_series_fee_change_arr_item.additional_properties = d
        return model_get_series_fee_changes_response_series_fee_change_arr_item

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
