from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_public_trades_get_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelPublicTradesGetResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["ticker"] = ticker

    params["min_ts"] = min_ts

    params["max_ts"] = max_ts

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/markets/trades",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelPublicTradesGetResponse]:
    if response.status_code == 200:
        response_200 = GithubComKalshiExchangeInfraSvcApi2ModelPublicTradesGetResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelPublicTradesGetResponse]:
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
    ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelPublicTradesGetResponse]:
    """Get Trades

      Endpoint for getting all trades for all markets.  A trade represents a completed transaction
    between two users on a specific market. Each trade includes the market ticker, price, quantity, and
    timestamp information.  This endpoint returns a paginated response. Use the 'limit' parameter to
    control page size (1-1000, defaults to 100). The response includes a 'cursor' field - pass this
    value in the 'cursor' parameter of your next request to get the next page. An empty cursor indicates
    no more pages are available.

    Args:
        limit (Union[Unset, int]): Number of results per page. Defaults to 100. Maximum value is
            1000.
        cursor (Union[Unset, str]): Pagination cursor. Use the cursor value returned from the
            previous response to get the next page of results. Leave empty for the first page.
        ticker (Union[Unset, str]): Filter trades by market ticker. Returns only trades for the
            specified market.
        min_ts (Union[Unset, int]): Filter trades that occurred after this Unix timestamp.
        max_ts (Union[Unset, int]): Filter trades that occurred before this Unix timestamp.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelPublicTradesGetResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        ticker=ticker,
        min_ts=min_ts,
        max_ts=max_ts,
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
    ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelPublicTradesGetResponse]:
    """Get Trades

      Endpoint for getting all trades for all markets.  A trade represents a completed transaction
    between two users on a specific market. Each trade includes the market ticker, price, quantity, and
    timestamp information.  This endpoint returns a paginated response. Use the 'limit' parameter to
    control page size (1-1000, defaults to 100). The response includes a 'cursor' field - pass this
    value in the 'cursor' parameter of your next request to get the next page. An empty cursor indicates
    no more pages are available.

    Args:
        limit (Union[Unset, int]): Number of results per page. Defaults to 100. Maximum value is
            1000.
        cursor (Union[Unset, str]): Pagination cursor. Use the cursor value returned from the
            previous response to get the next page of results. Leave empty for the first page.
        ticker (Union[Unset, str]): Filter trades by market ticker. Returns only trades for the
            specified market.
        min_ts (Union[Unset, int]): Filter trades that occurred after this Unix timestamp.
        max_ts (Union[Unset, int]): Filter trades that occurred before this Unix timestamp.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelPublicTradesGetResponse
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        ticker=ticker,
        min_ts=min_ts,
        max_ts=max_ts,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelPublicTradesGetResponse]:
    """Get Trades

      Endpoint for getting all trades for all markets.  A trade represents a completed transaction
    between two users on a specific market. Each trade includes the market ticker, price, quantity, and
    timestamp information.  This endpoint returns a paginated response. Use the 'limit' parameter to
    control page size (1-1000, defaults to 100). The response includes a 'cursor' field - pass this
    value in the 'cursor' parameter of your next request to get the next page. An empty cursor indicates
    no more pages are available.

    Args:
        limit (Union[Unset, int]): Number of results per page. Defaults to 100. Maximum value is
            1000.
        cursor (Union[Unset, str]): Pagination cursor. Use the cursor value returned from the
            previous response to get the next page of results. Leave empty for the first page.
        ticker (Union[Unset, str]): Filter trades by market ticker. Returns only trades for the
            specified market.
        min_ts (Union[Unset, int]): Filter trades that occurred after this Unix timestamp.
        max_ts (Union[Unset, int]): Filter trades that occurred before this Unix timestamp.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelPublicTradesGetResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        ticker=ticker,
        min_ts=min_ts,
        max_ts=max_ts,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelPublicTradesGetResponse]:
    """Get Trades

      Endpoint for getting all trades for all markets.  A trade represents a completed transaction
    between two users on a specific market. Each trade includes the market ticker, price, quantity, and
    timestamp information.  This endpoint returns a paginated response. Use the 'limit' parameter to
    control page size (1-1000, defaults to 100). The response includes a 'cursor' field - pass this
    value in the 'cursor' parameter of your next request to get the next page. An empty cursor indicates
    no more pages are available.

    Args:
        limit (Union[Unset, int]): Number of results per page. Defaults to 100. Maximum value is
            1000.
        cursor (Union[Unset, str]): Pagination cursor. Use the cursor value returned from the
            previous response to get the next page of results. Leave empty for the first page.
        ticker (Union[Unset, str]): Filter trades by market ticker. Returns only trades for the
            specified market.
        min_ts (Union[Unset, int]): Filter trades that occurred after this Unix timestamp.
        max_ts (Union[Unset, int]): Filter trades that occurred before this Unix timestamp.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelPublicTradesGetResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            ticker=ticker,
            min_ts=min_ts,
            max_ts=max_ts,
        )
    ).parsed
