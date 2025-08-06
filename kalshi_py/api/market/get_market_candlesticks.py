from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_get_market_candlesticks_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelGetMarketCandlesticksResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    series_ticker: str,
    ticker: str,
    *,
    start_ts: int,
    end_ts: int,
    period_interval: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["start_ts"] = start_ts

    params["end_ts"] = end_ts

    params["period_interval"] = period_interval

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/series/{series_ticker}/markets/{ticker}/candlesticks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketCandlesticksResponse]:
    if response.status_code == 200:
        response_200 = GithubComKalshiExchangeInfraSvcApi2ModelGetMarketCandlesticksResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketCandlesticksResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    series_ticker: str,
    ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start_ts: int,
    end_ts: int,
    period_interval: int,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketCandlesticksResponse]:
    """Get Market Candlesticks

      Endpoint for getting historical candlestick data for a specific market.  Candlesticks provide OHLC
    (Open, High, Low, Close) price data aggregated over specific time intervals. Each candlestick
    represents the price movement during that period, including opening and closing prices, as well as
    the highest and lowest prices reached.  The period_interval determines the time length of each
    candlestick and must be one of: 1 (1 minute), 60 (1 hour), or 1440 (1 day). The start_ts and end_ts
    parameters define the time range for the data.

    Args:
        series_ticker (str): Series ticker - the series that contains the target market
        ticker (str): Market ticker - unique identifier for the specific market
        start_ts (int): Start timestamp (Unix timestamp). Candlesticks will include those ending
            on or after this time.
        end_ts (int): End timestamp (Unix timestamp). Candlesticks will include those ending on or
            before this time.
        period_interval (int): Time period length of each candlestick in minutes. Valid values: 1
            (1 minute), 60 (1 hour), 1440 (1 day).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketCandlesticksResponse]
    """

    kwargs = _get_kwargs(
        series_ticker=series_ticker,
        ticker=ticker,
        start_ts=start_ts,
        end_ts=end_ts,
        period_interval=period_interval,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    series_ticker: str,
    ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start_ts: int,
    end_ts: int,
    period_interval: int,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketCandlesticksResponse]:
    """Get Market Candlesticks

      Endpoint for getting historical candlestick data for a specific market.  Candlesticks provide OHLC
    (Open, High, Low, Close) price data aggregated over specific time intervals. Each candlestick
    represents the price movement during that period, including opening and closing prices, as well as
    the highest and lowest prices reached.  The period_interval determines the time length of each
    candlestick and must be one of: 1 (1 minute), 60 (1 hour), or 1440 (1 day). The start_ts and end_ts
    parameters define the time range for the data.

    Args:
        series_ticker (str): Series ticker - the series that contains the target market
        ticker (str): Market ticker - unique identifier for the specific market
        start_ts (int): Start timestamp (Unix timestamp). Candlesticks will include those ending
            on or after this time.
        end_ts (int): End timestamp (Unix timestamp). Candlesticks will include those ending on or
            before this time.
        period_interval (int): Time period length of each candlestick in minutes. Valid values: 1
            (1 minute), 60 (1 hour), 1440 (1 day).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetMarketCandlesticksResponse
    """

    return sync_detailed(
        series_ticker=series_ticker,
        ticker=ticker,
        client=client,
        start_ts=start_ts,
        end_ts=end_ts,
        period_interval=period_interval,
    ).parsed


async def asyncio_detailed(
    series_ticker: str,
    ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start_ts: int,
    end_ts: int,
    period_interval: int,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketCandlesticksResponse]:
    """Get Market Candlesticks

      Endpoint for getting historical candlestick data for a specific market.  Candlesticks provide OHLC
    (Open, High, Low, Close) price data aggregated over specific time intervals. Each candlestick
    represents the price movement during that period, including opening and closing prices, as well as
    the highest and lowest prices reached.  The period_interval determines the time length of each
    candlestick and must be one of: 1 (1 minute), 60 (1 hour), or 1440 (1 day). The start_ts and end_ts
    parameters define the time range for the data.

    Args:
        series_ticker (str): Series ticker - the series that contains the target market
        ticker (str): Market ticker - unique identifier for the specific market
        start_ts (int): Start timestamp (Unix timestamp). Candlesticks will include those ending
            on or after this time.
        end_ts (int): End timestamp (Unix timestamp). Candlesticks will include those ending on or
            before this time.
        period_interval (int): Time period length of each candlestick in minutes. Valid values: 1
            (1 minute), 60 (1 hour), 1440 (1 day).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketCandlesticksResponse]
    """

    kwargs = _get_kwargs(
        series_ticker=series_ticker,
        ticker=ticker,
        start_ts=start_ts,
        end_ts=end_ts,
        period_interval=period_interval,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    series_ticker: str,
    ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start_ts: int,
    end_ts: int,
    period_interval: int,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketCandlesticksResponse]:
    """Get Market Candlesticks

      Endpoint for getting historical candlestick data for a specific market.  Candlesticks provide OHLC
    (Open, High, Low, Close) price data aggregated over specific time intervals. Each candlestick
    represents the price movement during that period, including opening and closing prices, as well as
    the highest and lowest prices reached.  The period_interval determines the time length of each
    candlestick and must be one of: 1 (1 minute), 60 (1 hour), or 1440 (1 day). The start_ts and end_ts
    parameters define the time range for the data.

    Args:
        series_ticker (str): Series ticker - the series that contains the target market
        ticker (str): Market ticker - unique identifier for the specific market
        start_ts (int): Start timestamp (Unix timestamp). Candlesticks will include those ending
            on or after this time.
        end_ts (int): End timestamp (Unix timestamp). Candlesticks will include those ending on or
            before this time.
        period_interval (int): Time period length of each candlestick in minutes. Valid values: 1
            (1 minute), 60 (1 hour), 1440 (1 day).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetMarketCandlesticksResponse
    """

    return (
        await asyncio_detailed(
            series_ticker=series_ticker,
            ticker=ticker,
            client=client,
            start_ts=start_ts,
            end_ts=end_ts,
            period_interval=period_interval,
        )
    ).parsed
