from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_event_response import GetEventResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event_ticker: str,
    *,
    with_nested_markets: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["with_nested_markets"] = with_nested_markets

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/events/{event_ticker}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetEventResponse]]:
    if response.status_code == 200:
        response_200 = GetEventResponse.from_dict(response.json())

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
) -> Response[Union[Any, GetEventResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
    with_nested_markets: Union[Unset, bool] = False,
) -> Response[Union[Any, GetEventResponse]]:
    """Get Event

      Endpoint for getting data about an event by its ticker.  An event represents a real-world
    occurrence that can be traded on, such as an election, sports game, or economic indicator release.
    Events contain one or more markets where users can place trades on different outcomes.

    Args:
        event_ticker (str):
        with_nested_markets (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetEventResponse]]
    """

    kwargs = _get_kwargs(
        event_ticker=event_ticker,
        with_nested_markets=with_nested_markets,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
    with_nested_markets: Union[Unset, bool] = False,
) -> Optional[Union[Any, GetEventResponse]]:
    """Get Event

      Endpoint for getting data about an event by its ticker.  An event represents a real-world
    occurrence that can be traded on, such as an election, sports game, or economic indicator release.
    Events contain one or more markets where users can place trades on different outcomes.

    Args:
        event_ticker (str):
        with_nested_markets (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetEventResponse]
    """

    return sync_detailed(
        event_ticker=event_ticker,
        client=client,
        with_nested_markets=with_nested_markets,
    ).parsed


async def asyncio_detailed(
    event_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
    with_nested_markets: Union[Unset, bool] = False,
) -> Response[Union[Any, GetEventResponse]]:
    """Get Event

      Endpoint for getting data about an event by its ticker.  An event represents a real-world
    occurrence that can be traded on, such as an election, sports game, or economic indicator release.
    Events contain one or more markets where users can place trades on different outcomes.

    Args:
        event_ticker (str):
        with_nested_markets (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetEventResponse]]
    """

    kwargs = _get_kwargs(
        event_ticker=event_ticker,
        with_nested_markets=with_nested_markets,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
    with_nested_markets: Union[Unset, bool] = False,
) -> Optional[Union[Any, GetEventResponse]]:
    """Get Event

      Endpoint for getting data about an event by its ticker.  An event represents a real-world
    occurrence that can be traded on, such as an election, sports game, or economic indicator release.
    Events contain one or more markets where users can place trades on different outcomes.

    Args:
        event_ticker (str):
        with_nested_markets (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetEventResponse]
    """

    return (
        await asyncio_detailed(
            event_ticker=event_ticker,
            client=client,
            with_nested_markets=with_nested_markets,
        )
    ).parsed
