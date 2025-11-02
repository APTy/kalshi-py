import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.quote_accepted_side import QuoteAcceptedSide
from ..models.quote_status import QuoteStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Quote")


@_attrs_define
class Quote:
    """
    Attributes:
        id (str): Unique identifier for the quote
        rfq_id (str): ID of the RFQ this quote is responding to
        creator_id (str): Public communications ID of the quote creator
        rfq_creator_id (str): Public communications ID of the RFQ creator
        market_ticker (str): The ticker of the market this quote is for
        contracts (int): Number of contracts in the quote
        yes_bid (int): Bid price for YES contracts, in cents
        no_bid (int): Bid price for NO contracts, in cents
        created_ts (datetime.datetime): Timestamp when the quote was created
        updated_ts (datetime.datetime): Timestamp when the quote was last updated
        status (QuoteStatus): Current status of the quote
        accepted_side (Union[Unset, QuoteAcceptedSide]): The side that was accepted (yes or no)
        accepted_ts (Union[Unset, datetime.datetime]): Timestamp when the quote was accepted
        confirmed_ts (Union[Unset, datetime.datetime]): Timestamp when the quote was confirmed
        executed_ts (Union[Unset, datetime.datetime]): Timestamp when the quote was executed
        cancelled_ts (Union[Unset, datetime.datetime]): Timestamp when the quote was cancelled
        rest_remainder (Union[Unset, bool]): Whether to rest the remainder of the quote after execution
        cancellation_reason (Union[Unset, str]): Reason for quote cancellation if cancelled
        creator_user_id (Union[Unset, str]): User ID of the quote creator (private field)
        rfq_creator_user_id (Union[Unset, str]): User ID of the RFQ creator (private field)
        expired_ts (Union[Unset, datetime.datetime]): Timestamp when the quote expired
        rfq_target_cost_centi_cents (Union[Unset, int]): Total value requested in the RFQ in centi-cents
        rfq_creator_order_id (Union[Unset, str]): Order ID for the RFQ creator (private field)
        creator_order_id (Union[Unset, str]): Order ID for the quote creator (private field)
    """

    id: str
    rfq_id: str
    creator_id: str
    rfq_creator_id: str
    market_ticker: str
    contracts: int
    yes_bid: int
    no_bid: int
    created_ts: datetime.datetime
    updated_ts: datetime.datetime
    status: QuoteStatus
    accepted_side: Union[Unset, QuoteAcceptedSide] = UNSET
    accepted_ts: Union[Unset, datetime.datetime] = UNSET
    confirmed_ts: Union[Unset, datetime.datetime] = UNSET
    executed_ts: Union[Unset, datetime.datetime] = UNSET
    cancelled_ts: Union[Unset, datetime.datetime] = UNSET
    rest_remainder: Union[Unset, bool] = UNSET
    cancellation_reason: Union[Unset, str] = UNSET
    creator_user_id: Union[Unset, str] = UNSET
    rfq_creator_user_id: Union[Unset, str] = UNSET
    expired_ts: Union[Unset, datetime.datetime] = UNSET
    rfq_target_cost_centi_cents: Union[Unset, int] = UNSET
    rfq_creator_order_id: Union[Unset, str] = UNSET
    creator_order_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        rfq_id = self.rfq_id

        creator_id = self.creator_id

        rfq_creator_id = self.rfq_creator_id

        market_ticker = self.market_ticker

        contracts = self.contracts

        yes_bid = self.yes_bid

        no_bid = self.no_bid

        created_ts = self.created_ts.isoformat()

        updated_ts = self.updated_ts.isoformat()

        status = self.status.value

        accepted_side: Union[Unset, str] = UNSET
        if not isinstance(self.accepted_side, Unset):
            accepted_side = self.accepted_side.value

        accepted_ts: Union[Unset, str] = UNSET
        if not isinstance(self.accepted_ts, Unset):
            accepted_ts = self.accepted_ts.isoformat()

        confirmed_ts: Union[Unset, str] = UNSET
        if not isinstance(self.confirmed_ts, Unset):
            confirmed_ts = self.confirmed_ts.isoformat()

        executed_ts: Union[Unset, str] = UNSET
        if not isinstance(self.executed_ts, Unset):
            executed_ts = self.executed_ts.isoformat()

        cancelled_ts: Union[Unset, str] = UNSET
        if not isinstance(self.cancelled_ts, Unset):
            cancelled_ts = self.cancelled_ts.isoformat()

        rest_remainder = self.rest_remainder

        cancellation_reason = self.cancellation_reason

        creator_user_id = self.creator_user_id

        rfq_creator_user_id = self.rfq_creator_user_id

        expired_ts: Union[Unset, str] = UNSET
        if not isinstance(self.expired_ts, Unset):
            expired_ts = self.expired_ts.isoformat()

        rfq_target_cost_centi_cents = self.rfq_target_cost_centi_cents

        rfq_creator_order_id = self.rfq_creator_order_id

        creator_order_id = self.creator_order_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "rfq_id": rfq_id,
                "creator_id": creator_id,
                "rfq_creator_id": rfq_creator_id,
                "market_ticker": market_ticker,
                "contracts": contracts,
                "yes_bid": yes_bid,
                "no_bid": no_bid,
                "created_ts": created_ts,
                "updated_ts": updated_ts,
                "status": status,
            }
        )
        if accepted_side is not UNSET:
            field_dict["accepted_side"] = accepted_side
        if accepted_ts is not UNSET:
            field_dict["accepted_ts"] = accepted_ts
        if confirmed_ts is not UNSET:
            field_dict["confirmed_ts"] = confirmed_ts
        if executed_ts is not UNSET:
            field_dict["executed_ts"] = executed_ts
        if cancelled_ts is not UNSET:
            field_dict["cancelled_ts"] = cancelled_ts
        if rest_remainder is not UNSET:
            field_dict["rest_remainder"] = rest_remainder
        if cancellation_reason is not UNSET:
            field_dict["cancellation_reason"] = cancellation_reason
        if creator_user_id is not UNSET:
            field_dict["creator_user_id"] = creator_user_id
        if rfq_creator_user_id is not UNSET:
            field_dict["rfq_creator_user_id"] = rfq_creator_user_id
        if expired_ts is not UNSET:
            field_dict["expired_ts"] = expired_ts
        if rfq_target_cost_centi_cents is not UNSET:
            field_dict["rfq_target_cost_centi_cents"] = rfq_target_cost_centi_cents
        if rfq_creator_order_id is not UNSET:
            field_dict["rfq_creator_order_id"] = rfq_creator_order_id
        if creator_order_id is not UNSET:
            field_dict["creator_order_id"] = creator_order_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        rfq_id = d.pop("rfq_id")

        creator_id = d.pop("creator_id")

        rfq_creator_id = d.pop("rfq_creator_id")

        market_ticker = d.pop("market_ticker")

        contracts = d.pop("contracts")

        yes_bid = d.pop("yes_bid")

        no_bid = d.pop("no_bid")

        created_ts = isoparse(d.pop("created_ts"))

        updated_ts = isoparse(d.pop("updated_ts"))

        status = QuoteStatus(d.pop("status"))

        _accepted_side = d.pop("accepted_side", UNSET)
        accepted_side: Union[Unset, QuoteAcceptedSide]
        if isinstance(_accepted_side, Unset):
            accepted_side = UNSET
        else:
            accepted_side = QuoteAcceptedSide(_accepted_side)

        _accepted_ts = d.pop("accepted_ts", UNSET)
        accepted_ts: Union[Unset, datetime.datetime]
        if isinstance(_accepted_ts, Unset):
            accepted_ts = UNSET
        else:
            accepted_ts = isoparse(_accepted_ts)

        _confirmed_ts = d.pop("confirmed_ts", UNSET)
        confirmed_ts: Union[Unset, datetime.datetime]
        if isinstance(_confirmed_ts, Unset):
            confirmed_ts = UNSET
        else:
            confirmed_ts = isoparse(_confirmed_ts)

        _executed_ts = d.pop("executed_ts", UNSET)
        executed_ts: Union[Unset, datetime.datetime]
        if isinstance(_executed_ts, Unset):
            executed_ts = UNSET
        else:
            executed_ts = isoparse(_executed_ts)

        _cancelled_ts = d.pop("cancelled_ts", UNSET)
        cancelled_ts: Union[Unset, datetime.datetime]
        if isinstance(_cancelled_ts, Unset):
            cancelled_ts = UNSET
        else:
            cancelled_ts = isoparse(_cancelled_ts)

        rest_remainder = d.pop("rest_remainder", UNSET)

        cancellation_reason = d.pop("cancellation_reason", UNSET)

        creator_user_id = d.pop("creator_user_id", UNSET)

        rfq_creator_user_id = d.pop("rfq_creator_user_id", UNSET)

        _expired_ts = d.pop("expired_ts", UNSET)
        expired_ts: Union[Unset, datetime.datetime]
        if isinstance(_expired_ts, Unset):
            expired_ts = UNSET
        else:
            expired_ts = isoparse(_expired_ts)

        rfq_target_cost_centi_cents = d.pop("rfq_target_cost_centi_cents", UNSET)

        rfq_creator_order_id = d.pop("rfq_creator_order_id", UNSET)

        creator_order_id = d.pop("creator_order_id", UNSET)

        quote = cls(
            id=id,
            rfq_id=rfq_id,
            creator_id=creator_id,
            rfq_creator_id=rfq_creator_id,
            market_ticker=market_ticker,
            contracts=contracts,
            yes_bid=yes_bid,
            no_bid=no_bid,
            created_ts=created_ts,
            updated_ts=updated_ts,
            status=status,
            accepted_side=accepted_side,
            accepted_ts=accepted_ts,
            confirmed_ts=confirmed_ts,
            executed_ts=executed_ts,
            cancelled_ts=cancelled_ts,
            rest_remainder=rest_remainder,
            cancellation_reason=cancellation_reason,
            creator_user_id=creator_user_id,
            rfq_creator_user_id=rfq_creator_user_id,
            expired_ts=expired_ts,
            rfq_target_cost_centi_cents=rfq_target_cost_centi_cents,
            rfq_creator_order_id=rfq_creator_order_id,
            creator_order_id=creator_order_id,
        )

        quote.additional_properties = d
        return quote

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
