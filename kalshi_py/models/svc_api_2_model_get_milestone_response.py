from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.svc_api_2_model_milestone import SvcApi2ModelMilestone


T = TypeVar("T", bound="SvcApi2ModelGetMilestoneResponse")


@_attrs_define
class SvcApi2ModelGetMilestoneResponse:
    """
    Attributes:
        milestone (Union[Unset, SvcApi2ModelMilestone]):
    """

    milestone: Union[Unset, "SvcApi2ModelMilestone"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        milestone: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.milestone, Unset):
            milestone = self.milestone.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if milestone is not UNSET:
            field_dict["milestone"] = milestone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.svc_api_2_model_milestone import SvcApi2ModelMilestone

        d = dict(src_dict)
        _milestone = d.pop("milestone", UNSET)
        milestone: Union[Unset, SvcApi2ModelMilestone]
        if isinstance(_milestone, Unset):
            milestone = UNSET
        else:
            milestone = SvcApi2ModelMilestone.from_dict(_milestone)

        svc_api_2_model_get_milestone_response = cls(
            milestone=milestone,
        )

        svc_api_2_model_get_milestone_response.additional_properties = d
        return svc_api_2_model_get_milestone_response

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
