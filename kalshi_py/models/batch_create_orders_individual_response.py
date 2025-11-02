from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_response import ErrorResponse
    from ..models.order import Order


T = TypeVar("T", bound="BatchCreateOrdersIndividualResponse")


@_attrs_define
class BatchCreateOrdersIndividualResponse:
    """
    Attributes:
        client_order_id (Union[None, Unset, str]):
        order (Union['Order', None, Unset]):
        error (Union['ErrorResponse', None, Unset]):
    """

    client_order_id: Union[None, Unset, str] = UNSET
    order: Union["Order", None, Unset] = UNSET
    error: Union["ErrorResponse", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.error_response import ErrorResponse
        from ..models.order import Order

        client_order_id: Union[None, Unset, str]
        if isinstance(self.client_order_id, Unset):
            client_order_id = UNSET
        else:
            client_order_id = self.client_order_id

        order: Union[None, Unset, dict[str, Any]]
        if isinstance(self.order, Unset):
            order = UNSET
        elif isinstance(self.order, Order):
            order = self.order.to_dict()
        else:
            order = self.order

        error: Union[None, Unset, dict[str, Any]]
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, ErrorResponse):
            error = self.error.to_dict()
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_order_id is not UNSET:
            field_dict["client_order_id"] = client_order_id
        if order is not UNSET:
            field_dict["order"] = order
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_response import ErrorResponse
        from ..models.order import Order

        d = dict(src_dict)

        def _parse_client_order_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        client_order_id = _parse_client_order_id(d.pop("client_order_id", UNSET))

        def _parse_order(data: object) -> Union["Order", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                order_type_1 = Order.from_dict(data)

                return order_type_1
            except:  # noqa: E722
                pass
            return cast(Union["Order", None, Unset], data)

        order = _parse_order(d.pop("order", UNSET))

        def _parse_error(data: object) -> Union["ErrorResponse", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_1 = ErrorResponse.from_dict(data)

                return error_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ErrorResponse", None, Unset], data)

        error = _parse_error(d.pop("error", UNSET))

        batch_create_orders_individual_response = cls(
            client_order_id=client_order_id,
            order=order,
            error=error,
        )

        batch_create_orders_individual_response.additional_properties = d
        return batch_create_orders_individual_response

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
