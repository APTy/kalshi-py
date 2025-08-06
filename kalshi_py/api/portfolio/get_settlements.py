from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_get_settlements_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = UNSET,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["ticker"] = ticker

    params["event_ticker"] = event_ticker

    params["min_ts"] = min_ts

    params["max_ts"] = max_ts

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/portfolio/settlements",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponse]:
    if response.status_code == 200:
        response_200 = GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponse]:
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
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponse]:
    """Get Settlements

      Endpoint for getting the member's settlements historical track.

    Args:
        limit (Union[Unset, int]): Parameter to specify the number of results per page. Defaults
            to 100.
        ticker (Union[Unset, str]): Restricts the response to settlements in a specific market.
        event_ticker (Union[Unset, str]): Restricts the response to settlements in a single event.
        min_ts (Union[Unset, int]): Restricts the response to settlements after a timestamp.
        max_ts (Union[Unset, int]): Restricts the response to settlements before a timestamp.
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in
            the pagination. Use the value returned from the previous response to get the next page.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        ticker=ticker,
        event_ticker=event_ticker,
        min_ts=min_ts,
        max_ts=max_ts,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponse]:
    """Get Settlements

      Endpoint for getting the member's settlements historical track.

    Args:
        limit (Union[Unset, int]): Parameter to specify the number of results per page. Defaults
            to 100.
        ticker (Union[Unset, str]): Restricts the response to settlements in a specific market.
        event_ticker (Union[Unset, str]): Restricts the response to settlements in a single event.
        min_ts (Union[Unset, int]): Restricts the response to settlements after a timestamp.
        max_ts (Union[Unset, int]): Restricts the response to settlements before a timestamp.
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in
            the pagination. Use the value returned from the previous response to get the next page.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponse
    """

    return sync_detailed(
        client=client,
        limit=limit,
        ticker=ticker,
        event_ticker=event_ticker,
        min_ts=min_ts,
        max_ts=max_ts,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponse]:
    """Get Settlements

      Endpoint for getting the member's settlements historical track.

    Args:
        limit (Union[Unset, int]): Parameter to specify the number of results per page. Defaults
            to 100.
        ticker (Union[Unset, str]): Restricts the response to settlements in a specific market.
        event_ticker (Union[Unset, str]): Restricts the response to settlements in a single event.
        min_ts (Union[Unset, int]): Restricts the response to settlements after a timestamp.
        max_ts (Union[Unset, int]): Restricts the response to settlements before a timestamp.
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in
            the pagination. Use the value returned from the previous response to get the next page.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        ticker=ticker,
        event_ticker=event_ticker,
        min_ts=min_ts,
        max_ts=max_ts,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponse]:
    """Get Settlements

      Endpoint for getting the member's settlements historical track.

    Args:
        limit (Union[Unset, int]): Parameter to specify the number of results per page. Defaults
            to 100.
        ticker (Union[Unset, str]): Restricts the response to settlements in a specific market.
        event_ticker (Union[Unset, str]): Restricts the response to settlements in a single event.
        min_ts (Union[Unset, int]): Restricts the response to settlements after a timestamp.
        max_ts (Union[Unset, int]): Restricts the response to settlements before a timestamp.
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in
            the pagination. Use the value returned from the previous response to get the next page.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetSettlementsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            ticker=ticker,
            event_ticker=event_ticker,
            min_ts=min_ts,
            max_ts=max_ts,
            cursor=cursor,
        )
    ).parsed
