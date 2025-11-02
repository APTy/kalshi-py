import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.associated_event import AssociatedEvent


T = TypeVar("T", bound="MultivariateEventCollection")


@_attrs_define
class MultivariateEventCollection:
    """
    Attributes:
        collection_ticker (str): Unique identifier for the collection.
        series_ticker (str): Series associated with the collection. Events produced in the collection will be associated
            with this series.
        title (str): Title of the collection.
        description (str): Short description of the collection.
        open_date (datetime.datetime): The open date of the collection. Before this time, the collection cannot be
            interacted with.
        close_date (datetime.datetime): The close date of the collection. After this time, the collection cannot be
            interacted with.
        associated_events (list['AssociatedEvent']): List of events with their individual configuration.
        associated_event_tickers (list[str]): [DEPRECATED - Use associated_events instead] A list of events associated
            with the collection. Markets in these events can be passed as inputs to the Lookup and Create endpoints.
        is_ordered (bool): Whether the collection is ordered. If true, the order of markets passed into Lookup/Create
            affects the output. If false, the order does not matter.
        is_single_market_per_event (bool): [DEPRECATED - Use associated_events instead] Whether the collection accepts
            multiple markets from the same event passed into Lookup/Create.
        is_all_yes (bool): [DEPRECATED - Use associated_events instead] Whether the collection requires that only the
            market side of 'yes' may be used.
        size_min (int): The minimum number of markets that must be passed into Lookup/Create (inclusive).
        size_max (int): The maximum number of markets that must be passed into Lookup/Create (inclusive).
        functional_description (str): A functional description of the collection describing how inputs affect the
            output.
    """

    collection_ticker: str
    series_ticker: str
    title: str
    description: str
    open_date: datetime.datetime
    close_date: datetime.datetime
    associated_events: list["AssociatedEvent"]
    associated_event_tickers: list[str]
    is_ordered: bool
    is_single_market_per_event: bool
    is_all_yes: bool
    size_min: int
    size_max: int
    functional_description: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_ticker = self.collection_ticker

        series_ticker = self.series_ticker

        title = self.title

        description = self.description

        open_date = self.open_date.isoformat()

        close_date = self.close_date.isoformat()

        associated_events = []
        for associated_events_item_data in self.associated_events:
            associated_events_item = associated_events_item_data.to_dict()
            associated_events.append(associated_events_item)

        associated_event_tickers = self.associated_event_tickers

        is_ordered = self.is_ordered

        is_single_market_per_event = self.is_single_market_per_event

        is_all_yes = self.is_all_yes

        size_min = self.size_min

        size_max = self.size_max

        functional_description = self.functional_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_ticker": collection_ticker,
                "series_ticker": series_ticker,
                "title": title,
                "description": description,
                "open_date": open_date,
                "close_date": close_date,
                "associated_events": associated_events,
                "associated_event_tickers": associated_event_tickers,
                "is_ordered": is_ordered,
                "is_single_market_per_event": is_single_market_per_event,
                "is_all_yes": is_all_yes,
                "size_min": size_min,
                "size_max": size_max,
                "functional_description": functional_description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.associated_event import AssociatedEvent

        d = dict(src_dict)
        collection_ticker = d.pop("collection_ticker")

        series_ticker = d.pop("series_ticker")

        title = d.pop("title")

        description = d.pop("description")

        open_date = isoparse(d.pop("open_date"))

        close_date = isoparse(d.pop("close_date"))

        associated_events = []
        _associated_events = d.pop("associated_events")
        for associated_events_item_data in _associated_events:
            associated_events_item = AssociatedEvent.from_dict(associated_events_item_data)

            associated_events.append(associated_events_item)

        associated_event_tickers = cast(list[str], d.pop("associated_event_tickers"))

        is_ordered = d.pop("is_ordered")

        is_single_market_per_event = d.pop("is_single_market_per_event")

        is_all_yes = d.pop("is_all_yes")

        size_min = d.pop("size_min")

        size_max = d.pop("size_max")

        functional_description = d.pop("functional_description")

        multivariate_event_collection = cls(
            collection_ticker=collection_ticker,
            series_ticker=series_ticker,
            title=title,
            description=description,
            open_date=open_date,
            close_date=close_date,
            associated_events=associated_events,
            associated_event_tickers=associated_event_tickers,
            is_ordered=is_ordered,
            is_single_market_per_event=is_single_market_per_event,
            is_all_yes=is_all_yes,
            size_min=size_min,
            size_max=size_max,
            functional_description=functional_description,
        )

        multivariate_event_collection.additional_properties = d
        return multivariate_event_collection

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
