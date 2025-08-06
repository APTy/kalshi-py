from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.svc_api_2_model_user_get_api_keys_response_api_keys_item import (
        SvcApi2ModelUserGetApiKeysResponseApiKeysItem,
    )


T = TypeVar("T", bound="SvcApi2ModelUserGetApiKeysResponse")


@_attrs_define
class SvcApi2ModelUserGetApiKeysResponse:
    """
    Attributes:
        api_keys (Union[Unset, list['SvcApi2ModelUserGetApiKeysResponseApiKeysItem']]): List of all API keys associated
            with the user.
    """

    api_keys: Union[Unset, list["SvcApi2ModelUserGetApiKeysResponseApiKeysItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_keys: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.api_keys, Unset):
            api_keys = []
            for api_keys_item_data in self.api_keys:
                api_keys_item = api_keys_item_data.to_dict()
                api_keys.append(api_keys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_keys is not UNSET:
            field_dict["api_keys"] = api_keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.svc_api_2_model_user_get_api_keys_response_api_keys_item import (
            SvcApi2ModelUserGetApiKeysResponseApiKeysItem,
        )

        d = dict(src_dict)
        api_keys = []
        _api_keys = d.pop("api_keys", UNSET)
        for api_keys_item_data in _api_keys or []:
            api_keys_item = SvcApi2ModelUserGetApiKeysResponseApiKeysItem.from_dict(api_keys_item_data)

            api_keys.append(api_keys_item)

        svc_api_2_model_user_get_api_keys_response = cls(
            api_keys=api_keys,
        )

        svc_api_2_model_user_get_api_keys_response.additional_properties = d
        return svc_api_2_model_user_get_api_keys_response

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
