import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.model_market_price_level_structure import ModelMarketPriceLevelStructure
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_price_range import ModelPriceRange


T = TypeVar("T", bound="ModelMarket")


@_attrs_define
class ModelMarket:
    """Contains information about a market

    Attributes:
        ticker (str): Unique identifier for markets
        event_ticker (str): Unique identifier for events
        market_type (str): Type of market (binary, scalar)
        subtitle (str): Shortened title for this market
        yes_sub_title (str): Shortened title for the yes side
        no_sub_title (str): Shortened title for the no side
        open_time (datetime.datetime): Time when trading begins
        close_time (datetime.datetime): Time when trading ends
        expiration_time (datetime.datetime): Time when market expires
        latest_expiration_time (datetime.datetime): Latest possible expiration time
        settlement_timer_seconds (int): Settlement timer in seconds
        status (str): Current market status
        response_price_units (str): Price units for response
        notional_value (int): Notional value of contract
        tick_size (int): Minimum price movement
        yes_bid (int): Highest YES buy offer price
        yes_ask (int): Lowest YES sell offer price
        no_bid (int): Highest NO buy offer price
        no_ask (int): Lowest NO sell offer price
        last_price (int): Last traded price
        previous_yes_bid (int): Previous YES bid price
        previous_yes_ask (int): Previous YES ask price
        previous_price (int): Previous traded price
        volume (int): Trading volume
        volume_24h (int): 24h trading volume
        liquidity (int): Current liquidity
        open_interest (int): Open interest
        result (str): Settlement result
        can_close_early (bool): Whether market can close early
        expiration_value (str): Expiration value
        category (str): Market category
        risk_limit_cents (int): Risk limit in cents
        rules_primary (str): Primary market rules
        rules_secondary (str): Secondary market rules
        price_level_structure (ModelMarketPriceLevelStructure): Price level structure name for this market.
        price_ranges (list['ModelPriceRange']): Valid price ranges for orders on this market.
        title (Union[Unset, str]): Full title describing this market
        notional_value_dollars (Union[Unset, str]): Notional value of contract in dollars Example: 0.2300.
        yes_bid_dollars (Union[Unset, str]): Highest YES buy offer price in dollars Example: 0.2300.
        yes_ask_dollars (Union[Unset, str]): Lowest YES sell offer price in dollars Example: 0.2300.
        no_bid_dollars (Union[Unset, str]): Highest NO buy offer price in dollars Example: 0.2300.
        no_ask_dollars (Union[Unset, str]): Lowest NO sell offer price in dollars Example: 0.2300.
        last_price_dollars (Union[Unset, str]): Last traded price in dollars Example: 0.2300.
        previous_yes_bid_dollars (Union[Unset, str]): Previous YES bid price in dollars Example: 0.2300.
        previous_yes_ask_dollars (Union[Unset, str]): Previous YES ask price in dollars Example: 0.2300.
        previous_price_dollars (Union[Unset, str]): Previous traded price in dollars Example: 0.2300.
        liquidity_dollars (Union[Unset, str]): Current liquidity in dollars Example: 0.2300.
        settlement_value (Union[Unset, int]): The settlement value of the YES/LONG side of the contract. Only filled
            after determination.
        settlement_value_dollars (Union[Unset, str]): The settlement value of the YES/LONG side of the contract. Only
            filled after determination. Example: 0.2300.
    """

    ticker: str
    event_ticker: str
    market_type: str
    subtitle: str
    yes_sub_title: str
    no_sub_title: str
    open_time: datetime.datetime
    close_time: datetime.datetime
    expiration_time: datetime.datetime
    latest_expiration_time: datetime.datetime
    settlement_timer_seconds: int
    status: str
    response_price_units: str
    notional_value: int
    tick_size: int
    yes_bid: int
    yes_ask: int
    no_bid: int
    no_ask: int
    last_price: int
    previous_yes_bid: int
    previous_yes_ask: int
    previous_price: int
    volume: int
    volume_24h: int
    liquidity: int
    open_interest: int
    result: str
    can_close_early: bool
    expiration_value: str
    category: str
    risk_limit_cents: int
    rules_primary: str
    rules_secondary: str
    price_level_structure: ModelMarketPriceLevelStructure
    price_ranges: list["ModelPriceRange"]
    title: Union[Unset, str] = UNSET
    notional_value_dollars: Union[Unset, str] = UNSET
    yes_bid_dollars: Union[Unset, str] = UNSET
    yes_ask_dollars: Union[Unset, str] = UNSET
    no_bid_dollars: Union[Unset, str] = UNSET
    no_ask_dollars: Union[Unset, str] = UNSET
    last_price_dollars: Union[Unset, str] = UNSET
    previous_yes_bid_dollars: Union[Unset, str] = UNSET
    previous_yes_ask_dollars: Union[Unset, str] = UNSET
    previous_price_dollars: Union[Unset, str] = UNSET
    liquidity_dollars: Union[Unset, str] = UNSET
    settlement_value: Union[Unset, int] = UNSET
    settlement_value_dollars: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticker = self.ticker

        event_ticker = self.event_ticker

        market_type = self.market_type

        subtitle = self.subtitle

        yes_sub_title = self.yes_sub_title

        no_sub_title = self.no_sub_title

        open_time = self.open_time.isoformat()

        close_time = self.close_time.isoformat()

        expiration_time = self.expiration_time.isoformat()

        latest_expiration_time = self.latest_expiration_time.isoformat()

        settlement_timer_seconds = self.settlement_timer_seconds

        status = self.status

        response_price_units = self.response_price_units

        notional_value = self.notional_value

        tick_size = self.tick_size

        yes_bid = self.yes_bid

        yes_ask = self.yes_ask

        no_bid = self.no_bid

        no_ask = self.no_ask

        last_price = self.last_price

        previous_yes_bid = self.previous_yes_bid

        previous_yes_ask = self.previous_yes_ask

        previous_price = self.previous_price

        volume = self.volume

        volume_24h = self.volume_24h

        liquidity = self.liquidity

        open_interest = self.open_interest

        result = self.result

        can_close_early = self.can_close_early

        expiration_value = self.expiration_value

        category = self.category

        risk_limit_cents = self.risk_limit_cents

        rules_primary = self.rules_primary

        rules_secondary = self.rules_secondary

        price_level_structure = self.price_level_structure.value

        price_ranges = []
        for price_ranges_item_data in self.price_ranges:
            price_ranges_item = price_ranges_item_data.to_dict()
            price_ranges.append(price_ranges_item)

        title = self.title

        notional_value_dollars = self.notional_value_dollars

        yes_bid_dollars = self.yes_bid_dollars

        yes_ask_dollars = self.yes_ask_dollars

        no_bid_dollars = self.no_bid_dollars

        no_ask_dollars = self.no_ask_dollars

        last_price_dollars = self.last_price_dollars

        previous_yes_bid_dollars = self.previous_yes_bid_dollars

        previous_yes_ask_dollars = self.previous_yes_ask_dollars

        previous_price_dollars = self.previous_price_dollars

        liquidity_dollars = self.liquidity_dollars

        settlement_value = self.settlement_value

        settlement_value_dollars = self.settlement_value_dollars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticker": ticker,
                "event_ticker": event_ticker,
                "market_type": market_type,
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
                "notional_value": notional_value,
                "tick_size": tick_size,
                "yes_bid": yes_bid,
                "yes_ask": yes_ask,
                "no_bid": no_bid,
                "no_ask": no_ask,
                "last_price": last_price,
                "previous_yes_bid": previous_yes_bid,
                "previous_yes_ask": previous_yes_ask,
                "previous_price": previous_price,
                "volume": volume,
                "volume_24h": volume_24h,
                "liquidity": liquidity,
                "open_interest": open_interest,
                "result": result,
                "can_close_early": can_close_early,
                "expiration_value": expiration_value,
                "category": category,
                "risk_limit_cents": risk_limit_cents,
                "rules_primary": rules_primary,
                "rules_secondary": rules_secondary,
                "price_level_structure": price_level_structure,
                "price_ranges": price_ranges,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if notional_value_dollars is not UNSET:
            field_dict["notional_value_dollars"] = notional_value_dollars
        if yes_bid_dollars is not UNSET:
            field_dict["yes_bid_dollars"] = yes_bid_dollars
        if yes_ask_dollars is not UNSET:
            field_dict["yes_ask_dollars"] = yes_ask_dollars
        if no_bid_dollars is not UNSET:
            field_dict["no_bid_dollars"] = no_bid_dollars
        if no_ask_dollars is not UNSET:
            field_dict["no_ask_dollars"] = no_ask_dollars
        if last_price_dollars is not UNSET:
            field_dict["last_price_dollars"] = last_price_dollars
        if previous_yes_bid_dollars is not UNSET:
            field_dict["previous_yes_bid_dollars"] = previous_yes_bid_dollars
        if previous_yes_ask_dollars is not UNSET:
            field_dict["previous_yes_ask_dollars"] = previous_yes_ask_dollars
        if previous_price_dollars is not UNSET:
            field_dict["previous_price_dollars"] = previous_price_dollars
        if liquidity_dollars is not UNSET:
            field_dict["liquidity_dollars"] = liquidity_dollars
        if settlement_value is not UNSET:
            field_dict["settlement_value"] = settlement_value
        if settlement_value_dollars is not UNSET:
            field_dict["settlement_value_dollars"] = settlement_value_dollars

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_price_range import ModelPriceRange

        d = dict(src_dict)
        ticker = d.pop("ticker")

        event_ticker = d.pop("event_ticker")

        market_type = d.pop("market_type")

        subtitle = d.pop("subtitle")

        yes_sub_title = d.pop("yes_sub_title")

        no_sub_title = d.pop("no_sub_title")

        open_time = isoparse(d.pop("open_time"))

        close_time = isoparse(d.pop("close_time"))

        expiration_time = isoparse(d.pop("expiration_time"))

        latest_expiration_time = isoparse(d.pop("latest_expiration_time"))

        settlement_timer_seconds = d.pop("settlement_timer_seconds")

        status = d.pop("status")

        response_price_units = d.pop("response_price_units")

        notional_value = d.pop("notional_value")

        tick_size = d.pop("tick_size")

        yes_bid = d.pop("yes_bid")

        yes_ask = d.pop("yes_ask")

        no_bid = d.pop("no_bid")

        no_ask = d.pop("no_ask")

        last_price = d.pop("last_price")

        previous_yes_bid = d.pop("previous_yes_bid")

        previous_yes_ask = d.pop("previous_yes_ask")

        previous_price = d.pop("previous_price")

        volume = d.pop("volume")

        volume_24h = d.pop("volume_24h")

        liquidity = d.pop("liquidity")

        open_interest = d.pop("open_interest")

        result = d.pop("result")

        can_close_early = d.pop("can_close_early")

        expiration_value = d.pop("expiration_value")

        category = d.pop("category")

        risk_limit_cents = d.pop("risk_limit_cents")

        rules_primary = d.pop("rules_primary")

        rules_secondary = d.pop("rules_secondary")

        price_level_structure = ModelMarketPriceLevelStructure(d.pop("price_level_structure"))

        price_ranges = []
        _price_ranges = d.pop("price_ranges")
        for price_ranges_item_data in _price_ranges:
            price_ranges_item = ModelPriceRange.from_dict(price_ranges_item_data)

            price_ranges.append(price_ranges_item)

        title = d.pop("title", UNSET)

        notional_value_dollars = d.pop("notional_value_dollars", UNSET)

        yes_bid_dollars = d.pop("yes_bid_dollars", UNSET)

        yes_ask_dollars = d.pop("yes_ask_dollars", UNSET)

        no_bid_dollars = d.pop("no_bid_dollars", UNSET)

        no_ask_dollars = d.pop("no_ask_dollars", UNSET)

        last_price_dollars = d.pop("last_price_dollars", UNSET)

        previous_yes_bid_dollars = d.pop("previous_yes_bid_dollars", UNSET)

        previous_yes_ask_dollars = d.pop("previous_yes_ask_dollars", UNSET)

        previous_price_dollars = d.pop("previous_price_dollars", UNSET)

        liquidity_dollars = d.pop("liquidity_dollars", UNSET)

        settlement_value = d.pop("settlement_value", UNSET)

        settlement_value_dollars = d.pop("settlement_value_dollars", UNSET)

        model_market = cls(
            ticker=ticker,
            event_ticker=event_ticker,
            market_type=market_type,
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
            notional_value=notional_value,
            tick_size=tick_size,
            yes_bid=yes_bid,
            yes_ask=yes_ask,
            no_bid=no_bid,
            no_ask=no_ask,
            last_price=last_price,
            previous_yes_bid=previous_yes_bid,
            previous_yes_ask=previous_yes_ask,
            previous_price=previous_price,
            volume=volume,
            volume_24h=volume_24h,
            liquidity=liquidity,
            open_interest=open_interest,
            result=result,
            can_close_early=can_close_early,
            expiration_value=expiration_value,
            category=category,
            risk_limit_cents=risk_limit_cents,
            rules_primary=rules_primary,
            rules_secondary=rules_secondary,
            price_level_structure=price_level_structure,
            price_ranges=price_ranges,
            title=title,
            notional_value_dollars=notional_value_dollars,
            yes_bid_dollars=yes_bid_dollars,
            yes_ask_dollars=yes_ask_dollars,
            no_bid_dollars=no_bid_dollars,
            no_ask_dollars=no_ask_dollars,
            last_price_dollars=last_price_dollars,
            previous_yes_bid_dollars=previous_yes_bid_dollars,
            previous_yes_ask_dollars=previous_yes_ask_dollars,
            previous_price_dollars=previous_price_dollars,
            liquidity_dollars=liquidity_dollars,
            settlement_value=settlement_value,
            settlement_value_dollars=settlement_value_dollars,
        )

        model_market.additional_properties = d
        return model_market

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
