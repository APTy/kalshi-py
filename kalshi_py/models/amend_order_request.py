from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.amend_order_request_action import AmendOrderRequestAction
from ..models.amend_order_request_side import AmendOrderRequestSide
from ..types import UNSET, Unset

T = TypeVar("T", bound="AmendOrderRequest")


@_attrs_define
class AmendOrderRequest:
    """
    Attributes:
        ticker (str): Market ticker
        side (AmendOrderRequestSide): Side of the order
        action (AmendOrderRequestAction): Action of the order
        client_order_id (str): The original client-specified order ID to be amended
        updated_client_order_id (str): The new client-specified order ID after amendment
        yes_price (Union[Unset, float]): Updated yes price for the order in cents
        no_price (Union[Unset, float]): Updated no price for the order in cents
        yes_price_dollars (Union[Unset, str]): Updated yes price for the order in fixed-point dollars. Exactly one of
            yes_price, no_price, yes_price_dollars, and no_price_dollars must be passed.
        no_price_dollars (Union[Unset, str]): Updated no price for the order in fixed-point dollars. Exactly one of
            yes_price, no_price, yes_price_dollars, and no_price_dollars must be passed.
        count (Union[Unset, int]): Updated quantity for the order
    """

    ticker: str
    side: AmendOrderRequestSide
    action: AmendOrderRequestAction
    client_order_id: str
    updated_client_order_id: str
    yes_price: Union[Unset, float] = UNSET
    no_price: Union[Unset, float] = UNSET
    yes_price_dollars: Union[Unset, str] = UNSET
    no_price_dollars: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticker = self.ticker

        side = self.side.value

        action = self.action.value

        client_order_id = self.client_order_id

        updated_client_order_id = self.updated_client_order_id

        yes_price = self.yes_price

        no_price = self.no_price

        yes_price_dollars = self.yes_price_dollars

        no_price_dollars = self.no_price_dollars

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticker": ticker,
                "side": side,
                "action": action,
                "client_order_id": client_order_id,
                "updated_client_order_id": updated_client_order_id,
            }
        )
        if yes_price is not UNSET:
            field_dict["yes_price"] = yes_price
        if no_price is not UNSET:
            field_dict["no_price"] = no_price
        if yes_price_dollars is not UNSET:
            field_dict["yes_price_dollars"] = yes_price_dollars
        if no_price_dollars is not UNSET:
            field_dict["no_price_dollars"] = no_price_dollars
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ticker = d.pop("ticker")

        side = AmendOrderRequestSide(d.pop("side"))

        action = AmendOrderRequestAction(d.pop("action"))

        client_order_id = d.pop("client_order_id")

        updated_client_order_id = d.pop("updated_client_order_id")

        yes_price = d.pop("yes_price", UNSET)

        no_price = d.pop("no_price", UNSET)

        yes_price_dollars = d.pop("yes_price_dollars", UNSET)

        no_price_dollars = d.pop("no_price_dollars", UNSET)

        count = d.pop("count", UNSET)

        amend_order_request = cls(
            ticker=ticker,
            side=side,
            action=action,
            client_order_id=client_order_id,
            updated_client_order_id=updated_client_order_id,
            yes_price=yes_price,
            no_price=no_price,
            yes_price_dollars=yes_price_dollars,
            no_price_dollars=no_price_dollars,
            count=count,
        )

        amend_order_request.additional_properties = d
        return amend_order_request

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
