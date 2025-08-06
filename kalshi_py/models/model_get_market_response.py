from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_market import ModelMarket


T = TypeVar("T", bound="ModelGetMarketResponse")


@_attrs_define
class ModelGetMarketResponse:
    """
    Attributes:
        market (Union[Unset, ModelMarket]): Contains information about a market
    """

    market: Union[Unset, "ModelMarket"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        market: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.market, Unset):
            market = self.market.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if market is not UNSET:
            field_dict["market"] = market

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_market import ModelMarket

        d = dict(src_dict)
        _market = d.pop("market", UNSET)
        market: Union[Unset, ModelMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = ModelMarket.from_dict(_market)

        model_get_market_response = cls(
            market=market,
        )

        model_get_market_response.additional_properties = d
        return model_get_market_response

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
