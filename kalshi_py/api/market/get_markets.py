from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_get_markets_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelGetMarketsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = UNSET,
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
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketsResponse]:
    if response.status_code == 200:
        response_200 = GithubComKalshiExchangeInfraSvcApi2ModelGetMarketsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
    max_close_ts: Union[Unset, int] = UNSET,
    min_close_ts: Union[Unset, int] = UNSET,
    status: Union[Unset, str] = UNSET,
    tickers: Union[Unset, str] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketsResponse]:
    r"""Get Markets

      Endpoint for listing and discovering markets on Kalshi. A market represents a specific binary
    outcome within an event that users can trade on (e.g., \"Will candidate X win?\"). Markets have
    yes/no positions, current prices, volume, and settlement rules. This endpoint returns a paginated
    response. Use the 'limit' parameter to control page size (1-1000, defaults to 100). The response
    includes a 'cursor' field - pass this value in the 'cursor' parameter of your next request to get
    the next page. An empty cursor indicates no more pages are available.

    Args:
        limit (Union[Unset, int]): Number of results per page. Defaults to 100. Maximum value is
            1000.
        cursor (Union[Unset, str]): Pagination cursor. Use the cursor value returned from the
            previous response to get the next page of results. Leave empty for the first page.
        event_ticker (Union[Unset, str]): Filter markets by event ticker. Returns only markets
            belonging to the specified event.
        series_ticker (Union[Unset, str]): Filter markets by series ticker. Returns only markets
            belonging to events in the specified series.
        max_close_ts (Union[Unset, int]): Filter markets that close before this Unix timestamp.
        min_close_ts (Union[Unset, int]): Filter markets that close after this Unix timestamp.
        status (Union[Unset, str]): Filter by market status. Comma-separated list. Possible
            values: 'unopened', 'open', 'closed', 'settled'. Leave empty to return markets with any
            status.
        tickers (Union[Unset, str]): Filter by specific market tickers. Comma-separated list of
            market tickers to retrieve.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketsResponse]
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
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
    max_close_ts: Union[Unset, int] = UNSET,
    min_close_ts: Union[Unset, int] = UNSET,
    status: Union[Unset, str] = UNSET,
    tickers: Union[Unset, str] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketsResponse]:
    r"""Get Markets

      Endpoint for listing and discovering markets on Kalshi. A market represents a specific binary
    outcome within an event that users can trade on (e.g., \"Will candidate X win?\"). Markets have
    yes/no positions, current prices, volume, and settlement rules. This endpoint returns a paginated
    response. Use the 'limit' parameter to control page size (1-1000, defaults to 100). The response
    includes a 'cursor' field - pass this value in the 'cursor' parameter of your next request to get
    the next page. An empty cursor indicates no more pages are available.

    Args:
        limit (Union[Unset, int]): Number of results per page. Defaults to 100. Maximum value is
            1000.
        cursor (Union[Unset, str]): Pagination cursor. Use the cursor value returned from the
            previous response to get the next page of results. Leave empty for the first page.
        event_ticker (Union[Unset, str]): Filter markets by event ticker. Returns only markets
            belonging to the specified event.
        series_ticker (Union[Unset, str]): Filter markets by series ticker. Returns only markets
            belonging to events in the specified series.
        max_close_ts (Union[Unset, int]): Filter markets that close before this Unix timestamp.
        min_close_ts (Union[Unset, int]): Filter markets that close after this Unix timestamp.
        status (Union[Unset, str]): Filter by market status. Comma-separated list. Possible
            values: 'unopened', 'open', 'closed', 'settled'. Leave empty to return markets with any
            status.
        tickers (Union[Unset, str]): Filter by specific market tickers. Comma-separated list of
            market tickers to retrieve.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetMarketsResponse
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
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
    max_close_ts: Union[Unset, int] = UNSET,
    min_close_ts: Union[Unset, int] = UNSET,
    status: Union[Unset, str] = UNSET,
    tickers: Union[Unset, str] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketsResponse]:
    r"""Get Markets

      Endpoint for listing and discovering markets on Kalshi. A market represents a specific binary
    outcome within an event that users can trade on (e.g., \"Will candidate X win?\"). Markets have
    yes/no positions, current prices, volume, and settlement rules. This endpoint returns a paginated
    response. Use the 'limit' parameter to control page size (1-1000, defaults to 100). The response
    includes a 'cursor' field - pass this value in the 'cursor' parameter of your next request to get
    the next page. An empty cursor indicates no more pages are available.

    Args:
        limit (Union[Unset, int]): Number of results per page. Defaults to 100. Maximum value is
            1000.
        cursor (Union[Unset, str]): Pagination cursor. Use the cursor value returned from the
            previous response to get the next page of results. Leave empty for the first page.
        event_ticker (Union[Unset, str]): Filter markets by event ticker. Returns only markets
            belonging to the specified event.
        series_ticker (Union[Unset, str]): Filter markets by series ticker. Returns only markets
            belonging to events in the specified series.
        max_close_ts (Union[Unset, int]): Filter markets that close before this Unix timestamp.
        min_close_ts (Union[Unset, int]): Filter markets that close after this Unix timestamp.
        status (Union[Unset, str]): Filter by market status. Comma-separated list. Possible
            values: 'unopened', 'open', 'closed', 'settled'. Leave empty to return markets with any
            status.
        tickers (Union[Unset, str]): Filter by specific market tickers. Comma-separated list of
            market tickers to retrieve.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketsResponse]
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
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
    max_close_ts: Union[Unset, int] = UNSET,
    min_close_ts: Union[Unset, int] = UNSET,
    status: Union[Unset, str] = UNSET,
    tickers: Union[Unset, str] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketsResponse]:
    r"""Get Markets

      Endpoint for listing and discovering markets on Kalshi. A market represents a specific binary
    outcome within an event that users can trade on (e.g., \"Will candidate X win?\"). Markets have
    yes/no positions, current prices, volume, and settlement rules. This endpoint returns a paginated
    response. Use the 'limit' parameter to control page size (1-1000, defaults to 100). The response
    includes a 'cursor' field - pass this value in the 'cursor' parameter of your next request to get
    the next page. An empty cursor indicates no more pages are available.

    Args:
        limit (Union[Unset, int]): Number of results per page. Defaults to 100. Maximum value is
            1000.
        cursor (Union[Unset, str]): Pagination cursor. Use the cursor value returned from the
            previous response to get the next page of results. Leave empty for the first page.
        event_ticker (Union[Unset, str]): Filter markets by event ticker. Returns only markets
            belonging to the specified event.
        series_ticker (Union[Unset, str]): Filter markets by series ticker. Returns only markets
            belonging to events in the specified series.
        max_close_ts (Union[Unset, int]): Filter markets that close before this Unix timestamp.
        min_close_ts (Union[Unset, int]): Filter markets that close after this Unix timestamp.
        status (Union[Unset, str]): Filter by market status. Comma-separated list. Possible
            values: 'unopened', 'open', 'closed', 'settled'. Leave empty to return markets with any
            status.
        tickers (Union[Unset, str]): Filter by specific market tickers. Comma-separated list of
            market tickers to retrieve.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetMarketsResponse
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
