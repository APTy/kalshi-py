import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelMultivariateEventCollection")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelMultivariateEventCollection:
    """
    Attributes:
        associated_event_tickers (Union[Unset, list[str]]): A list of events associated with the collection. Markets in
            these events can be passed as inputs to the Lookup and Create endpoints.
        close_date (Union[Unset, datetime.datetime]): The close date of the collection. After this time, the collection
            cannot be interacted with.
        collection_ticker (Union[Unset, str]): Unique identifier for the collection.
        description (Union[Unset, str]): Short description of the collection.
        functional_description (Union[Unset, str]): A functional description of the collection describing how inputs
            affect the output.
        is_all_yes (Union[Unset, bool]): Whether the collection requires that only the market side of 'yes' may be used.
        is_ordered (Union[Unset, bool]): Whether the collection is ordered. If true, the order of markets passed into
            Lookup/Create affects the output. If false, the order does not matter.
        is_single_market_per_event (Union[Unset, bool]): Whether the collection accepts multiple markets from the same
            event passed into Lookup/Create.
        open_date (Union[Unset, datetime.datetime]): The open date of the collection. Before this time, the collection
            cannot be interacted with.
        series_ticker (Union[Unset, str]): Series associated with the collection. Events produced in the collection will
            be associated with this series.
        size_max (Union[Unset, int]): The maximum number of markets that must be passed into Lookup/Create (inclusive).
        size_min (Union[Unset, int]): The minimum number of markets that must be passed into Lookup/Create (inclusive).
        title (Union[Unset, str]): Title of the collection.
    """

    associated_event_tickers: Union[Unset, list[str]] = UNSET
    close_date: Union[Unset, datetime.datetime] = UNSET
    collection_ticker: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    functional_description: Union[Unset, str] = UNSET
    is_all_yes: Union[Unset, bool] = UNSET
    is_ordered: Union[Unset, bool] = UNSET
    is_single_market_per_event: Union[Unset, bool] = UNSET
    open_date: Union[Unset, datetime.datetime] = UNSET
    series_ticker: Union[Unset, str] = UNSET
    size_max: Union[Unset, int] = UNSET
    size_min: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        associated_event_tickers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.associated_event_tickers, Unset):
            associated_event_tickers = self.associated_event_tickers

        close_date: Union[Unset, str] = UNSET
        if not isinstance(self.close_date, Unset):
            close_date = self.close_date.isoformat()

        collection_ticker = self.collection_ticker

        description = self.description

        functional_description = self.functional_description

        is_all_yes = self.is_all_yes

        is_ordered = self.is_ordered

        is_single_market_per_event = self.is_single_market_per_event

        open_date: Union[Unset, str] = UNSET
        if not isinstance(self.open_date, Unset):
            open_date = self.open_date.isoformat()

        series_ticker = self.series_ticker

        size_max = self.size_max

        size_min = self.size_min

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if associated_event_tickers is not UNSET:
            field_dict["associated_event_tickers"] = associated_event_tickers
        if close_date is not UNSET:
            field_dict["close_date"] = close_date
        if collection_ticker is not UNSET:
            field_dict["collection_ticker"] = collection_ticker
        if description is not UNSET:
            field_dict["description"] = description
        if functional_description is not UNSET:
            field_dict["functional_description"] = functional_description
        if is_all_yes is not UNSET:
            field_dict["is_all_yes"] = is_all_yes
        if is_ordered is not UNSET:
            field_dict["is_ordered"] = is_ordered
        if is_single_market_per_event is not UNSET:
            field_dict["is_single_market_per_event"] = is_single_market_per_event
        if open_date is not UNSET:
            field_dict["open_date"] = open_date
        if series_ticker is not UNSET:
            field_dict["series_ticker"] = series_ticker
        if size_max is not UNSET:
            field_dict["size_max"] = size_max
        if size_min is not UNSET:
            field_dict["size_min"] = size_min
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        associated_event_tickers = cast(list[str], d.pop("associated_event_tickers", UNSET))

        _close_date = d.pop("close_date", UNSET)
        close_date: Union[Unset, datetime.datetime]
        if isinstance(_close_date, Unset):
            close_date = UNSET
        else:
            close_date = isoparse(_close_date)

        collection_ticker = d.pop("collection_ticker", UNSET)

        description = d.pop("description", UNSET)

        functional_description = d.pop("functional_description", UNSET)

        is_all_yes = d.pop("is_all_yes", UNSET)

        is_ordered = d.pop("is_ordered", UNSET)

        is_single_market_per_event = d.pop("is_single_market_per_event", UNSET)

        _open_date = d.pop("open_date", UNSET)
        open_date: Union[Unset, datetime.datetime]
        if isinstance(_open_date, Unset):
            open_date = UNSET
        else:
            open_date = isoparse(_open_date)

        series_ticker = d.pop("series_ticker", UNSET)

        size_max = d.pop("size_max", UNSET)

        size_min = d.pop("size_min", UNSET)

        title = d.pop("title", UNSET)

        github_com_kalshi_exchange_infra_svc_api_2_model_multivariate_event_collection = cls(
            associated_event_tickers=associated_event_tickers,
            close_date=close_date,
            collection_ticker=collection_ticker,
            description=description,
            functional_description=functional_description,
            is_all_yes=is_all_yes,
            is_ordered=is_ordered,
            is_single_market_per_event=is_single_market_per_event,
            open_date=open_date,
            series_ticker=series_ticker,
            size_max=size_max,
            size_min=size_min,
            title=title,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_multivariate_event_collection.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_multivariate_event_collection

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
