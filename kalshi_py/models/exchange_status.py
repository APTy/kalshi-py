import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExchangeStatus")


@_attrs_define
class ExchangeStatus:
    """
    Attributes:
        exchange_active (bool): False if the core Kalshi exchange is no longer taking any state changes at all. This
            includes but is not limited to trading, new users, and transfers. True unless we are under maintenance.
        trading_active (bool): True if we are currently permitting trading on the exchange. This is true during trading
            hours and false outside exchange hours. Kalshi reserves the right to pause at any time in case issues are
            detected.
        exchange_estimated_resume_time (Union[None, Unset, datetime.datetime]): Estimated downtime for the current
            exchange maintenance window. However, this is not guaranteed and can be extended.
    """

    exchange_active: bool
    trading_active: bool
    exchange_estimated_resume_time: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchange_active = self.exchange_active

        trading_active = self.trading_active

        exchange_estimated_resume_time: Union[None, Unset, str]
        if isinstance(self.exchange_estimated_resume_time, Unset):
            exchange_estimated_resume_time = UNSET
        elif isinstance(self.exchange_estimated_resume_time, datetime.datetime):
            exchange_estimated_resume_time = self.exchange_estimated_resume_time.isoformat()
        else:
            exchange_estimated_resume_time = self.exchange_estimated_resume_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exchange_active": exchange_active,
                "trading_active": trading_active,
            }
        )
        if exchange_estimated_resume_time is not UNSET:
            field_dict["exchange_estimated_resume_time"] = exchange_estimated_resume_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exchange_active = d.pop("exchange_active")

        trading_active = d.pop("trading_active")

        def _parse_exchange_estimated_resume_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                exchange_estimated_resume_time_type_0 = isoparse(data)

                return exchange_estimated_resume_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        exchange_estimated_resume_time = _parse_exchange_estimated_resume_time(
            d.pop("exchange_estimated_resume_time", UNSET)
        )

        exchange_status = cls(
            exchange_active=exchange_active,
            trading_active=trading_active,
            exchange_estimated_resume_time=exchange_estimated_resume_time,
        )

        exchange_status.additional_properties = d
        return exchange_status

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
