from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelExchangeStatus")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelExchangeStatus:
    """
    Attributes:
        exchange_active (Union[Unset, bool]): False if the core Kalshi exchange is no longer taking any state changes at
            all. This includes but is not limited to trading, new users, and transfers. True unless we are under
            maintenance.
        exchange_estimated_resume_time (Union[Unset, Any]):
        trading_active (Union[Unset, bool]): True if we are currently permitting trading on the exchange. This is true
            during trading hours and false outside exchange hours. Kalshi reserves the right to pause at any time in case
            issues are detected.
    """

    exchange_active: Union[Unset, bool] = UNSET
    exchange_estimated_resume_time: Union[Unset, Any] = UNSET
    trading_active: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchange_active = self.exchange_active

        exchange_estimated_resume_time = self.exchange_estimated_resume_time

        trading_active = self.trading_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exchange_active is not UNSET:
            field_dict["exchange_active"] = exchange_active
        if exchange_estimated_resume_time is not UNSET:
            field_dict["exchange_estimated_resume_time"] = exchange_estimated_resume_time
        if trading_active is not UNSET:
            field_dict["trading_active"] = trading_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exchange_active = d.pop("exchange_active", UNSET)

        exchange_estimated_resume_time = d.pop("exchange_estimated_resume_time", UNSET)

        trading_active = d.pop("trading_active", UNSET)

        github_com_kalshi_exchange_infra_svc_api_2_model_exchange_status = cls(
            exchange_active=exchange_active,
            exchange_estimated_resume_time=exchange_estimated_resume_time,
            trading_active=trading_active,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_exchange_status.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_exchange_status

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
