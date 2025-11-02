from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quote import Quote


T = TypeVar("T", bound="GetQuotesResponse")


@_attrs_define
class GetQuotesResponse:
    """
    Attributes:
        quotes (list['Quote']): List of quotes matching the query criteria
        cursor (Union[Unset, str]): Cursor for pagination to get the next page of results
    """

    quotes: list["Quote"]
    cursor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quotes = []
        for quotes_item_data in self.quotes:
            quotes_item = quotes_item_data.to_dict()
            quotes.append(quotes_item)

        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quotes": quotes,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quote import Quote

        d = dict(src_dict)
        quotes = []
        _quotes = d.pop("quotes")
        for quotes_item_data in _quotes:
            quotes_item = Quote.from_dict(quotes_item_data)

            quotes.append(quotes_item)

        cursor = d.pop("cursor", UNSET)

        get_quotes_response = cls(
            quotes=quotes,
            cursor=cursor,
        )

        get_quotes_response.additional_properties = d
        return get_quotes_response

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
