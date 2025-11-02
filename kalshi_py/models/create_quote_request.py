from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateQuoteRequest")


@_attrs_define
class CreateQuoteRequest:
    """
    Attributes:
        rfq_id (str): The ID of the RFQ to quote on
        yes_bid (str): The bid price for YES contracts, in dollars
        no_bid (str): The bid price for NO contracts, in dollars
        rest_remainder (bool): Whether to rest the remainder of the quote after execution
    """

    rfq_id: str
    yes_bid: str
    no_bid: str
    rest_remainder: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rfq_id = self.rfq_id

        yes_bid = self.yes_bid

        no_bid = self.no_bid

        rest_remainder = self.rest_remainder

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rfq_id": rfq_id,
                "yes_bid": yes_bid,
                "no_bid": no_bid,
                "rest_remainder": rest_remainder,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rfq_id = d.pop("rfq_id")

        yes_bid = d.pop("yes_bid")

        no_bid = d.pop("no_bid")

        rest_remainder = d.pop("rest_remainder")

        create_quote_request = cls(
            rfq_id=rfq_id,
            yes_bid=yes_bid,
            no_bid=no_bid,
            rest_remainder=rest_remainder,
        )

        create_quote_request.additional_properties = d
        return create_quote_request

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
