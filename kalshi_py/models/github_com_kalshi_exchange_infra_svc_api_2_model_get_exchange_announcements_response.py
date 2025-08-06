from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_get_exchange_announcements_response_announcements_item import (
        GithubComKalshiExchangeInfraSvcApi2ModelGetExchangeAnnouncementsResponseAnnouncementsItem,
    )


T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelGetExchangeAnnouncementsResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelGetExchangeAnnouncementsResponse:
    """
    Attributes:
        announcements (Union[Unset,
            list['GithubComKalshiExchangeInfraSvcApi2ModelGetExchangeAnnouncementsResponseAnnouncementsItem']]): A list of
            exchange-wide announcements.
    """

    announcements: Union[
        Unset, list["GithubComKalshiExchangeInfraSvcApi2ModelGetExchangeAnnouncementsResponseAnnouncementsItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        announcements: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.announcements, Unset):
            announcements = []
            for announcements_item_data in self.announcements:
                announcements_item = announcements_item_data.to_dict()
                announcements.append(announcements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if announcements is not UNSET:
            field_dict["announcements"] = announcements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_get_exchange_announcements_response_announcements_item import (
            GithubComKalshiExchangeInfraSvcApi2ModelGetExchangeAnnouncementsResponseAnnouncementsItem,
        )

        d = dict(src_dict)
        announcements = []
        _announcements = d.pop("announcements", UNSET)
        for announcements_item_data in _announcements or []:
            announcements_item = (
                GithubComKalshiExchangeInfraSvcApi2ModelGetExchangeAnnouncementsResponseAnnouncementsItem.from_dict(
                    announcements_item_data
                )
            )

            announcements.append(announcements_item)

        github_com_kalshi_exchange_infra_svc_api_2_model_get_exchange_announcements_response = cls(
            announcements=announcements,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_get_exchange_announcements_response.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_get_exchange_announcements_response

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
