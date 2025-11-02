import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rfq_status import RFQStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mve_selected_leg import MveSelectedLeg


T = TypeVar("T", bound="RFQ")


@_attrs_define
class RFQ:
    """
    Attributes:
        id (str): Unique identifier for the RFQ
        creator_id (str): Public communications ID of the RFQ creator
        market_ticker (str): The ticker of the market this RFQ is for
        status (RFQStatus): Current status of the RFQ (open, closed)
        created_ts (datetime.datetime): Timestamp when the RFQ was created
        contracts (Union[Unset, int]): Number of contracts requested in the RFQ
        target_cost_centi_cents (Union[Unset, int]): Total value of the RFQ in centi-cents
        mve_collection_ticker (Union[Unset, str]): Ticker of the MVE collection this market belongs to
        mve_selected_legs (Union[None, Unset, list['MveSelectedLeg']]): Selected legs for the MVE collection
        rest_remainder (Union[Unset, bool]): Whether to rest the remainder of the RFQ after execution
        cancellation_reason (Union[Unset, str]): Reason for RFQ cancellation if cancelled
        creator_user_id (Union[Unset, str]): User ID of the RFQ creator (private field)
        cancelled_ts (Union[Unset, datetime.datetime]): Timestamp when the RFQ was cancelled
        updated_ts (Union[Unset, datetime.datetime]): Timestamp when the RFQ was last updated
    """

    id: str
    creator_id: str
    market_ticker: str
    status: RFQStatus
    created_ts: datetime.datetime
    contracts: Union[Unset, int] = UNSET
    target_cost_centi_cents: Union[Unset, int] = UNSET
    mve_collection_ticker: Union[Unset, str] = UNSET
    mve_selected_legs: Union[None, Unset, list["MveSelectedLeg"]] = UNSET
    rest_remainder: Union[Unset, bool] = UNSET
    cancellation_reason: Union[Unset, str] = UNSET
    creator_user_id: Union[Unset, str] = UNSET
    cancelled_ts: Union[Unset, datetime.datetime] = UNSET
    updated_ts: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        creator_id = self.creator_id

        market_ticker = self.market_ticker

        status = self.status.value

        created_ts = self.created_ts.isoformat()

        contracts = self.contracts

        target_cost_centi_cents = self.target_cost_centi_cents

        mve_collection_ticker = self.mve_collection_ticker

        mve_selected_legs: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.mve_selected_legs, Unset):
            mve_selected_legs = UNSET
        elif isinstance(self.mve_selected_legs, list):
            mve_selected_legs = []
            for mve_selected_legs_type_0_item_data in self.mve_selected_legs:
                mve_selected_legs_type_0_item = mve_selected_legs_type_0_item_data.to_dict()
                mve_selected_legs.append(mve_selected_legs_type_0_item)

        else:
            mve_selected_legs = self.mve_selected_legs

        rest_remainder = self.rest_remainder

        cancellation_reason = self.cancellation_reason

        creator_user_id = self.creator_user_id

        cancelled_ts: Union[Unset, str] = UNSET
        if not isinstance(self.cancelled_ts, Unset):
            cancelled_ts = self.cancelled_ts.isoformat()

        updated_ts: Union[Unset, str] = UNSET
        if not isinstance(self.updated_ts, Unset):
            updated_ts = self.updated_ts.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "creator_id": creator_id,
                "market_ticker": market_ticker,
                "status": status,
                "created_ts": created_ts,
            }
        )
        if contracts is not UNSET:
            field_dict["contracts"] = contracts
        if target_cost_centi_cents is not UNSET:
            field_dict["target_cost_centi_cents"] = target_cost_centi_cents
        if mve_collection_ticker is not UNSET:
            field_dict["mve_collection_ticker"] = mve_collection_ticker
        if mve_selected_legs is not UNSET:
            field_dict["mve_selected_legs"] = mve_selected_legs
        if rest_remainder is not UNSET:
            field_dict["rest_remainder"] = rest_remainder
        if cancellation_reason is not UNSET:
            field_dict["cancellation_reason"] = cancellation_reason
        if creator_user_id is not UNSET:
            field_dict["creator_user_id"] = creator_user_id
        if cancelled_ts is not UNSET:
            field_dict["cancelled_ts"] = cancelled_ts
        if updated_ts is not UNSET:
            field_dict["updated_ts"] = updated_ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mve_selected_leg import MveSelectedLeg

        d = dict(src_dict)
        id = d.pop("id")

        creator_id = d.pop("creator_id")

        market_ticker = d.pop("market_ticker")

        status = RFQStatus(d.pop("status"))

        created_ts = isoparse(d.pop("created_ts"))

        contracts = d.pop("contracts", UNSET)

        target_cost_centi_cents = d.pop("target_cost_centi_cents", UNSET)

        mve_collection_ticker = d.pop("mve_collection_ticker", UNSET)

        def _parse_mve_selected_legs(data: object) -> Union[None, Unset, list["MveSelectedLeg"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mve_selected_legs_type_0 = []
                _mve_selected_legs_type_0 = data
                for mve_selected_legs_type_0_item_data in _mve_selected_legs_type_0:
                    mve_selected_legs_type_0_item = MveSelectedLeg.from_dict(mve_selected_legs_type_0_item_data)

                    mve_selected_legs_type_0.append(mve_selected_legs_type_0_item)

                return mve_selected_legs_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["MveSelectedLeg"]], data)

        mve_selected_legs = _parse_mve_selected_legs(d.pop("mve_selected_legs", UNSET))

        rest_remainder = d.pop("rest_remainder", UNSET)

        cancellation_reason = d.pop("cancellation_reason", UNSET)

        creator_user_id = d.pop("creator_user_id", UNSET)

        _cancelled_ts = d.pop("cancelled_ts", UNSET)
        cancelled_ts: Union[Unset, datetime.datetime]
        if isinstance(_cancelled_ts, Unset):
            cancelled_ts = UNSET
        else:
            cancelled_ts = isoparse(_cancelled_ts)

        _updated_ts = d.pop("updated_ts", UNSET)
        updated_ts: Union[Unset, datetime.datetime]
        if isinstance(_updated_ts, Unset):
            updated_ts = UNSET
        else:
            updated_ts = isoparse(_updated_ts)

        rfq = cls(
            id=id,
            creator_id=creator_id,
            market_ticker=market_ticker,
            status=status,
            created_ts=created_ts,
            contracts=contracts,
            target_cost_centi_cents=target_cost_centi_cents,
            mve_collection_ticker=mve_collection_ticker,
            mve_selected_legs=mve_selected_legs,
            rest_remainder=rest_remainder,
            cancellation_reason=cancellation_reason,
            creator_user_id=creator_user_id,
            cancelled_ts=cancelled_ts,
            updated_ts=updated_ts,
        )

        rfq.additional_properties = d
        return rfq

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
