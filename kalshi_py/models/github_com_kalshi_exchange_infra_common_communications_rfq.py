import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraCommonCommunicationsRFQ")


@_attrs_define
class GithubComKalshiExchangeInfraCommonCommunicationsRFQ:
    """
    Attributes:
        cancellation_reason (Union[Unset, str]): Reason for RFQ cancellation if cancelled.
        cancelled_ts (Union[Unset, datetime.datetime]): Timestamp when the RFQ was cancelled.
        contracts (Union[Unset, int]): Number of contracts requested in the RFQ.
        created_ts (Union[Unset, datetime.datetime]): Timestamp when the RFQ was created.
        creator_id (Union[Unset, str]):
        creator_user_id (Union[Unset, str]):
        id (Union[Unset, str]):
        market_ticker (Union[Unset, str]): The ticker of the market this RFQ is for.
        rest_remainder (Union[Unset, bool]): Whether to rest the remainder of the RFQ after execution.
        status (Union[Unset, str]):
        updated_ts (Union[Unset, datetime.datetime]): Timestamp when the RFQ was last updated.
    """

    cancellation_reason: Union[Unset, str] = UNSET
    cancelled_ts: Union[Unset, datetime.datetime] = UNSET
    contracts: Union[Unset, int] = UNSET
    created_ts: Union[Unset, datetime.datetime] = UNSET
    creator_id: Union[Unset, str] = UNSET
    creator_user_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    market_ticker: Union[Unset, str] = UNSET
    rest_remainder: Union[Unset, bool] = UNSET
    status: Union[Unset, str] = UNSET
    updated_ts: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cancellation_reason = self.cancellation_reason

        cancelled_ts: Union[Unset, str] = UNSET
        if not isinstance(self.cancelled_ts, Unset):
            cancelled_ts = self.cancelled_ts.isoformat()

        contracts = self.contracts

        created_ts: Union[Unset, str] = UNSET
        if not isinstance(self.created_ts, Unset):
            created_ts = self.created_ts.isoformat()

        creator_id = self.creator_id

        creator_user_id = self.creator_user_id

        id = self.id

        market_ticker = self.market_ticker

        rest_remainder = self.rest_remainder

        status = self.status

        updated_ts: Union[Unset, str] = UNSET
        if not isinstance(self.updated_ts, Unset):
            updated_ts = self.updated_ts.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cancellation_reason is not UNSET:
            field_dict["cancellation_reason"] = cancellation_reason
        if cancelled_ts is not UNSET:
            field_dict["cancelled_ts"] = cancelled_ts
        if contracts is not UNSET:
            field_dict["contracts"] = contracts
        if created_ts is not UNSET:
            field_dict["created_ts"] = created_ts
        if creator_id is not UNSET:
            field_dict["creator_id"] = creator_id
        if creator_user_id is not UNSET:
            field_dict["creator_user_id"] = creator_user_id
        if id is not UNSET:
            field_dict["id"] = id
        if market_ticker is not UNSET:
            field_dict["market_ticker"] = market_ticker
        if rest_remainder is not UNSET:
            field_dict["rest_remainder"] = rest_remainder
        if status is not UNSET:
            field_dict["status"] = status
        if updated_ts is not UNSET:
            field_dict["updated_ts"] = updated_ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cancellation_reason = d.pop("cancellation_reason", UNSET)

        _cancelled_ts = d.pop("cancelled_ts", UNSET)
        cancelled_ts: Union[Unset, datetime.datetime]
        if isinstance(_cancelled_ts, Unset):
            cancelled_ts = UNSET
        else:
            cancelled_ts = isoparse(_cancelled_ts)

        contracts = d.pop("contracts", UNSET)

        _created_ts = d.pop("created_ts", UNSET)
        created_ts: Union[Unset, datetime.datetime]
        if isinstance(_created_ts, Unset):
            created_ts = UNSET
        else:
            created_ts = isoparse(_created_ts)

        creator_id = d.pop("creator_id", UNSET)

        creator_user_id = d.pop("creator_user_id", UNSET)

        id = d.pop("id", UNSET)

        market_ticker = d.pop("market_ticker", UNSET)

        rest_remainder = d.pop("rest_remainder", UNSET)

        status = d.pop("status", UNSET)

        _updated_ts = d.pop("updated_ts", UNSET)
        updated_ts: Union[Unset, datetime.datetime]
        if isinstance(_updated_ts, Unset):
            updated_ts = UNSET
        else:
            updated_ts = isoparse(_updated_ts)

        github_com_kalshi_exchange_infra_common_communications_rfq = cls(
            cancellation_reason=cancellation_reason,
            cancelled_ts=cancelled_ts,
            contracts=contracts,
            created_ts=created_ts,
            creator_id=creator_id,
            creator_user_id=creator_user_id,
            id=id,
            market_ticker=market_ticker,
            rest_remainder=rest_remainder,
            status=status,
            updated_ts=updated_ts,
        )

        github_com_kalshi_exchange_infra_common_communications_rfq.additional_properties = d
        return github_com_kalshi_exchange_infra_common_communications_rfq

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
