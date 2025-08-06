from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_order_book_no_dollars_item import (
        GithubComKalshiExchangeInfraSvcApi2ModelOrderBookNoDollarsItem,
    )
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_order_book_yes_dollars_item import (
        GithubComKalshiExchangeInfraSvcApi2ModelOrderBookYesDollarsItem,
    )


T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelOrderBook")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelOrderBook:
    """
    Attributes:
        no (Union[Unset, list[list[int]]]): Array of price levels for no orders. Each level is [price, quantity] where
            price is in cents or centicents based on use_centi_cent parameter.
        no_dollars (Union[Unset, list['GithubComKalshiExchangeInfraSvcApi2ModelOrderBookNoDollarsItem']]): Array of
            price levels for no orders. Each level is {price, quantity} where price is in dollars.
        yes (Union[Unset, list[list[int]]]): Array of price levels for yes orders. Each level is [price, quantity] where
            price is in cents or centicents based on use_centi_cent parameter.
        yes_dollars (Union[Unset, list['GithubComKalshiExchangeInfraSvcApi2ModelOrderBookYesDollarsItem']]): Array of
            price levels for yes orders. Each level is {price, quantity} where price is in dollars.
    """

    no: Union[Unset, list[list[int]]] = UNSET
    no_dollars: Union[Unset, list["GithubComKalshiExchangeInfraSvcApi2ModelOrderBookNoDollarsItem"]] = UNSET
    yes: Union[Unset, list[list[int]]] = UNSET
    yes_dollars: Union[Unset, list["GithubComKalshiExchangeInfraSvcApi2ModelOrderBookYesDollarsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        no: Union[Unset, list[list[int]]] = UNSET
        if not isinstance(self.no, Unset):
            no = []
            for no_item_data in self.no:
                no_item = no_item_data

                no.append(no_item)

        no_dollars: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.no_dollars, Unset):
            no_dollars = []
            for no_dollars_item_data in self.no_dollars:
                no_dollars_item = no_dollars_item_data.to_dict()
                no_dollars.append(no_dollars_item)

        yes: Union[Unset, list[list[int]]] = UNSET
        if not isinstance(self.yes, Unset):
            yes = []
            for yes_item_data in self.yes:
                yes_item = yes_item_data

                yes.append(yes_item)

        yes_dollars: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.yes_dollars, Unset):
            yes_dollars = []
            for yes_dollars_item_data in self.yes_dollars:
                yes_dollars_item = yes_dollars_item_data.to_dict()
                yes_dollars.append(yes_dollars_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if no is not UNSET:
            field_dict["no"] = no
        if no_dollars is not UNSET:
            field_dict["no_dollars"] = no_dollars
        if yes is not UNSET:
            field_dict["yes"] = yes
        if yes_dollars is not UNSET:
            field_dict["yes_dollars"] = yes_dollars

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_order_book_no_dollars_item import (
            GithubComKalshiExchangeInfraSvcApi2ModelOrderBookNoDollarsItem,
        )
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_order_book_yes_dollars_item import (
            GithubComKalshiExchangeInfraSvcApi2ModelOrderBookYesDollarsItem,
        )

        d = dict(src_dict)
        no = []
        _no = d.pop("no", UNSET)
        for no_item_data in _no or []:
            no_item = cast(list[int], no_item_data)

            no.append(no_item)

        no_dollars = []
        _no_dollars = d.pop("no_dollars", UNSET)
        for no_dollars_item_data in _no_dollars or []:
            no_dollars_item = GithubComKalshiExchangeInfraSvcApi2ModelOrderBookNoDollarsItem.from_dict(
                no_dollars_item_data
            )

            no_dollars.append(no_dollars_item)

        yes = []
        _yes = d.pop("yes", UNSET)
        for yes_item_data in _yes or []:
            yes_item = cast(list[int], yes_item_data)

            yes.append(yes_item)

        yes_dollars = []
        _yes_dollars = d.pop("yes_dollars", UNSET)
        for yes_dollars_item_data in _yes_dollars or []:
            yes_dollars_item = GithubComKalshiExchangeInfraSvcApi2ModelOrderBookYesDollarsItem.from_dict(
                yes_dollars_item_data
            )

            yes_dollars.append(yes_dollars_item)

        github_com_kalshi_exchange_infra_svc_api_2_model_order_book = cls(
            no=no,
            no_dollars=no_dollars,
            yes=yes,
            yes_dollars=yes_dollars,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_order_book.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_order_book

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
