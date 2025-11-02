from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_markets_response import GetMarketsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
    max_close_ts: Union[Unset, int] = UNSET,
    min_close_ts: Union[Unset, int] = UNSET,
    status: Union[Unset, str] = UNSET,
    tickers: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["event_ticker"] = event_ticker

    params["series_ticker"] = series_ticker

    params["max_close_ts"] = max_close_ts

    params["min_close_ts"] = min_close_ts

    params["status"] = status

    params["tickers"] = tickers

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/markets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetMarketsResponse]]:
    if response.status_code == 200:
        response_200 = GetMarketsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetMarketsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
    max_close_ts: Union[Unset, int] = UNSET,
    min_close_ts: Union[Unset, int] = UNSET,
    status: Union[Unset, str] = UNSET,
    tickers: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetMarketsResponse]]:
    """Get Markets

     Filter by market status. Comma-separated list. Possible values: 'unopened', 'open', 'closed',
    'settled'. Leave empty to return markets with any status.

    Args:
        limit (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):
        event_ticker (Union[Unset, str]):
        series_ticker (Union[Unset, str]):
        max_close_ts (Union[Unset, int]):
        min_close_ts (Union[Unset, int]):
        status (Union[Unset, str]):
        tickers (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetMarketsResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        event_ticker=event_ticker,
        series_ticker=series_ticker,
        max_close_ts=max_close_ts,
        min_close_ts=min_close_ts,
        status=status,
        tickers=tickers,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
    max_close_ts: Union[Unset, int] = UNSET,
    min_close_ts: Union[Unset, int] = UNSET,
    status: Union[Unset, str] = UNSET,
    tickers: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetMarketsResponse]]:
    """Get Markets

     Filter by market status. Comma-separated list. Possible values: 'unopened', 'open', 'closed',
    'settled'. Leave empty to return markets with any status.

    Args:
        limit (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):
        event_ticker (Union[Unset, str]):
        series_ticker (Union[Unset, str]):
        max_close_ts (Union[Unset, int]):
        min_close_ts (Union[Unset, int]):
        status (Union[Unset, str]):
        tickers (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetMarketsResponse]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        event_ticker=event_ticker,
        series_ticker=series_ticker,
        max_close_ts=max_close_ts,
        min_close_ts=min_close_ts,
        status=status,
        tickers=tickers,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
    max_close_ts: Union[Unset, int] = UNSET,
    min_close_ts: Union[Unset, int] = UNSET,
    status: Union[Unset, str] = UNSET,
    tickers: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetMarketsResponse]]:
    """Get Markets

     Filter by market status. Comma-separated list. Possible values: 'unopened', 'open', 'closed',
    'settled'. Leave empty to return markets with any status.

    Args:
        limit (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):
        event_ticker (Union[Unset, str]):
        series_ticker (Union[Unset, str]):
        max_close_ts (Union[Unset, int]):
        min_close_ts (Union[Unset, int]):
        status (Union[Unset, str]):
        tickers (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetMarketsResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        event_ticker=event_ticker,
        series_ticker=series_ticker,
        max_close_ts=max_close_ts,
        min_close_ts=min_close_ts,
        status=status,
        tickers=tickers,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
    max_close_ts: Union[Unset, int] = UNSET,
    min_close_ts: Union[Unset, int] = UNSET,
    status: Union[Unset, str] = UNSET,
    tickers: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetMarketsResponse]]:
    """Get Markets

     Filter by market status. Comma-separated list. Possible values: 'unopened', 'open', 'closed',
    'settled'. Leave empty to return markets with any status.

    Args:
        limit (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):
        event_ticker (Union[Unset, str]):
        series_ticker (Union[Unset, str]):
        max_close_ts (Union[Unset, int]):
        min_close_ts (Union[Unset, int]):
        status (Union[Unset, str]):
        tickers (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetMarketsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            event_ticker=event_ticker,
            series_ticker=series_ticker,
            max_close_ts=max_close_ts,
            min_close_ts=min_close_ts,
            status=status,
            tickers=tickers,
        )
    ).parsed
