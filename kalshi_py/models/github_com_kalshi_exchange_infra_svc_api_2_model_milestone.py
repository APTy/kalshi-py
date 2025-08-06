import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_common_unimodel_details import (
        GithubComKalshiExchangeInfraCommonUnimodelDetails,
    )


T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelMilestone")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelMilestone:
    """
    Attributes:
        category (Union[Unset, str]): Category of the milestone.
        details (Union[Unset, GithubComKalshiExchangeInfraCommonUnimodelDetails]):
        end_date (Union[Unset, datetime.datetime]): End date of the milestone, if any.
        id (Union[Unset, str]): Unique identifier for the milestone.
        last_updated_ts (Union[Unset, datetime.datetime]): Last time this structured target was updated.
        notification_message (Union[Unset, str]): Notification message for the milestone.
        primary_event_tickers (Union[Unset, list[str]]): List of event tickers directly related to the outcome of this
            milestone.
        related_event_tickers (Union[Unset, list[str]]): List of event tickers related to this milestone.
        source_id (Union[Unset, str]): Source id of milestone if available.
        start_date (Union[Unset, datetime.datetime]): Start date of the milestone.
        title (Union[Unset, str]): Title of the milestone.
        type_ (Union[Unset, str]): Type of the milestone.
    """

    category: Union[Unset, str] = UNSET
    details: Union[Unset, "GithubComKalshiExchangeInfraCommonUnimodelDetails"] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated_ts: Union[Unset, datetime.datetime] = UNSET
    notification_message: Union[Unset, str] = UNSET
    primary_event_tickers: Union[Unset, list[str]] = UNSET
    related_event_tickers: Union[Unset, list[str]] = UNSET
    source_id: Union[Unset, str] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    title: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        id = self.id

        last_updated_ts: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_ts, Unset):
            last_updated_ts = self.last_updated_ts.isoformat()

        notification_message = self.notification_message

        primary_event_tickers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.primary_event_tickers, Unset):
            primary_event_tickers = self.primary_event_tickers

        related_event_tickers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.related_event_tickers, Unset):
            related_event_tickers = self.related_event_tickers

        source_id = self.source_id

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        title = self.title

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if details is not UNSET:
            field_dict["details"] = details
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if id is not UNSET:
            field_dict["id"] = id
        if last_updated_ts is not UNSET:
            field_dict["last_updated_ts"] = last_updated_ts
        if notification_message is not UNSET:
            field_dict["notification_message"] = notification_message
        if primary_event_tickers is not UNSET:
            field_dict["primary_event_tickers"] = primary_event_tickers
        if related_event_tickers is not UNSET:
            field_dict["related_event_tickers"] = related_event_tickers
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_common_unimodel_details import (
            GithubComKalshiExchangeInfraCommonUnimodelDetails,
        )

        d = dict(src_dict)
        category = d.pop("category", UNSET)

        _details = d.pop("details", UNSET)
        details: Union[Unset, GithubComKalshiExchangeInfraCommonUnimodelDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = GithubComKalshiExchangeInfraCommonUnimodelDetails.from_dict(_details)

        _end_date = d.pop("end_date", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        id = d.pop("id", UNSET)

        _last_updated_ts = d.pop("last_updated_ts", UNSET)
        last_updated_ts: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_ts, Unset):
            last_updated_ts = UNSET
        else:
            last_updated_ts = isoparse(_last_updated_ts)

        notification_message = d.pop("notification_message", UNSET)

        primary_event_tickers = cast(list[str], d.pop("primary_event_tickers", UNSET))

        related_event_tickers = cast(list[str], d.pop("related_event_tickers", UNSET))

        source_id = d.pop("source_id", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        github_com_kalshi_exchange_infra_svc_api_2_model_milestone = cls(
            category=category,
            details=details,
            end_date=end_date,
            id=id,
            last_updated_ts=last_updated_ts,
            notification_message=notification_message,
            primary_event_tickers=primary_event_tickers,
            related_event_tickers=related_event_tickers,
            source_id=source_id,
            start_date=start_date,
            title=title,
            type_=type_,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_milestone.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_milestone

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
