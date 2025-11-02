from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_fcm_orders_status import GetFCMOrdersStatus
from ...models.get_orders_response import GetOrdersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    status: Union[Unset, GetFCMOrdersStatus] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    subtrader_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ticker"] = ticker

    params["event_ticker"] = event_ticker

    params["min_ts"] = min_ts

    params["max_ts"] = max_ts

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["limit"] = limit

    params["cursor"] = cursor

    params["subtrader_id"] = subtrader_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fcm/orders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetOrdersResponse]]:
    if response.status_code == 200:
        response_200 = GetOrdersResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetOrdersResponse]]:
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
    event_ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    status: Union[Unset, GetFCMOrdersStatus] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    subtrader_id: str,
) -> Response[Union[Any, GetOrdersResponse]]:
    """Get FCM Orders

     Endpoint for FCM members to get orders filtered by subtrader ID.
    This endpoint requires FCM member access level and allows filtering orders by subtrader ID.

    Args:
        ticker (Union[Unset, str]):
        event_ticker (Union[Unset, str]):
        min_ts (Union[Unset, int]):
        max_ts (Union[Unset, int]):
        status (Union[Unset, GetFCMOrdersStatus]):
        limit (Union[Unset, int]):
        cursor (Union[Unset, str]):
        subtrader_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetOrdersResponse]]
    """

    kwargs = _get_kwargs(
        ticker=ticker,
        event_ticker=event_ticker,
        min_ts=min_ts,
        max_ts=max_ts,
        status=status,
        limit=limit,
        cursor=cursor,
        subtrader_id=subtrader_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    status: Union[Unset, GetFCMOrdersStatus] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    subtrader_id: str,
) -> Optional[Union[Any, GetOrdersResponse]]:
    """Get FCM Orders

     Endpoint for FCM members to get orders filtered by subtrader ID.
    This endpoint requires FCM member access level and allows filtering orders by subtrader ID.

    Args:
        ticker (Union[Unset, str]):
        event_ticker (Union[Unset, str]):
        min_ts (Union[Unset, int]):
        max_ts (Union[Unset, int]):
        status (Union[Unset, GetFCMOrdersStatus]):
        limit (Union[Unset, int]):
        cursor (Union[Unset, str]):
        subtrader_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetOrdersResponse]
    """

    return sync_detailed(
        client=client,
        ticker=ticker,
        event_ticker=event_ticker,
        min_ts=min_ts,
        max_ts=max_ts,
        status=status,
        limit=limit,
        cursor=cursor,
        subtrader_id=subtrader_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    status: Union[Unset, GetFCMOrdersStatus] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    subtrader_id: str,
) -> Response[Union[Any, GetOrdersResponse]]:
    """Get FCM Orders

     Endpoint for FCM members to get orders filtered by subtrader ID.
    This endpoint requires FCM member access level and allows filtering orders by subtrader ID.

    Args:
        ticker (Union[Unset, str]):
        event_ticker (Union[Unset, str]):
        min_ts (Union[Unset, int]):
        max_ts (Union[Unset, int]):
        status (Union[Unset, GetFCMOrdersStatus]):
        limit (Union[Unset, int]):
        cursor (Union[Unset, str]):
        subtrader_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetOrdersResponse]]
    """

    kwargs = _get_kwargs(
        ticker=ticker,
        event_ticker=event_ticker,
        min_ts=min_ts,
        max_ts=max_ts,
        status=status,
        limit=limit,
        cursor=cursor,
        subtrader_id=subtrader_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    status: Union[Unset, GetFCMOrdersStatus] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    subtrader_id: str,
) -> Optional[Union[Any, GetOrdersResponse]]:
    """Get FCM Orders

     Endpoint for FCM members to get orders filtered by subtrader ID.
    This endpoint requires FCM member access level and allows filtering orders by subtrader ID.

    Args:
        ticker (Union[Unset, str]):
        event_ticker (Union[Unset, str]):
        min_ts (Union[Unset, int]):
        max_ts (Union[Unset, int]):
        status (Union[Unset, GetFCMOrdersStatus]):
        limit (Union[Unset, int]):
        cursor (Union[Unset, str]):
        subtrader_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetOrdersResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            ticker=ticker,
            event_ticker=event_ticker,
            min_ts=min_ts,
            max_ts=max_ts,
            status=status,
            limit=limit,
            cursor=cursor,
            subtrader_id=subtrader_id,
        )
    ).parsed
