from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_settlements_response import GetSettlementsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["ticker"] = ticker

    params["event_ticker"] = event_ticker

    params["min_ts"] = min_ts

    params["max_ts"] = max_ts

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/portfolio/settlements",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetSettlementsResponse]]:
    if response.status_code == 200:
        response_200 = GetSettlementsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetSettlementsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, GetSettlementsResponse]]:
    """Get Settlements

      Endpoint for getting the member's settlements historical track.

    Args:
        limit (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):
        ticker (Union[Unset, str]):
        event_ticker (Union[Unset, str]):
        min_ts (Union[Unset, int]):
        max_ts (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetSettlementsResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        ticker=ticker,
        event_ticker=event_ticker,
        min_ts=min_ts,
        max_ts=max_ts,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, GetSettlementsResponse]]:
    """Get Settlements

      Endpoint for getting the member's settlements historical track.

    Args:
        limit (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):
        ticker (Union[Unset, str]):
        event_ticker (Union[Unset, str]):
        min_ts (Union[Unset, int]):
        max_ts (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetSettlementsResponse]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        ticker=ticker,
        event_ticker=event_ticker,
        min_ts=min_ts,
        max_ts=max_ts,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, GetSettlementsResponse]]:
    """Get Settlements

      Endpoint for getting the member's settlements historical track.

    Args:
        limit (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):
        ticker (Union[Unset, str]):
        event_ticker (Union[Unset, str]):
        min_ts (Union[Unset, int]):
        max_ts (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetSettlementsResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        ticker=ticker,
        event_ticker=event_ticker,
        min_ts=min_ts,
        max_ts=max_ts,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, GetSettlementsResponse]]:
    """Get Settlements

      Endpoint for getting the member's settlements historical track.

    Args:
        limit (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):
        ticker (Union[Unset, str]):
        event_ticker (Union[Unset, str]):
        min_ts (Union[Unset, int]):
        max_ts (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetSettlementsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            ticker=ticker,
            event_ticker=event_ticker,
            min_ts=min_ts,
            max_ts=max_ts,
        )
    ).parsed
