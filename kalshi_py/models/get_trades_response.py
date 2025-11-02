from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trade import Trade


T = TypeVar("T", bound="GetTradesResponse")


@_attrs_define
class GetTradesResponse:
    """
    Attributes:
        trades (Union[Unset, list['Trade']]):
        cursor (Union[Unset, str]):
    """

    trades: Union[Unset, list["Trade"]] = UNSET
    cursor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trades: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.trades, Unset):
            trades = []
            for trades_item_data in self.trades:
                trades_item = trades_item_data.to_dict()
                trades.append(trades_item)

        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trades is not UNSET:
            field_dict["trades"] = trades
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trade import Trade

        d = dict(src_dict)
        trades = []
        _trades = d.pop("trades", UNSET)
        for trades_item_data in _trades or []:
            trades_item = Trade.from_dict(trades_item_data)

            trades.append(trades_item)

        cursor = d.pop("cursor", UNSET)

        get_trades_response = cls(
            trades=trades,
            cursor=cursor,
        )

        get_trades_response.additional_properties = d
        return get_trades_response

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
