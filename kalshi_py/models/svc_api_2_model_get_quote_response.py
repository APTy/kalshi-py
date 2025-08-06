from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.common_communications_quote import CommonCommunicationsQuote


T = TypeVar("T", bound="SvcApi2ModelGetQuoteResponse")


@_attrs_define
class SvcApi2ModelGetQuoteResponse:
    """
    Attributes:
        quote (Union[Unset, CommonCommunicationsQuote]):
    """

    quote: Union[Unset, "CommonCommunicationsQuote"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quote: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quote, Unset):
            quote = self.quote.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quote is not UNSET:
            field_dict["quote"] = quote

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.common_communications_quote import CommonCommunicationsQuote

        d = dict(src_dict)
        _quote = d.pop("quote", UNSET)
        quote: Union[Unset, CommonCommunicationsQuote]
        if isinstance(_quote, Unset):
            quote = UNSET
        else:
            quote = CommonCommunicationsQuote.from_dict(_quote)

        svc_api_2_model_get_quote_response = cls(
            quote=quote,
        )

        svc_api_2_model_get_quote_response.additional_properties = d
        return svc_api_2_model_get_quote_response

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
