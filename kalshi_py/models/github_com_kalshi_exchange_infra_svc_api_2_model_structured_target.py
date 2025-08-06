import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_common_unimodel_details import (
        GithubComKalshiExchangeInfraCommonUnimodelDetails,
    )


T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelStructuredTarget")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelStructuredTarget:
    """
    Attributes:
        details (Union[Unset, GithubComKalshiExchangeInfraCommonUnimodelDetails]):
        id (Union[Unset, str]): Unique identifier for the structured target.
        last_updated_ts (Union[Unset, datetime.datetime]): Timestamp when this structured target was last updated.
        name (Union[Unset, str]): Name of the structured target.
        source_id (Union[Unset, str]): External source identifier for the structured target, if available (e.g., third-
            party data provider ID).
        type_ (Union[Unset, str]): Type of the structured target.
    """

    details: Union[Unset, "GithubComKalshiExchangeInfraCommonUnimodelDetails"] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated_ts: Union[Unset, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    source_id: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        id = self.id

        last_updated_ts: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_ts, Unset):
            last_updated_ts = self.last_updated_ts.isoformat()

        name = self.name

        source_id = self.source_id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["details"] = details
        if id is not UNSET:
            field_dict["id"] = id
        if last_updated_ts is not UNSET:
            field_dict["last_updated_ts"] = last_updated_ts
        if name is not UNSET:
            field_dict["name"] = name
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_common_unimodel_details import (
            GithubComKalshiExchangeInfraCommonUnimodelDetails,
        )

        d = dict(src_dict)
        _details = d.pop("details", UNSET)
        details: Union[Unset, GithubComKalshiExchangeInfraCommonUnimodelDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = GithubComKalshiExchangeInfraCommonUnimodelDetails.from_dict(_details)

        id = d.pop("id", UNSET)

        _last_updated_ts = d.pop("last_updated_ts", UNSET)
        last_updated_ts: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_ts, Unset):
            last_updated_ts = UNSET
        else:
            last_updated_ts = isoparse(_last_updated_ts)

        name = d.pop("name", UNSET)

        source_id = d.pop("source_id", UNSET)

        type_ = d.pop("type", UNSET)

        github_com_kalshi_exchange_infra_svc_api_2_model_structured_target = cls(
            details=details,
            id=id,
            last_updated_ts=last_updated_ts,
            name=name,
            source_id=source_id,
            type_=type_,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_structured_target.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_structured_target

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
