from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_event_data import ModelEventData
    from ..models.model_market import ModelMarket


T = TypeVar("T", bound="ModelGetEventResponse")


@_attrs_define
class ModelGetEventResponse:
    """
    Attributes:
        event (Union[Unset, ModelEventData]):
        markets (Union[Unset, list['ModelMarket']]):
    """

    event: Union[Unset, "ModelEventData"] = UNSET
    markets: Union[Unset, list["ModelMarket"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.to_dict()

        markets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.markets, Unset):
            markets = []
            for markets_item_data in self.markets:
                markets_item = markets_item_data.to_dict()
                markets.append(markets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event is not UNSET:
            field_dict["event"] = event
        if markets is not UNSET:
            field_dict["markets"] = markets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_event_data import ModelEventData
        from ..models.model_market import ModelMarket

        d = dict(src_dict)
        _event = d.pop("event", UNSET)
        event: Union[Unset, ModelEventData]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = ModelEventData.from_dict(_event)

        markets = []
        _markets = d.pop("markets", UNSET)
        for markets_item_data in _markets or []:
            markets_item = ModelMarket.from_dict(markets_item_data)

            markets.append(markets_item)

        model_get_event_response = cls(
            event=event,
            markets=markets,
        )

        model_get_event_response.additional_properties = d
        return model_get_event_response

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
