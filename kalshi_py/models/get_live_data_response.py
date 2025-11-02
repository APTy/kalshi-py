from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.live_data import LiveData


T = TypeVar("T", bound="GetLiveDataResponse")


@_attrs_define
class GetLiveDataResponse:
    """
    Attributes:
        live_data (LiveData):
    """

    live_data: "LiveData"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        live_data = self.live_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "live_data": live_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.live_data import LiveData

        d = dict(src_dict)
        live_data = LiveData.from_dict(d.pop("live_data"))

        get_live_data_response = cls(
            live_data=live_data,
        )

        get_live_data_response.additional_properties = d
        return get_live_data_response

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
