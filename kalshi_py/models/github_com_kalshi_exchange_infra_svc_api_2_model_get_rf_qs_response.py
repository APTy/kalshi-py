from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_get_rf_qs_response_rfqs_item import (
        GithubComKalshiExchangeInfraSvcApi2ModelGetRFQsResponseRfqsItem,
    )


T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelGetRFQsResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelGetRFQsResponse:
    """
    Attributes:
        cursor (Union[Unset, str]): Cursor for pagination to get the next page of results.
        rfqs (Union[Unset, list['GithubComKalshiExchangeInfraSvcApi2ModelGetRFQsResponseRfqsItem']]): List of RFQs
            matching the query criteria.
    """

    cursor: Union[Unset, str] = UNSET
    rfqs: Union[Unset, list["GithubComKalshiExchangeInfraSvcApi2ModelGetRFQsResponseRfqsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursor = self.cursor

        rfqs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rfqs, Unset):
            rfqs = []
            for rfqs_item_data in self.rfqs:
                rfqs_item = rfqs_item_data.to_dict()
                rfqs.append(rfqs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if rfqs is not UNSET:
            field_dict["rfqs"] = rfqs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_get_rf_qs_response_rfqs_item import (
            GithubComKalshiExchangeInfraSvcApi2ModelGetRFQsResponseRfqsItem,
        )

        d = dict(src_dict)
        cursor = d.pop("cursor", UNSET)

        rfqs = []
        _rfqs = d.pop("rfqs", UNSET)
        for rfqs_item_data in _rfqs or []:
            rfqs_item = GithubComKalshiExchangeInfraSvcApi2ModelGetRFQsResponseRfqsItem.from_dict(rfqs_item_data)

            rfqs.append(rfqs_item)

        github_com_kalshi_exchange_infra_svc_api_2_model_get_rf_qs_response = cls(
            cursor=cursor,
            rfqs=rfqs,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_get_rf_qs_response.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_get_rf_qs_response

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
