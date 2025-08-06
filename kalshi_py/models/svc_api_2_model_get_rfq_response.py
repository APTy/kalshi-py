from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.common_communications_rfq import CommonCommunicationsRFQ


T = TypeVar("T", bound="SvcApi2ModelGetRFQResponse")


@_attrs_define
class SvcApi2ModelGetRFQResponse:
    """
    Attributes:
        rfq (Union[Unset, CommonCommunicationsRFQ]):
    """

    rfq: Union[Unset, "CommonCommunicationsRFQ"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rfq: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rfq, Unset):
            rfq = self.rfq.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rfq is not UNSET:
            field_dict["rfq"] = rfq

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.common_communications_rfq import CommonCommunicationsRFQ

        d = dict(src_dict)
        _rfq = d.pop("rfq", UNSET)
        rfq: Union[Unset, CommonCommunicationsRFQ]
        if isinstance(_rfq, Unset):
            rfq = UNSET
        else:
            rfq = CommonCommunicationsRFQ.from_dict(_rfq)

        svc_api_2_model_get_rfq_response = cls(
            rfq=rfq,
        )

        svc_api_2_model_get_rfq_response.additional_properties = d
        return svc_api_2_model_get_rfq_response

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
