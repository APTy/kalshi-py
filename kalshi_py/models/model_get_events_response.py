from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_event_data import ModelEventData


T = TypeVar("T", bound="ModelGetEventsResponse")


@_attrs_define
class ModelGetEventsResponse:
    """
    Attributes:
        cursor (Union[Unset, str]): Pagination cursor for the next page. Empty if there are no more results.
        events (Union[Unset, list['ModelEventData']]): Array of events matching the query criteria.
    """

    cursor: Union[Unset, str] = UNSET
    events: Union[Unset, list["ModelEventData"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursor = self.cursor

        events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_event_data import ModelEventData

        d = dict(src_dict)
        cursor = d.pop("cursor", UNSET)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = ModelEventData.from_dict(events_item_data)

            events.append(events_item)

        model_get_events_response = cls(
            cursor=cursor,
            events=events,
        )

        model_get_events_response.additional_properties = d
        return model_get_events_response

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
