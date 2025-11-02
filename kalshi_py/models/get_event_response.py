from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.event_data import EventData
    from ..models.market import Market


T = TypeVar("T", bound="GetEventResponse")


@_attrs_define
class GetEventResponse:
    """
    Attributes:
        event (EventData):
        markets (list['Market']): Data for the markets in this event. This field is deprecated in favour of the
            "markets" field inside the event. Which will be filled with the same value if you use the query parameter
            "with_nested_markets=true".
    """

    event: "EventData"
    markets: list["Market"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event = self.event.to_dict()

        markets = []
        for markets_item_data in self.markets:
            markets_item = markets_item_data.to_dict()
            markets.append(markets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
                "markets": markets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_data import EventData
        from ..models.market import Market

        d = dict(src_dict)
        event = EventData.from_dict(d.pop("event"))

        markets = []
        _markets = d.pop("markets")
        for markets_item_data in _markets:
            markets_item = Market.from_dict(markets_item_data)

            markets.append(markets_item)

        get_event_response = cls(
            event=event,
            markets=markets,
        )

        get_event_response.additional_properties = d
        return get_event_response

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
