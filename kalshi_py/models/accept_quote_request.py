from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.accept_quote_request_accepted_side import AcceptQuoteRequestAcceptedSide

T = TypeVar("T", bound="AcceptQuoteRequest")


@_attrs_define
class AcceptQuoteRequest:
    """
    Attributes:
        accepted_side (AcceptQuoteRequestAcceptedSide): The side of the quote to accept (yes or no)
    """

    accepted_side: AcceptQuoteRequestAcceptedSide
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepted_side = self.accepted_side.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accepted_side": accepted_side,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accepted_side = AcceptQuoteRequestAcceptedSide(d.pop("accepted_side"))

        accept_quote_request = cls(
            accepted_side=accepted_side,
        )

        accept_quote_request.additional_properties = d
        return accept_quote_request

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
