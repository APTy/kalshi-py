from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generic_object import GenericObject


T = TypeVar("T", bound="GithubComKalshiExchangeInfraCommonUnimodelDetails")


@_attrs_define
class GithubComKalshiExchangeInfraCommonUnimodelDetails:
    """
    Attributes:
        key (Union[Unset, GenericObject]): Generic object type
    """

    key: Union[Unset, "GenericObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generic_object import GenericObject

        d = dict(src_dict)
        _key = d.pop("key", UNSET)
        key: Union[Unset, GenericObject]
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = GenericObject.from_dict(_key)

        github_com_kalshi_exchange_infra_common_unimodel_details = cls(
            key=key,
        )

        github_com_kalshi_exchange_infra_common_unimodel_details.additional_properties = d
        return github_com_kalshi_exchange_infra_common_unimodel_details

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
