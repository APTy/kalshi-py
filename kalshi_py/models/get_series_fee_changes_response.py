from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.series_fee_change import SeriesFeeChange


T = TypeVar("T", bound="GetSeriesFeeChangesResponse")


@_attrs_define
class GetSeriesFeeChangesResponse:
    """
    Attributes:
        series_fee_change_arr (list['SeriesFeeChange']):
    """

    series_fee_change_arr: list["SeriesFeeChange"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        series_fee_change_arr = []
        for series_fee_change_arr_item_data in self.series_fee_change_arr:
            series_fee_change_arr_item = series_fee_change_arr_item_data.to_dict()
            series_fee_change_arr.append(series_fee_change_arr_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "series_fee_change_arr": series_fee_change_arr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.series_fee_change import SeriesFeeChange

        d = dict(src_dict)
        series_fee_change_arr = []
        _series_fee_change_arr = d.pop("series_fee_change_arr")
        for series_fee_change_arr_item_data in _series_fee_change_arr:
            series_fee_change_arr_item = SeriesFeeChange.from_dict(series_fee_change_arr_item_data)

            series_fee_change_arr.append(series_fee_change_arr_item)

        get_series_fee_changes_response = cls(
            series_fee_change_arr=series_fee_change_arr,
        )

        get_series_fee_changes_response.additional_properties = d
        return get_series_fee_changes_response

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
