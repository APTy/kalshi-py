from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_multivariate_event_collection import ModelMultivariateEventCollection


T = TypeVar("T", bound="ModelGetMultivariateEventCollectionsResponse")


@_attrs_define
class ModelGetMultivariateEventCollectionsResponse:
    """
    Attributes:
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in the pagination. Use
            the value returned here in the cursor query parameter for this end-point to get the next page containing limit
            records. An empty value of this field indicates there is no next page.
        multivariate_contracts (Union[Unset, list['ModelMultivariateEventCollection']]): List of multivariate event
            collections.
    """

    cursor: Union[Unset, str] = UNSET
    multivariate_contracts: Union[Unset, list["ModelMultivariateEventCollection"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursor = self.cursor

        multivariate_contracts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.multivariate_contracts, Unset):
            multivariate_contracts = []
            for multivariate_contracts_item_data in self.multivariate_contracts:
                multivariate_contracts_item = multivariate_contracts_item_data.to_dict()
                multivariate_contracts.append(multivariate_contracts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if multivariate_contracts is not UNSET:
            field_dict["multivariate_contracts"] = multivariate_contracts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_multivariate_event_collection import ModelMultivariateEventCollection

        d = dict(src_dict)
        cursor = d.pop("cursor", UNSET)

        multivariate_contracts = []
        _multivariate_contracts = d.pop("multivariate_contracts", UNSET)
        for multivariate_contracts_item_data in _multivariate_contracts or []:
            multivariate_contracts_item = ModelMultivariateEventCollection.from_dict(multivariate_contracts_item_data)

            multivariate_contracts.append(multivariate_contracts_item)

        model_get_multivariate_event_collections_response = cls(
            cursor=cursor,
            multivariate_contracts=multivariate_contracts,
        )

        model_get_multivariate_event_collections_response.additional_properties = d
        return model_get_multivariate_event_collections_response

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
