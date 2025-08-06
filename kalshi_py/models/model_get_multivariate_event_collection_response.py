from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_multivariate_event_collection import ModelMultivariateEventCollection


T = TypeVar("T", bound="ModelGetMultivariateEventCollectionResponse")


@_attrs_define
class ModelGetMultivariateEventCollectionResponse:
    """
    Attributes:
        multivariate_contract (Union[Unset, ModelMultivariateEventCollection]):
    """

    multivariate_contract: Union[Unset, "ModelMultivariateEventCollection"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        multivariate_contract: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.multivariate_contract, Unset):
            multivariate_contract = self.multivariate_contract.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if multivariate_contract is not UNSET:
            field_dict["multivariate_contract"] = multivariate_contract

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_multivariate_event_collection import ModelMultivariateEventCollection

        d = dict(src_dict)
        _multivariate_contract = d.pop("multivariate_contract", UNSET)
        multivariate_contract: Union[Unset, ModelMultivariateEventCollection]
        if isinstance(_multivariate_contract, Unset):
            multivariate_contract = UNSET
        else:
            multivariate_contract = ModelMultivariateEventCollection.from_dict(_multivariate_contract)

        model_get_multivariate_event_collection_response = cls(
            multivariate_contract=multivariate_contract,
        )

        model_get_multivariate_event_collection_response.additional_properties = d
        return model_get_multivariate_event_collection_response

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
