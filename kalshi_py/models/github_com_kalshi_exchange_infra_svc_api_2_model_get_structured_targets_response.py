from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_structured_target import (
        GithubComKalshiExchangeInfraSvcApi2ModelStructuredTarget,
    )


T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelGetStructuredTargetsResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelGetStructuredTargetsResponse:
    """
    Attributes:
        cursor (Union[Unset, str]): Pagination cursor for the next page. Empty if there are no more results.
        structured_targets (Union[Unset, list['GithubComKalshiExchangeInfraSvcApi2ModelStructuredTarget']]): Array of
            structured targets matching the query criteria.
    """

    cursor: Union[Unset, str] = UNSET
    structured_targets: Union[Unset, list["GithubComKalshiExchangeInfraSvcApi2ModelStructuredTarget"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursor = self.cursor

        structured_targets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.structured_targets, Unset):
            structured_targets = []
            for structured_targets_item_data in self.structured_targets:
                structured_targets_item = structured_targets_item_data.to_dict()
                structured_targets.append(structured_targets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if structured_targets is not UNSET:
            field_dict["structured_targets"] = structured_targets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_structured_target import (
            GithubComKalshiExchangeInfraSvcApi2ModelStructuredTarget,
        )

        d = dict(src_dict)
        cursor = d.pop("cursor", UNSET)

        structured_targets = []
        _structured_targets = d.pop("structured_targets", UNSET)
        for structured_targets_item_data in _structured_targets or []:
            structured_targets_item = GithubComKalshiExchangeInfraSvcApi2ModelStructuredTarget.from_dict(
                structured_targets_item_data
            )

            structured_targets.append(structured_targets_item)

        github_com_kalshi_exchange_infra_svc_api_2_model_get_structured_targets_response = cls(
            cursor=cursor,
            structured_targets=structured_targets,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_get_structured_targets_response.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_get_structured_targets_response

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
