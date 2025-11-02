from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_events_response import GetEventsResponse
from ...models.get_events_status import GetEventsStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
    with_nested_markets: Union[Unset, bool] = False,
    with_milestones: Union[Unset, bool] = False,
    status: Union[Unset, GetEventsStatus] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
    min_close_ts: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["with_nested_markets"] = with_nested_markets

    params["with_milestones"] = with_milestones

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["series_ticker"] = series_ticker

    params["min_close_ts"] = min_close_ts

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetEventsResponse]]:
    if response.status_code == 200:
        response_200 = GetEventsResponse.from_dict(response.json())

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
) -> Response[Union[Any, GetEventsResponse]]:
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
    with_nested_markets: Union[Unset, bool] = False,
    with_milestones: Union[Unset, bool] = False,
    status: Union[Unset, GetEventsStatus] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
    min_close_ts: Union[Unset, int] = UNSET,
) -> Response[Union[Any, GetEventsResponse]]:
    """Get Events

     Filter by event status. Possible values: 'open', 'closed', 'settled'. Leave empty to return events
    with any status.

    Args:
        limit (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):
        with_nested_markets (Union[Unset, bool]):  Default: False.
        with_milestones (Union[Unset, bool]):  Default: False.
        status (Union[Unset, GetEventsStatus]):
        series_ticker (Union[Unset, str]):
        min_close_ts (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetEventsResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        with_nested_markets=with_nested_markets,
        with_milestones=with_milestones,
        status=status,
        series_ticker=series_ticker,
        min_close_ts=min_close_ts,
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
    with_nested_markets: Union[Unset, bool] = False,
    with_milestones: Union[Unset, bool] = False,
    status: Union[Unset, GetEventsStatus] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
    min_close_ts: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, GetEventsResponse]]:
    """Get Events

     Filter by event status. Possible values: 'open', 'closed', 'settled'. Leave empty to return events
    with any status.

    Args:
        limit (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):
        with_nested_markets (Union[Unset, bool]):  Default: False.
        with_milestones (Union[Unset, bool]):  Default: False.
        status (Union[Unset, GetEventsStatus]):
        series_ticker (Union[Unset, str]):
        min_close_ts (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetEventsResponse]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        with_nested_markets=with_nested_markets,
        with_milestones=with_milestones,
        status=status,
        series_ticker=series_ticker,
        min_close_ts=min_close_ts,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
    with_nested_markets: Union[Unset, bool] = False,
    with_milestones: Union[Unset, bool] = False,
    status: Union[Unset, GetEventsStatus] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
    min_close_ts: Union[Unset, int] = UNSET,
) -> Response[Union[Any, GetEventsResponse]]:
    """Get Events

     Filter by event status. Possible values: 'open', 'closed', 'settled'. Leave empty to return events
    with any status.

    Args:
        limit (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):
        with_nested_markets (Union[Unset, bool]):  Default: False.
        with_milestones (Union[Unset, bool]):  Default: False.
        status (Union[Unset, GetEventsStatus]):
        series_ticker (Union[Unset, str]):
        min_close_ts (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetEventsResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        with_nested_markets=with_nested_markets,
        with_milestones=with_milestones,
        status=status,
        series_ticker=series_ticker,
        min_close_ts=min_close_ts,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
    with_nested_markets: Union[Unset, bool] = False,
    with_milestones: Union[Unset, bool] = False,
    status: Union[Unset, GetEventsStatus] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
    min_close_ts: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, GetEventsResponse]]:
    """Get Events

     Filter by event status. Possible values: 'open', 'closed', 'settled'. Leave empty to return events
    with any status.

    Args:
        limit (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):
        with_nested_markets (Union[Unset, bool]):  Default: False.
        with_milestones (Union[Unset, bool]):  Default: False.
        status (Union[Unset, GetEventsStatus]):
        series_ticker (Union[Unset, str]):
        min_close_ts (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetEventsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            with_nested_markets=with_nested_markets,
            with_milestones=with_milestones,
            status=status,
            series_ticker=series_ticker,
            min_close_ts=min_close_ts,
        )
    ).parsed
