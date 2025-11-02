from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.live_data import LiveData


T = TypeVar("T", bound="GetLiveDatasResponse")


@_attrs_define
class GetLiveDatasResponse:
    """
    Attributes:
        live_datas (list['LiveData']):
    """

    live_datas: list["LiveData"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        live_datas = []
        for live_datas_item_data in self.live_datas:
            live_datas_item = live_datas_item_data.to_dict()
            live_datas.append(live_datas_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "live_datas": live_datas,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.live_data import LiveData

        d = dict(src_dict)
        live_datas = []
        _live_datas = d.pop("live_datas")
        for live_datas_item_data in _live_datas:
            live_datas_item = LiveData.from_dict(live_datas_item_data)

            live_datas.append(live_datas_item)

        get_live_datas_response = cls(
            live_datas=live_datas,
        )

        get_live_datas_response.additional_properties = d
        return get_live_datas_response

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
