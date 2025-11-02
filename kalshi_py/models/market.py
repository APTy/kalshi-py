import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.market_market_type import MarketMarketType
from ..models.market_response_price_units import MarketResponsePriceUnits
from ..models.market_result import MarketResult
from ..models.market_status import MarketStatus
from ..models.market_strike_type import MarketStrikeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.market_custom_strike_type_0 import MarketCustomStrikeType0
    from ..models.mve_selected_leg import MveSelectedLeg
    from ..models.price_range import PriceRange


T = TypeVar("T", bound="Market")


@_attrs_define
class Market:
    """
    Attributes:
        ticker (str):
        event_ticker (str):
        market_type (MarketMarketType): Identifies the type of market
        title (str):
        subtitle (str):
        yes_sub_title (str): Shortened title for the yes side of this market
        no_sub_title (str): Shortened title for the no side of this market
        open_time (datetime.datetime):
        close_time (datetime.datetime):
        expiration_time (datetime.datetime):
        latest_expiration_time (datetime.datetime): Latest possible time for this market to expire
        settlement_timer_seconds (int): The amount of time after determination that the market settles
        status (MarketStatus):
        response_price_units (MarketResponsePriceUnits): The units used to express all price related fields
        yes_bid (float):
        yes_bid_dollars (str): Price for the highest YES buy offer on this market in dollars
        yes_ask (float):
        yes_ask_dollars (str): Price for the lowest YES sell offer on this market in dollars
        no_bid (float):
        no_bid_dollars (str): Price for the highest NO buy offer on this market in dollars
        no_ask (float):
        no_ask_dollars (str): Price for the lowest NO sell offer on this market in dollars
        last_price (float):
        last_price_dollars (str): Price for the last traded YES contract on this market in dollars
        volume (int):
        volume_24h (int):
        result (MarketResult):
        can_close_early (bool):
        open_interest (int): Number of contracts bought on this market disconsidering netting
        notional_value (int): The total value of a single contract at settlement in cents
        notional_value_dollars (str): The total value of a single contract at settlement in dollars
        previous_yes_bid (int): Price for the highest YES buy offer on this market a day ago in cents
        previous_yes_bid_dollars (str): Price for the highest YES buy offer on this market a day ago in dollars
        previous_yes_ask (int): Price for the lowest YES sell offer on this market a day ago in cents
        previous_yes_ask_dollars (str): Price for the lowest YES sell offer on this market a day ago in dollars
        previous_price (int): Price for the last traded YES contract on this market a day ago in cents
        previous_price_dollars (str): Price for the last traded YES contract on this market a day ago in dollars
        liquidity (int): Value for current offers in this market in cents
        liquidity_dollars (str): Value for current offers in this market in dollars
        expiration_value (str): The value that was considered for the settlement
        category (str):
        risk_limit_cents (int):
        tick_size (int): The minimum price movement in the market
        rules_primary (str): A plain language description of the most important market terms
        rules_secondary (str): A plain language description of secondary market terms
        price_level_structure (str): Price level structure for this market, defining price ranges and tick sizes
        price_ranges (list['PriceRange']): Valid price ranges for orders on this market
        expected_expiration_time (Union[None, Unset, datetime.datetime]): Time when this market is expected to expire
        settlement_value (Union[None, Unset, int]): The settlement value of the YES/LONG side of the contract in cents.
            Only filled after determination
        settlement_value_dollars (Union[None, Unset, str]): The settlement value of the YES/LONG side of the contract in
            dollars. Only filled after determination
        fee_waiver_expiration_time (Union[None, Unset, datetime.datetime]): Time when this market's fee waiver expires
        early_close_condition (Union[None, Unset, str]): The condition under which the market can close early
        strike_type (Union[Unset, MarketStrikeType]): Strike type defines how the market strike is defined and evaluated
        floor_strike (Union[None, Unset, float]): Minimum expiration value that leads to a YES settlement
        cap_strike (Union[None, Unset, float]): Maximum expiration value that leads to a YES settlement
        functional_strike (Union[None, Unset, str]): Mapping from expiration values to settlement values
        custom_strike (Union['MarketCustomStrikeType0', None, Unset]): Expiration value for each target that leads to a
            YES settlement
        mve_collection_ticker (Union[None, Unset, str]): The ticker of the multivariate event collection
        mve_selected_legs (Union[None, Unset, list['MveSelectedLeg']]):
        primary_participant_key (Union[None, Unset, str]):
    """

    ticker: str
    event_ticker: str
    market_type: MarketMarketType
    title: str
    subtitle: str
    yes_sub_title: str
    no_sub_title: str
    open_time: datetime.datetime
    close_time: datetime.datetime
    expiration_time: datetime.datetime
    latest_expiration_time: datetime.datetime
    settlement_timer_seconds: int
    status: MarketStatus
    response_price_units: MarketResponsePriceUnits
    yes_bid: float
    yes_bid_dollars: str
    yes_ask: float
    yes_ask_dollars: str
    no_bid: float
    no_bid_dollars: str
    no_ask: float
    no_ask_dollars: str
    last_price: float
    last_price_dollars: str
    volume: int
    volume_24h: int
    result: MarketResult
    can_close_early: bool
    open_interest: int
    notional_value: int
    notional_value_dollars: str
    previous_yes_bid: int
    previous_yes_bid_dollars: str
    previous_yes_ask: int
    previous_yes_ask_dollars: str
    previous_price: int
    previous_price_dollars: str
    liquidity: int
    liquidity_dollars: str
    expiration_value: str
    category: str
    risk_limit_cents: int
    tick_size: int
    rules_primary: str
    rules_secondary: str
    price_level_structure: str
    price_ranges: list["PriceRange"]
    expected_expiration_time: Union[None, Unset, datetime.datetime] = UNSET
    settlement_value: Union[None, Unset, int] = UNSET
    settlement_value_dollars: Union[None, Unset, str] = UNSET
    fee_waiver_expiration_time: Union[None, Unset, datetime.datetime] = UNSET
    early_close_condition: Union[None, Unset, str] = UNSET
    strike_type: Union[Unset, MarketStrikeType] = UNSET
    floor_strike: Union[None, Unset, float] = UNSET
    cap_strike: Union[None, Unset, float] = UNSET
    functional_strike: Union[None, Unset, str] = UNSET
    custom_strike: Union["MarketCustomStrikeType0", None, Unset] = UNSET
    mve_collection_ticker: Union[None, Unset, str] = UNSET
    mve_selected_legs: Union[None, Unset, list["MveSelectedLeg"]] = UNSET
    primary_participant_key: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.market_custom_strike_type_0 import MarketCustomStrikeType0

        ticker = self.ticker

        event_ticker = self.event_ticker

        market_type = self.market_type.value

        title = self.title

        subtitle = self.subtitle

        yes_sub_title = self.yes_sub_title

        no_sub_title = self.no_sub_title

        open_time = self.open_time.isoformat()

        close_time = self.close_time.isoformat()

        expiration_time = self.expiration_time.isoformat()

        latest_expiration_time = self.latest_expiration_time.isoformat()

        settlement_timer_seconds = self.settlement_timer_seconds

        status = self.status.value

        response_price_units = self.response_price_units.value

        yes_bid = self.yes_bid

        yes_bid_dollars = self.yes_bid_dollars

        yes_ask = self.yes_ask

        yes_ask_dollars = self.yes_ask_dollars

        no_bid = self.no_bid

        no_bid_dollars = self.no_bid_dollars

        no_ask = self.no_ask

        no_ask_dollars = self.no_ask_dollars

        last_price = self.last_price

        last_price_dollars = self.last_price_dollars

        volume = self.volume

        volume_24h = self.volume_24h

        result = self.result.value

        can_close_early = self.can_close_early

        open_interest = self.open_interest

        notional_value = self.notional_value

        notional_value_dollars = self.notional_value_dollars

        previous_yes_bid = self.previous_yes_bid

        previous_yes_bid_dollars = self.previous_yes_bid_dollars

        previous_yes_ask = self.previous_yes_ask

        previous_yes_ask_dollars = self.previous_yes_ask_dollars

        previous_price = self.previous_price

        previous_price_dollars = self.previous_price_dollars

        liquidity = self.liquidity

        liquidity_dollars = self.liquidity_dollars

        expiration_value = self.expiration_value

        category = self.category

        risk_limit_cents = self.risk_limit_cents

        tick_size = self.tick_size

        rules_primary = self.rules_primary

        rules_secondary = self.rules_secondary

        price_level_structure = self.price_level_structure

        price_ranges = []
        for price_ranges_item_data in self.price_ranges:
            price_ranges_item = price_ranges_item_data.to_dict()
            price_ranges.append(price_ranges_item)

        expected_expiration_time: Union[None, Unset, str]
        if isinstance(self.expected_expiration_time, Unset):
            expected_expiration_time = UNSET
        elif isinstance(self.expected_expiration_time, datetime.datetime):
            expected_expiration_time = self.expected_expiration_time.isoformat()
        else:
            expected_expiration_time = self.expected_expiration_time

        settlement_value: Union[None, Unset, int]
        if isinstance(self.settlement_value, Unset):
            settlement_value = UNSET
        else:
            settlement_value = self.settlement_value

        settlement_value_dollars: Union[None, Unset, str]
        if isinstance(self.settlement_value_dollars, Unset):
            settlement_value_dollars = UNSET
        else:
            settlement_value_dollars = self.settlement_value_dollars

        fee_waiver_expiration_time: Union[None, Unset, str]
        if isinstance(self.fee_waiver_expiration_time, Unset):
            fee_waiver_expiration_time = UNSET
        elif isinstance(self.fee_waiver_expiration_time, datetime.datetime):
            fee_waiver_expiration_time = self.fee_waiver_expiration_time.isoformat()
        else:
            fee_waiver_expiration_time = self.fee_waiver_expiration_time

        early_close_condition: Union[None, Unset, str]
        if isinstance(self.early_close_condition, Unset):
            early_close_condition = UNSET
        else:
            early_close_condition = self.early_close_condition

        strike_type: Union[Unset, str] = UNSET
        if not isinstance(self.strike_type, Unset):
            strike_type = self.strike_type.value

        floor_strike: Union[None, Unset, float]
        if isinstance(self.floor_strike, Unset):
            floor_strike = UNSET
        else:
            floor_strike = self.floor_strike

        cap_strike: Union[None, Unset, float]
        if isinstance(self.cap_strike, Unset):
            cap_strike = UNSET
        else:
            cap_strike = self.cap_strike

        functional_strike: Union[None, Unset, str]
        if isinstance(self.functional_strike, Unset):
            functional_strike = UNSET
        else:
            functional_strike = self.functional_strike

        custom_strike: Union[None, Unset, dict[str, Any]]
        if isinstance(self.custom_strike, Unset):
            custom_strike = UNSET
        elif isinstance(self.custom_strike, MarketCustomStrikeType0):
            custom_strike = self.custom_strike.to_dict()
        else:
            custom_strike = self.custom_strike

        mve_collection_ticker: Union[None, Unset, str]
        if isinstance(self.mve_collection_ticker, Unset):
            mve_collection_ticker = UNSET
        else:
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

        primary_participant_key: Union[None, Unset, str]
        if isinstance(self.primary_participant_key, Unset):
            primary_participant_key = UNSET
        else:
            primary_participant_key = self.primary_participant_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticker": ticker,
                "event_ticker": event_ticker,
                "market_type": market_type,
                "title": title,
                "subtitle": subtitle,
                "yes_sub_title": yes_sub_title,
                "no_sub_title": no_sub_title,
                "open_time": open_time,
                "close_time": close_time,
                "expiration_time": expiration_time,
                "latest_expiration_time": latest_expiration_time,
                "settlement_timer_seconds": settlement_timer_seconds,
                "status": status,
                "response_price_units": response_price_units,
                "yes_bid": yes_bid,
                "yes_bid_dollars": yes_bid_dollars,
                "yes_ask": yes_ask,
                "yes_ask_dollars": yes_ask_dollars,
                "no_bid": no_bid,
                "no_bid_dollars": no_bid_dollars,
                "no_ask": no_ask,
                "no_ask_dollars": no_ask_dollars,
                "last_price": last_price,
                "last_price_dollars": last_price_dollars,
                "volume": volume,
                "volume_24h": volume_24h,
                "result": result,
                "can_close_early": can_close_early,
                "open_interest": open_interest,
                "notional_value": notional_value,
                "notional_value_dollars": notional_value_dollars,
                "previous_yes_bid": previous_yes_bid,
                "previous_yes_bid_dollars": previous_yes_bid_dollars,
                "previous_yes_ask": previous_yes_ask,
                "previous_yes_ask_dollars": previous_yes_ask_dollars,
                "previous_price": previous_price,
                "previous_price_dollars": previous_price_dollars,
                "liquidity": liquidity,
                "liquidity_dollars": liquidity_dollars,
                "expiration_value": expiration_value,
                "category": category,
                "risk_limit_cents": risk_limit_cents,
                "tick_size": tick_size,
                "rules_primary": rules_primary,
                "rules_secondary": rules_secondary,
                "price_level_structure": price_level_structure,
                "price_ranges": price_ranges,
            }
        )
        if expected_expiration_time is not UNSET:
            field_dict["expected_expiration_time"] = expected_expiration_time
        if settlement_value is not UNSET:
            field_dict["settlement_value"] = settlement_value
        if settlement_value_dollars is not UNSET:
            field_dict["settlement_value_dollars"] = settlement_value_dollars
        if fee_waiver_expiration_time is not UNSET:
            field_dict["fee_waiver_expiration_time"] = fee_waiver_expiration_time
        if early_close_condition is not UNSET:
            field_dict["early_close_condition"] = early_close_condition
        if strike_type is not UNSET:
            field_dict["strike_type"] = strike_type
        if floor_strike is not UNSET:
            field_dict["floor_strike"] = floor_strike
        if cap_strike is not UNSET:
            field_dict["cap_strike"] = cap_strike
        if functional_strike is not UNSET:
            field_dict["functional_strike"] = functional_strike
        if custom_strike is not UNSET:
            field_dict["custom_strike"] = custom_strike
        if mve_collection_ticker is not UNSET:
            field_dict["mve_collection_ticker"] = mve_collection_ticker
        if mve_selected_legs is not UNSET:
            field_dict["mve_selected_legs"] = mve_selected_legs
        if primary_participant_key is not UNSET:
            field_dict["primary_participant_key"] = primary_participant_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.market_custom_strike_type_0 import MarketCustomStrikeType0
        from ..models.mve_selected_leg import MveSelectedLeg
        from ..models.price_range import PriceRange

        d = dict(src_dict)
        ticker = d.pop("ticker")

        event_ticker = d.pop("event_ticker")

        market_type = MarketMarketType(d.pop("market_type"))

        title = d.pop("title")

        subtitle = d.pop("subtitle")

        yes_sub_title = d.pop("yes_sub_title")

        no_sub_title = d.pop("no_sub_title")

        open_time = isoparse(d.pop("open_time"))

        close_time = isoparse(d.pop("close_time"))

        expiration_time = isoparse(d.pop("expiration_time"))

        latest_expiration_time = isoparse(d.pop("latest_expiration_time"))

        settlement_timer_seconds = d.pop("settlement_timer_seconds")

        status = MarketStatus(d.pop("status"))

        response_price_units = MarketResponsePriceUnits(d.pop("response_price_units"))

        yes_bid = d.pop("yes_bid")

        yes_bid_dollars = d.pop("yes_bid_dollars")

        yes_ask = d.pop("yes_ask")

        yes_ask_dollars = d.pop("yes_ask_dollars")

        no_bid = d.pop("no_bid")

        no_bid_dollars = d.pop("no_bid_dollars")

        no_ask = d.pop("no_ask")

        no_ask_dollars = d.pop("no_ask_dollars")

        last_price = d.pop("last_price")

        last_price_dollars = d.pop("last_price_dollars")

        volume = d.pop("volume")

        volume_24h = d.pop("volume_24h")

        result = MarketResult(d.pop("result"))

        can_close_early = d.pop("can_close_early")

        open_interest = d.pop("open_interest")

        notional_value = d.pop("notional_value")

        notional_value_dollars = d.pop("notional_value_dollars")

        previous_yes_bid = d.pop("previous_yes_bid")

        previous_yes_bid_dollars = d.pop("previous_yes_bid_dollars")

        previous_yes_ask = d.pop("previous_yes_ask")

        previous_yes_ask_dollars = d.pop("previous_yes_ask_dollars")

        previous_price = d.pop("previous_price")

        previous_price_dollars = d.pop("previous_price_dollars")

        liquidity = d.pop("liquidity")

        liquidity_dollars = d.pop("liquidity_dollars")

        expiration_value = d.pop("expiration_value")

        category = d.pop("category")

        risk_limit_cents = d.pop("risk_limit_cents")

        tick_size = d.pop("tick_size")

        rules_primary = d.pop("rules_primary")

        rules_secondary = d.pop("rules_secondary")

        price_level_structure = d.pop("price_level_structure")

        price_ranges = []
        _price_ranges = d.pop("price_ranges")
        for price_ranges_item_data in _price_ranges:
            price_ranges_item = PriceRange.from_dict(price_ranges_item_data)

            price_ranges.append(price_ranges_item)

        def _parse_expected_expiration_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expected_expiration_time_type_0 = isoparse(data)

                return expected_expiration_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        expected_expiration_time = _parse_expected_expiration_time(d.pop("expected_expiration_time", UNSET))

        def _parse_settlement_value(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        settlement_value = _parse_settlement_value(d.pop("settlement_value", UNSET))

        def _parse_settlement_value_dollars(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        settlement_value_dollars = _parse_settlement_value_dollars(d.pop("settlement_value_dollars", UNSET))

        def _parse_fee_waiver_expiration_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fee_waiver_expiration_time_type_0 = isoparse(data)

                return fee_waiver_expiration_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        fee_waiver_expiration_time = _parse_fee_waiver_expiration_time(d.pop("fee_waiver_expiration_time", UNSET))

        def _parse_early_close_condition(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        early_close_condition = _parse_early_close_condition(d.pop("early_close_condition", UNSET))

        _strike_type = d.pop("strike_type", UNSET)
        strike_type: Union[Unset, MarketStrikeType]
        if isinstance(_strike_type, Unset):
            strike_type = UNSET
        else:
            strike_type = MarketStrikeType(_strike_type)

        def _parse_floor_strike(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        floor_strike = _parse_floor_strike(d.pop("floor_strike", UNSET))

        def _parse_cap_strike(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cap_strike = _parse_cap_strike(d.pop("cap_strike", UNSET))

        def _parse_functional_strike(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        functional_strike = _parse_functional_strike(d.pop("functional_strike", UNSET))

        def _parse_custom_strike(data: object) -> Union["MarketCustomStrikeType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_strike_type_0 = MarketCustomStrikeType0.from_dict(data)

                return custom_strike_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MarketCustomStrikeType0", None, Unset], data)

        custom_strike = _parse_custom_strike(d.pop("custom_strike", UNSET))

        def _parse_mve_collection_ticker(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mve_collection_ticker = _parse_mve_collection_ticker(d.pop("mve_collection_ticker", UNSET))

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

        def _parse_primary_participant_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        primary_participant_key = _parse_primary_participant_key(d.pop("primary_participant_key", UNSET))

        market = cls(
            ticker=ticker,
            event_ticker=event_ticker,
            market_type=market_type,
            title=title,
            subtitle=subtitle,
            yes_sub_title=yes_sub_title,
            no_sub_title=no_sub_title,
            open_time=open_time,
            close_time=close_time,
            expiration_time=expiration_time,
            latest_expiration_time=latest_expiration_time,
            settlement_timer_seconds=settlement_timer_seconds,
            status=status,
            response_price_units=response_price_units,
            yes_bid=yes_bid,
            yes_bid_dollars=yes_bid_dollars,
            yes_ask=yes_ask,
            yes_ask_dollars=yes_ask_dollars,
            no_bid=no_bid,
            no_bid_dollars=no_bid_dollars,
            no_ask=no_ask,
            no_ask_dollars=no_ask_dollars,
            last_price=last_price,
            last_price_dollars=last_price_dollars,
            volume=volume,
            volume_24h=volume_24h,
            result=result,
            can_close_early=can_close_early,
            open_interest=open_interest,
            notional_value=notional_value,
            notional_value_dollars=notional_value_dollars,
            previous_yes_bid=previous_yes_bid,
            previous_yes_bid_dollars=previous_yes_bid_dollars,
            previous_yes_ask=previous_yes_ask,
            previous_yes_ask_dollars=previous_yes_ask_dollars,
            previous_price=previous_price,
            previous_price_dollars=previous_price_dollars,
            liquidity=liquidity,
            liquidity_dollars=liquidity_dollars,
            expiration_value=expiration_value,
            category=category,
            risk_limit_cents=risk_limit_cents,
            tick_size=tick_size,
            rules_primary=rules_primary,
            rules_secondary=rules_secondary,
            price_level_structure=price_level_structure,
            price_ranges=price_ranges,
            expected_expiration_time=expected_expiration_time,
            settlement_value=settlement_value,
            settlement_value_dollars=settlement_value_dollars,
            fee_waiver_expiration_time=fee_waiver_expiration_time,
            early_close_condition=early_close_condition,
            strike_type=strike_type,
            floor_strike=floor_strike,
            cap_strike=cap_strike,
            functional_strike=functional_strike,
            custom_strike=custom_strike,
            mve_collection_ticker=mve_collection_ticker,
            mve_selected_legs=mve_selected_legs,
            primary_participant_key=primary_participant_key,
        )

        market.additional_properties = d
        return market

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
