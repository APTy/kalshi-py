import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.milestone_details import MilestoneDetails


T = TypeVar("T", bound="Milestone")


@_attrs_define
class Milestone:
    """
    Attributes:
        id (str): Unique identifier for the milestone.
        category (str): Category of the milestone.
        type_ (str): Type of the milestone.
        start_date (datetime.datetime): Start date of the milestone.
        related_event_tickers (list[str]): List of event tickers related to this milestone.
        title (str): Title of the milestone.
        notification_message (str): Notification message for the milestone.
        details (MilestoneDetails): Additional details about the milestone.
        primary_event_tickers (list[str]): List of event tickers directly related to the outcome of this milestone.
        last_updated_ts (datetime.datetime): Last time this structured target was updated.
        end_date (Union[None, Unset, datetime.datetime]): End date of the milestone, if any.
        source_id (Union[None, Unset, str]): Source id of milestone if available.
    """

    id: str
    category: str
    type_: str
    start_date: datetime.datetime
    related_event_tickers: list[str]
    title: str
    notification_message: str
    details: "MilestoneDetails"
    primary_event_tickers: list[str]
    last_updated_ts: datetime.datetime
    end_date: Union[None, Unset, datetime.datetime] = UNSET
    source_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        category = self.category

        type_ = self.type_

        start_date = self.start_date.isoformat()

        related_event_tickers = self.related_event_tickers

        title = self.title

        notification_message = self.notification_message

        details = self.details.to_dict()

        primary_event_tickers = self.primary_event_tickers

        last_updated_ts = self.last_updated_ts.isoformat()

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        source_id: Union[None, Unset, str]
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        else:
            source_id = self.source_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "category": category,
                "type": type_,
                "start_date": start_date,
                "related_event_tickers": related_event_tickers,
                "title": title,
                "notification_message": notification_message,
                "details": details,
                "primary_event_tickers": primary_event_tickers,
                "last_updated_ts": last_updated_ts,
            }
        )
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if source_id is not UNSET:
            field_dict["source_id"] = source_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.milestone_details import MilestoneDetails

        d = dict(src_dict)
        id = d.pop("id")

        category = d.pop("category")

        type_ = d.pop("type")

        start_date = isoparse(d.pop("start_date"))

        related_event_tickers = cast(list[str], d.pop("related_event_tickers"))

        title = d.pop("title")

        notification_message = d.pop("notification_message")

        details = MilestoneDetails.from_dict(d.pop("details"))

        primary_event_tickers = cast(list[str], d.pop("primary_event_tickers"))

        last_updated_ts = isoparse(d.pop("last_updated_ts"))

        def _parse_end_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        def _parse_source_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_id = _parse_source_id(d.pop("source_id", UNSET))

        milestone = cls(
            id=id,
            category=category,
            type_=type_,
            start_date=start_date,
            related_event_tickers=related_event_tickers,
            title=title,
            notification_message=notification_message,
            details=details,
            primary_event_tickers=primary_event_tickers,
            last_updated_ts=last_updated_ts,
            end_date=end_date,
            source_id=source_id,
        )

        milestone.additional_properties = d
        return milestone

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
