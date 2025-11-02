from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_fills_response import GetFillsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ticker: Union[Unset, str] = UNSET,
    order_id: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ticker"] = ticker

    params["order_id"] = order_id

    params["min_ts"] = min_ts

    params["max_ts"] = max_ts

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/portfolio/fills",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetFillsResponse]]:
    if response.status_code == 200:
        response_200 = GetFillsResponse.from_dict(response.json())

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
) -> Response[Union[Any, GetFillsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ticker: Union[Unset, str] = UNSET,
    order_id: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetFillsResponse]]:
    """Get Fills

      Endpoint for getting all fills for the member. A fill is when a trade you have is matched.

    Args:
        ticker (Union[Unset, str]):
        order_id (Union[Unset, str]):
        min_ts (Union[Unset, int]):
        max_ts (Union[Unset, int]):
        limit (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetFillsResponse]]
    """

    kwargs = _get_kwargs(
        ticker=ticker,
        order_id=order_id,
        min_ts=min_ts,
        max_ts=max_ts,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ticker: Union[Unset, str] = UNSET,
    order_id: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetFillsResponse]]:
    """Get Fills

      Endpoint for getting all fills for the member. A fill is when a trade you have is matched.

    Args:
        ticker (Union[Unset, str]):
        order_id (Union[Unset, str]):
        min_ts (Union[Unset, int]):
        max_ts (Union[Unset, int]):
        limit (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetFillsResponse]
    """

    return sync_detailed(
        client=client,
        ticker=ticker,
        order_id=order_id,
        min_ts=min_ts,
        max_ts=max_ts,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ticker: Union[Unset, str] = UNSET,
    order_id: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetFillsResponse]]:
    """Get Fills

      Endpoint for getting all fills for the member. A fill is when a trade you have is matched.

    Args:
        ticker (Union[Unset, str]):
        order_id (Union[Unset, str]):
        min_ts (Union[Unset, int]):
        max_ts (Union[Unset, int]):
        limit (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetFillsResponse]]
    """

    kwargs = _get_kwargs(
        ticker=ticker,
        order_id=order_id,
        min_ts=min_ts,
        max_ts=max_ts,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ticker: Union[Unset, str] = UNSET,
    order_id: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetFillsResponse]]:
    """Get Fills

      Endpoint for getting all fills for the member. A fill is when a trade you have is matched.

    Args:
        ticker (Union[Unset, str]):
        order_id (Union[Unset, str]):
        min_ts (Union[Unset, int]):
        max_ts (Union[Unset, int]):
        limit (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetFillsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            ticker=ticker,
            order_id=order_id,
            min_ts=min_ts,
            max_ts=max_ts,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
