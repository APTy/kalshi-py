from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_data import EventData
    from ..models.milestone import Milestone


T = TypeVar("T", bound="GetEventsResponse")


@_attrs_define
class GetEventsResponse:
    """
    Attributes:
        events (list['EventData']): Array of events matching the query criteria.
        cursor (str): Pagination cursor for the next page. Empty if there are no more results.
        milestones (Union[Unset, list['Milestone']]): Array of milestones related to the events.
    """

    events: list["EventData"]
    cursor: str
    milestones: Union[Unset, list["Milestone"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        cursor = self.cursor

        milestones: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.milestones, Unset):
            milestones = []
            for milestones_item_data in self.milestones:
                milestones_item = milestones_item_data.to_dict()
                milestones.append(milestones_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
                "cursor": cursor,
            }
        )
        if milestones is not UNSET:
            field_dict["milestones"] = milestones

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_data import EventData
        from ..models.milestone import Milestone

        d = dict(src_dict)
        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = EventData.from_dict(events_item_data)

            events.append(events_item)

        cursor = d.pop("cursor")

        milestones = []
        _milestones = d.pop("milestones", UNSET)
        for milestones_item_data in _milestones or []:
            milestones_item = Milestone.from_dict(milestones_item_data)

            milestones.append(milestones_item)

        get_events_response = cls(
            events=events,
            cursor=cursor,
            milestones=milestones,
        )

        get_events_response.additional_properties = d
        return get_events_response

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
