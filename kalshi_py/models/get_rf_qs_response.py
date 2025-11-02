from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rfq import RFQ


T = TypeVar("T", bound="GetRFQsResponse")


@_attrs_define
class GetRFQsResponse:
    """
    Attributes:
        rfqs (list['RFQ']): List of RFQs matching the query criteria
        cursor (Union[Unset, str]): Cursor for pagination to get the next page of results
    """

    rfqs: list["RFQ"]
    cursor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rfqs = []
        for rfqs_item_data in self.rfqs:
            rfqs_item = rfqs_item_data.to_dict()
            rfqs.append(rfqs_item)

        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rfqs": rfqs,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rfq import RFQ

        d = dict(src_dict)
        rfqs = []
        _rfqs = d.pop("rfqs")
        for rfqs_item_data in _rfqs:
            rfqs_item = RFQ.from_dict(rfqs_item_data)

            rfqs.append(rfqs_item)

        cursor = d.pop("cursor", UNSET)

        get_rf_qs_response = cls(
            rfqs=rfqs,
            cursor=cursor,
        )

        get_rf_qs_response.additional_properties = d
        return get_rf_qs_response

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
