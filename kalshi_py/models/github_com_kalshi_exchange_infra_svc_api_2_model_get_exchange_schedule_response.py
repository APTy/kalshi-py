from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_common_exchange_metadata_schedule import (
        GithubComKalshiExchangeInfraCommonExchangeMetadataSchedule,
    )


T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelGetExchangeScheduleResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelGetExchangeScheduleResponse:
    """
    Attributes:
        schedule (Union[Unset, GithubComKalshiExchangeInfraCommonExchangeMetadataSchedule]):
    """

    schedule: Union[Unset, "GithubComKalshiExchangeInfraCommonExchangeMetadataSchedule"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_common_exchange_metadata_schedule import (
            GithubComKalshiExchangeInfraCommonExchangeMetadataSchedule,
        )

        d = dict(src_dict)
        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, GithubComKalshiExchangeInfraCommonExchangeMetadataSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = GithubComKalshiExchangeInfraCommonExchangeMetadataSchedule.from_dict(_schedule)

        github_com_kalshi_exchange_infra_svc_api_2_model_get_exchange_schedule_response = cls(
            schedule=schedule,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_get_exchange_schedule_response.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_get_exchange_schedule_response

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
