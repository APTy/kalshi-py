from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_get_series_fee_changes_response_series_fee_change_arr_item import (
        ModelGetSeriesFeeChangesResponseSeriesFeeChangeArrItem,
    )


T = TypeVar("T", bound="ModelGetSeriesFeeChangesResponse")


@_attrs_define
class ModelGetSeriesFeeChangesResponse:
    """
    Attributes:
        series_fee_change_arr (Union[Unset, list['ModelGetSeriesFeeChangesResponseSeriesFeeChangeArrItem']]):
    """

    series_fee_change_arr: Union[Unset, list["ModelGetSeriesFeeChangesResponseSeriesFeeChangeArrItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        series_fee_change_arr: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.series_fee_change_arr, Unset):
            series_fee_change_arr = []
            for series_fee_change_arr_item_data in self.series_fee_change_arr:
                series_fee_change_arr_item = series_fee_change_arr_item_data.to_dict()
                series_fee_change_arr.append(series_fee_change_arr_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if series_fee_change_arr is not UNSET:
            field_dict["series_fee_change_arr"] = series_fee_change_arr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_get_series_fee_changes_response_series_fee_change_arr_item import (
            ModelGetSeriesFeeChangesResponseSeriesFeeChangeArrItem,
        )

        d = dict(src_dict)
        series_fee_change_arr = []
        _series_fee_change_arr = d.pop("series_fee_change_arr", UNSET)
        for series_fee_change_arr_item_data in _series_fee_change_arr or []:
            series_fee_change_arr_item = ModelGetSeriesFeeChangesResponseSeriesFeeChangeArrItem.from_dict(
                series_fee_change_arr_item_data
            )

            series_fee_change_arr.append(series_fee_change_arr_item)

        model_get_series_fee_changes_response = cls(
            series_fee_change_arr=series_fee_change_arr,
        )

        model_get_series_fee_changes_response.additional_properties = d
        return model_get_series_fee_changes_response

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
