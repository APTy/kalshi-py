from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_get_incentive_programs_response_incentive_programs_item import (
        ModelGetIncentiveProgramsResponseIncentiveProgramsItem,
    )


T = TypeVar("T", bound="ModelGetIncentiveProgramsResponse")


@_attrs_define
class ModelGetIncentiveProgramsResponse:
    """
    Attributes:
        incentive_programs (Union[Unset, list['ModelGetIncentiveProgramsResponseIncentiveProgramsItem']]):
        next_cursor (Union[Unset, str]):
    """

    incentive_programs: Union[Unset, list["ModelGetIncentiveProgramsResponseIncentiveProgramsItem"]] = UNSET
    next_cursor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incentive_programs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.incentive_programs, Unset):
            incentive_programs = []
            for incentive_programs_item_data in self.incentive_programs:
                incentive_programs_item = incentive_programs_item_data.to_dict()
                incentive_programs.append(incentive_programs_item)

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if incentive_programs is not UNSET:
            field_dict["incentive_programs"] = incentive_programs
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_get_incentive_programs_response_incentive_programs_item import (
            ModelGetIncentiveProgramsResponseIncentiveProgramsItem,
        )

        d = dict(src_dict)
        incentive_programs = []
        _incentive_programs = d.pop("incentive_programs", UNSET)
        for incentive_programs_item_data in _incentive_programs or []:
            incentive_programs_item = ModelGetIncentiveProgramsResponseIncentiveProgramsItem.from_dict(
                incentive_programs_item_data
            )

            incentive_programs.append(incentive_programs_item)

        next_cursor = d.pop("next_cursor", UNSET)

        model_get_incentive_programs_response = cls(
            incentive_programs=incentive_programs,
            next_cursor=next_cursor,
        )

        model_get_incentive_programs_response.additional_properties = d
        return model_get_incentive_programs_response

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
