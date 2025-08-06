from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_get_event_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelGetEventResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event_ticker: str,
    *,
    with_nested_markets: Union[Unset, bool] = UNSET,
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
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetEventResponse]:
    if response.status_code == 200:
        response_200 = GithubComKalshiExchangeInfraSvcApi2ModelGetEventResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetEventResponse]:
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
    with_nested_markets: Union[Unset, bool] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetEventResponse]:
    """Get Event

      Endpoint for getting data about an event by its ticker.  An event represents a real-world
    occurrence that can be traded on, such as an election, sports game, or economic indicator release.
    Events contain one or more markets where users can place trades on different outcomes.

    Args:
        event_ticker (str): Event ticker
        with_nested_markets (Union[Unset, bool]): If true, markets are included within the event
            object. If false (default), markets are returned as a separate top-level field in the
            response.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetEventResponse]
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
    with_nested_markets: Union[Unset, bool] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetEventResponse]:
    """Get Event

      Endpoint for getting data about an event by its ticker.  An event represents a real-world
    occurrence that can be traded on, such as an election, sports game, or economic indicator release.
    Events contain one or more markets where users can place trades on different outcomes.

    Args:
        event_ticker (str): Event ticker
        with_nested_markets (Union[Unset, bool]): If true, markets are included within the event
            object. If false (default), markets are returned as a separate top-level field in the
            response.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetEventResponse
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
    with_nested_markets: Union[Unset, bool] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetEventResponse]:
    """Get Event

      Endpoint for getting data about an event by its ticker.  An event represents a real-world
    occurrence that can be traded on, such as an election, sports game, or economic indicator release.
    Events contain one or more markets where users can place trades on different outcomes.

    Args:
        event_ticker (str): Event ticker
        with_nested_markets (Union[Unset, bool]): If true, markets are included within the event
            object. If false (default), markets are returned as a separate top-level field in the
            response.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetEventResponse]
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
    with_nested_markets: Union[Unset, bool] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetEventResponse]:
    """Get Event

      Endpoint for getting data about an event by its ticker.  An event represents a real-world
    occurrence that can be traded on, such as an election, sports game, or economic indicator release.
    Events contain one or more markets where users can place trades on different outcomes.

    Args:
        event_ticker (str): Event ticker
        with_nested_markets (Union[Unset, bool]): If true, markets are included within the event
            object. If false (default), markets are returned as a separate top-level field in the
            response.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetEventResponse
    """

    return (
        await asyncio_detailed(
            event_ticker=event_ticker,
            client=client,
            with_nested_markets=with_nested_markets,
        )
    ).parsed
