import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraCommonCommunicationsQuote")


@_attrs_define
class GithubComKalshiExchangeInfraCommonCommunicationsQuote:
    """
    Attributes:
        accepted_side (Union[Unset, str]): The side that was accepted (yes or no).
        accepted_ts (Union[Unset, datetime.datetime]): Timestamp when the quote was accepted.
        cancellation_reason (Union[Unset, str]): Reason for quote cancellation if cancelled.
        cancelled_ts (Union[Unset, datetime.datetime]): Timestamp when the quote was cancelled.
        confirmed_ts (Union[Unset, datetime.datetime]): Timestamp when the quote was confirmed.
        contracts (Union[Unset, int]): Number of contracts in the quote.
        created_ts (Union[Unset, datetime.datetime]): Timestamp when the quote was created.
        creator_id (Union[Unset, str]):
        creator_order_id (Union[Unset, str]):
        creator_user_id (Union[Unset, str]):
        executed_ts (Union[Unset, datetime.datetime]): Timestamp when the quote was executed.
        id (Union[Unset, str]):
        market_ticker (Union[Unset, str]): The ticker of the market this quote is for.
        no_bid (Union[Unset, int]):
        rest_remainder (Union[Unset, bool]): Whether to rest the remainder of the quote after execution.
        rfq_creator_id (Union[Unset, str]):
        rfq_creator_order_id (Union[Unset, str]):
        rfq_creator_user_id (Union[Unset, str]):
        rfq_id (Union[Unset, str]):
        status (Union[Unset, str]):
        updated_ts (Union[Unset, datetime.datetime]): Timestamp when the quote was last updated.
        yes_bid (Union[Unset, int]):
    """

    accepted_side: Union[Unset, str] = UNSET
    accepted_ts: Union[Unset, datetime.datetime] = UNSET
    cancellation_reason: Union[Unset, str] = UNSET
    cancelled_ts: Union[Unset, datetime.datetime] = UNSET
    confirmed_ts: Union[Unset, datetime.datetime] = UNSET
    contracts: Union[Unset, int] = UNSET
    created_ts: Union[Unset, datetime.datetime] = UNSET
    creator_id: Union[Unset, str] = UNSET
    creator_order_id: Union[Unset, str] = UNSET
    creator_user_id: Union[Unset, str] = UNSET
    executed_ts: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    market_ticker: Union[Unset, str] = UNSET
    no_bid: Union[Unset, int] = UNSET
    rest_remainder: Union[Unset, bool] = UNSET
    rfq_creator_id: Union[Unset, str] = UNSET
    rfq_creator_order_id: Union[Unset, str] = UNSET
    rfq_creator_user_id: Union[Unset, str] = UNSET
    rfq_id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    updated_ts: Union[Unset, datetime.datetime] = UNSET
    yes_bid: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepted_side = self.accepted_side

        accepted_ts: Union[Unset, str] = UNSET
        if not isinstance(self.accepted_ts, Unset):
            accepted_ts = self.accepted_ts.isoformat()

        cancellation_reason = self.cancellation_reason

        cancelled_ts: Union[Unset, str] = UNSET
        if not isinstance(self.cancelled_ts, Unset):
            cancelled_ts = self.cancelled_ts.isoformat()

        confirmed_ts: Union[Unset, str] = UNSET
        if not isinstance(self.confirmed_ts, Unset):
            confirmed_ts = self.confirmed_ts.isoformat()

        contracts = self.contracts

        created_ts: Union[Unset, str] = UNSET
        if not isinstance(self.created_ts, Unset):
            created_ts = self.created_ts.isoformat()

        creator_id = self.creator_id

        creator_order_id = self.creator_order_id

        creator_user_id = self.creator_user_id

        executed_ts: Union[Unset, str] = UNSET
        if not isinstance(self.executed_ts, Unset):
            executed_ts = self.executed_ts.isoformat()

        id = self.id

        market_ticker = self.market_ticker

        no_bid = self.no_bid

        rest_remainder = self.rest_remainder

        rfq_creator_id = self.rfq_creator_id

        rfq_creator_order_id = self.rfq_creator_order_id

        rfq_creator_user_id = self.rfq_creator_user_id

        rfq_id = self.rfq_id

        status = self.status

        updated_ts: Union[Unset, str] = UNSET
        if not isinstance(self.updated_ts, Unset):
            updated_ts = self.updated_ts.isoformat()

        yes_bid = self.yes_bid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accepted_side is not UNSET:
            field_dict["accepted_side"] = accepted_side
        if accepted_ts is not UNSET:
            field_dict["accepted_ts"] = accepted_ts
        if cancellation_reason is not UNSET:
            field_dict["cancellation_reason"] = cancellation_reason
        if cancelled_ts is not UNSET:
            field_dict["cancelled_ts"] = cancelled_ts
        if confirmed_ts is not UNSET:
            field_dict["confirmed_ts"] = confirmed_ts
        if contracts is not UNSET:
            field_dict["contracts"] = contracts
        if created_ts is not UNSET:
            field_dict["created_ts"] = created_ts
        if creator_id is not UNSET:
            field_dict["creator_id"] = creator_id
        if creator_order_id is not UNSET:
            field_dict["creator_order_id"] = creator_order_id
        if creator_user_id is not UNSET:
            field_dict["creator_user_id"] = creator_user_id
        if executed_ts is not UNSET:
            field_dict["executed_ts"] = executed_ts
        if id is not UNSET:
            field_dict["id"] = id
        if market_ticker is not UNSET:
            field_dict["market_ticker"] = market_ticker
        if no_bid is not UNSET:
            field_dict["no_bid"] = no_bid
        if rest_remainder is not UNSET:
            field_dict["rest_remainder"] = rest_remainder
        if rfq_creator_id is not UNSET:
            field_dict["rfq_creator_id"] = rfq_creator_id
        if rfq_creator_order_id is not UNSET:
            field_dict["rfq_creator_order_id"] = rfq_creator_order_id
        if rfq_creator_user_id is not UNSET:
            field_dict["rfq_creator_user_id"] = rfq_creator_user_id
        if rfq_id is not UNSET:
            field_dict["rfq_id"] = rfq_id
        if status is not UNSET:
            field_dict["status"] = status
        if updated_ts is not UNSET:
            field_dict["updated_ts"] = updated_ts
        if yes_bid is not UNSET:
            field_dict["yes_bid"] = yes_bid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accepted_side = d.pop("accepted_side", UNSET)

        _accepted_ts = d.pop("accepted_ts", UNSET)
        accepted_ts: Union[Unset, datetime.datetime]
        if isinstance(_accepted_ts, Unset):
            accepted_ts = UNSET
        else:
            accepted_ts = isoparse(_accepted_ts)

        cancellation_reason = d.pop("cancellation_reason", UNSET)

        _cancelled_ts = d.pop("cancelled_ts", UNSET)
        cancelled_ts: Union[Unset, datetime.datetime]
        if isinstance(_cancelled_ts, Unset):
            cancelled_ts = UNSET
        else:
            cancelled_ts = isoparse(_cancelled_ts)

        _confirmed_ts = d.pop("confirmed_ts", UNSET)
        confirmed_ts: Union[Unset, datetime.datetime]
        if isinstance(_confirmed_ts, Unset):
            confirmed_ts = UNSET
        else:
            confirmed_ts = isoparse(_confirmed_ts)

        contracts = d.pop("contracts", UNSET)

        _created_ts = d.pop("created_ts", UNSET)
        created_ts: Union[Unset, datetime.datetime]
        if isinstance(_created_ts, Unset):
            created_ts = UNSET
        else:
            created_ts = isoparse(_created_ts)

        creator_id = d.pop("creator_id", UNSET)

        creator_order_id = d.pop("creator_order_id", UNSET)

        creator_user_id = d.pop("creator_user_id", UNSET)

        _executed_ts = d.pop("executed_ts", UNSET)
        executed_ts: Union[Unset, datetime.datetime]
        if isinstance(_executed_ts, Unset):
            executed_ts = UNSET
        else:
            executed_ts = isoparse(_executed_ts)

        id = d.pop("id", UNSET)

        market_ticker = d.pop("market_ticker", UNSET)

        no_bid = d.pop("no_bid", UNSET)

        rest_remainder = d.pop("rest_remainder", UNSET)

        rfq_creator_id = d.pop("rfq_creator_id", UNSET)

        rfq_creator_order_id = d.pop("rfq_creator_order_id", UNSET)

        rfq_creator_user_id = d.pop("rfq_creator_user_id", UNSET)

        rfq_id = d.pop("rfq_id", UNSET)

        status = d.pop("status", UNSET)

        _updated_ts = d.pop("updated_ts", UNSET)
        updated_ts: Union[Unset, datetime.datetime]
        if isinstance(_updated_ts, Unset):
            updated_ts = UNSET
        else:
            updated_ts = isoparse(_updated_ts)

        yes_bid = d.pop("yes_bid", UNSET)

        github_com_kalshi_exchange_infra_common_communications_quote = cls(
            accepted_side=accepted_side,
            accepted_ts=accepted_ts,
            cancellation_reason=cancellation_reason,
            cancelled_ts=cancelled_ts,
            confirmed_ts=confirmed_ts,
            contracts=contracts,
            created_ts=created_ts,
            creator_id=creator_id,
            creator_order_id=creator_order_id,
            creator_user_id=creator_user_id,
            executed_ts=executed_ts,
            id=id,
            market_ticker=market_ticker,
            no_bid=no_bid,
            rest_remainder=rest_remainder,
            rfq_creator_id=rfq_creator_id,
            rfq_creator_order_id=rfq_creator_order_id,
            rfq_creator_user_id=rfq_creator_user_id,
            rfq_id=rfq_id,
            status=status,
            updated_ts=updated_ts,
            yes_bid=yes_bid,
        )

        github_com_kalshi_exchange_infra_common_communications_quote.additional_properties = d
        return github_com_kalshi_exchange_infra_common_communications_quote

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
