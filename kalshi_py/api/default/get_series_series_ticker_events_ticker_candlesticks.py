from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_common_api_json_error import (
    GithubComKalshiExchangeInfraCommonApiJSONError,
)
from ...models.model_get_event_candlesticks_response import ModelGetEventCandlesticksResponse
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
        "url": f"/series/{series_ticker}/events/{ticker}/candlesticks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetEventCandlesticksResponse]]:
    if response.status_code == 200:
        response_200 = ModelGetEventCandlesticksResponse.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = GithubComKalshiExchangeInfraCommonApiJSONError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetEventCandlesticksResponse]]:
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
) -> Response[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetEventCandlesticksResponse]]:
    """End-point for returning aggregated data across all markets corresponding to an event.

    Args:
        series_ticker (str): Series Ticker
        ticker (str): Event Ticker
        start_ts (int): Start timestamp for the range
        end_ts (int): End timestamp for the range
        period_interval (int): Specifies the length of each candlestick period, in minutes. Must
            be one minute, one hour, or one day.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetEventCandlesticksResponse]]
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
) -> Optional[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetEventCandlesticksResponse]]:
    """End-point for returning aggregated data across all markets corresponding to an event.

    Args:
        series_ticker (str): Series Ticker
        ticker (str): Event Ticker
        start_ts (int): Start timestamp for the range
        end_ts (int): End timestamp for the range
        period_interval (int): Specifies the length of each candlestick period, in minutes. Must
            be one minute, one hour, or one day.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetEventCandlesticksResponse]
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
) -> Response[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetEventCandlesticksResponse]]:
    """End-point for returning aggregated data across all markets corresponding to an event.

    Args:
        series_ticker (str): Series Ticker
        ticker (str): Event Ticker
        start_ts (int): Start timestamp for the range
        end_ts (int): End timestamp for the range
        period_interval (int): Specifies the length of each candlestick period, in minutes. Must
            be one minute, one hour, or one day.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetEventCandlesticksResponse]]
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
) -> Optional[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetEventCandlesticksResponse]]:
    """End-point for returning aggregated data across all markets corresponding to an event.

    Args:
        series_ticker (str): Series Ticker
        ticker (str): Event Ticker
        start_ts (int): Start timestamp for the range
        end_ts (int): End timestamp for the range
        period_interval (int): Specifies the length of each candlestick period, in minutes. Must
            be one minute, one hour, or one day.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetEventCandlesticksResponse]
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
