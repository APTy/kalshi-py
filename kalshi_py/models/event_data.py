import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_data_product_metadata_type_0 import EventDataProductMetadataType0
    from ..models.market import Market


T = TypeVar("T", bound="EventData")


@_attrs_define
class EventData:
    """
    Attributes:
        event_ticker (str): Unique identifier for this event.
        series_ticker (str): Unique identifier for the series this event belongs to.
        sub_title (str): Shortened descriptive title for the event.
        title (str): Full title of the event.
        collateral_return_type (str): Specifies how collateral is returned when markets settle (e.g., 'binary' for
            standard yes/no markets).
        mutually_exclusive (bool): If true, only one market in this event can resolve to 'yes'. If false, multiple
            markets can resolve to 'yes'.
        category (str): Event category (deprecated, use series-level category instead).
        available_on_brokers (bool): Whether this event is available to trade on brokers.
        product_metadata (Union['EventDataProductMetadataType0', None]): Additional metadata for the event.
        strike_date (Union[None, Unset, datetime.datetime]): The specific date this event is based on. Only filled when
            the event uses a date strike (mutually exclusive with strike_period).
        strike_period (Union[None, Unset, str]): The time period this event covers (e.g., 'week', 'month'). Only filled
            when the event uses a period strike (mutually exclusive with strike_date).
        markets (Union[None, Unset, list['Market']]): Array of markets associated with this event. Only populated when
            'with_nested_markets=true' is specified in the request.
    """

    event_ticker: str
    series_ticker: str
    sub_title: str
    title: str
    collateral_return_type: str
    mutually_exclusive: bool
    category: str
    available_on_brokers: bool
    product_metadata: Union["EventDataProductMetadataType0", None]
    strike_date: Union[None, Unset, datetime.datetime] = UNSET
    strike_period: Union[None, Unset, str] = UNSET
    markets: Union[None, Unset, list["Market"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_data_product_metadata_type_0 import EventDataProductMetadataType0

        event_ticker = self.event_ticker

        series_ticker = self.series_ticker

        sub_title = self.sub_title

        title = self.title

        collateral_return_type = self.collateral_return_type

        mutually_exclusive = self.mutually_exclusive

        category = self.category

        available_on_brokers = self.available_on_brokers

        product_metadata: Union[None, dict[str, Any]]
        if isinstance(self.product_metadata, EventDataProductMetadataType0):
            product_metadata = self.product_metadata.to_dict()
        else:
            product_metadata = self.product_metadata

        strike_date: Union[None, Unset, str]
        if isinstance(self.strike_date, Unset):
            strike_date = UNSET
        elif isinstance(self.strike_date, datetime.datetime):
            strike_date = self.strike_date.isoformat()
        else:
            strike_date = self.strike_date

        strike_period: Union[None, Unset, str]
        if isinstance(self.strike_period, Unset):
            strike_period = UNSET
        else:
            strike_period = self.strike_period

        markets: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.markets, Unset):
            markets = UNSET
        elif isinstance(self.markets, list):
            markets = []
            for markets_type_0_item_data in self.markets:
                markets_type_0_item = markets_type_0_item_data.to_dict()
                markets.append(markets_type_0_item)

        else:
            markets = self.markets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_ticker": event_ticker,
                "series_ticker": series_ticker,
                "sub_title": sub_title,
                "title": title,
                "collateral_return_type": collateral_return_type,
                "mutually_exclusive": mutually_exclusive,
                "category": category,
                "available_on_brokers": available_on_brokers,
                "product_metadata": product_metadata,
            }
        )
        if strike_date is not UNSET:
            field_dict["strike_date"] = strike_date
        if strike_period is not UNSET:
            field_dict["strike_period"] = strike_period
        if markets is not UNSET:
            field_dict["markets"] = markets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_data_product_metadata_type_0 import EventDataProductMetadataType0
        from ..models.market import Market

        d = dict(src_dict)
        event_ticker = d.pop("event_ticker")

        series_ticker = d.pop("series_ticker")

        sub_title = d.pop("sub_title")

        title = d.pop("title")

        collateral_return_type = d.pop("collateral_return_type")

        mutually_exclusive = d.pop("mutually_exclusive")

        category = d.pop("category")

        available_on_brokers = d.pop("available_on_brokers")

        def _parse_product_metadata(data: object) -> Union["EventDataProductMetadataType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                product_metadata_type_0 = EventDataProductMetadataType0.from_dict(data)

                return product_metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["EventDataProductMetadataType0", None], data)

        product_metadata = _parse_product_metadata(d.pop("product_metadata"))

        def _parse_strike_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                strike_date_type_0 = isoparse(data)

                return strike_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        strike_date = _parse_strike_date(d.pop("strike_date", UNSET))

        def _parse_strike_period(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        strike_period = _parse_strike_period(d.pop("strike_period", UNSET))

        def _parse_markets(data: object) -> Union[None, Unset, list["Market"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                markets_type_0 = []
                _markets_type_0 = data
                for markets_type_0_item_data in _markets_type_0:
                    markets_type_0_item = Market.from_dict(markets_type_0_item_data)

                    markets_type_0.append(markets_type_0_item)

                return markets_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["Market"]], data)

        markets = _parse_markets(d.pop("markets", UNSET))

        event_data = cls(
            event_ticker=event_ticker,
            series_ticker=series_ticker,
            sub_title=sub_title,
            title=title,
            collateral_return_type=collateral_return_type,
            mutually_exclusive=mutually_exclusive,
            category=category,
            available_on_brokers=available_on_brokers,
            product_metadata=product_metadata,
            strike_date=strike_date,
            strike_period=strike_period,
            markets=markets,
        )

        event_data.additional_properties = d
        return event_data

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
