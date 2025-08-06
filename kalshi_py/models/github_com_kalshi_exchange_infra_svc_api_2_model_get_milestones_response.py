from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_milestone import (
        GithubComKalshiExchangeInfraSvcApi2ModelMilestone,
    )


T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelGetMilestonesResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelGetMilestonesResponse:
    """
    Attributes:
        cursor (Union[Unset, str]): Cursor for pagination.
        milestones (Union[Unset, list['GithubComKalshiExchangeInfraSvcApi2ModelMilestone']]): List of milestones.
    """

    cursor: Union[Unset, str] = UNSET
    milestones: Union[Unset, list["GithubComKalshiExchangeInfraSvcApi2ModelMilestone"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursor = self.cursor

        milestones: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.milestones, Unset):
            milestones = []
            for milestones_item_data in self.milestones:
                milestones_item = milestones_item_data.to_dict()
                milestones.append(milestones_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if milestones is not UNSET:
            field_dict["milestones"] = milestones

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_milestone import (
            GithubComKalshiExchangeInfraSvcApi2ModelMilestone,
        )

        d = dict(src_dict)
        cursor = d.pop("cursor", UNSET)

        milestones = []
        _milestones = d.pop("milestones", UNSET)
        for milestones_item_data in _milestones or []:
            milestones_item = GithubComKalshiExchangeInfraSvcApi2ModelMilestone.from_dict(milestones_item_data)

            milestones.append(milestones_item)

        github_com_kalshi_exchange_infra_svc_api_2_model_get_milestones_response = cls(
            cursor=cursor,
            milestones=milestones,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_get_milestones_response.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_get_milestones_response

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
