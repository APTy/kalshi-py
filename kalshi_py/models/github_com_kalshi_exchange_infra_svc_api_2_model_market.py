import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelMarket")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelMarket:
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
        title (Union[Unset, str]): Full title describing this market
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
    title: Union[Unset, str] = UNSET
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

        title = self.title

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
            }
        )
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        title = d.pop("title", UNSET)

        github_com_kalshi_exchange_infra_svc_api_2_model_market = cls(
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
            title=title,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_market.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_market

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
