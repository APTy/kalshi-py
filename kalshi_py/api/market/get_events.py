from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_get_events_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelGetEventsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    with_nested_markets: Union[Unset, bool] = UNSET,
    status: Union[Unset, str] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["with_nested_markets"] = with_nested_markets

    params["status"] = status

    params["series_ticker"] = series_ticker

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetEventsResponse]:
    if response.status_code == 200:
        response_200 = GithubComKalshiExchangeInfraSvcApi2ModelGetEventsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetEventsResponse]:
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
    with_nested_markets: Union[Unset, bool] = UNSET,
    status: Union[Unset, str] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetEventsResponse]:
    """Get Events

      Endpoint for getting data about all events.  An event represents a real-world occurrence that can
    be traded on, such as an election, sports game, or economic indicator release. Events contain one or
    more markets where users can place trades on different outcomes.  This endpoint returns a paginated
    response. Use the 'limit' parameter to control page size (1-200, defaults to 100). The response
    includes a 'cursor' field - pass this value in the 'cursor' parameter of your next request to get
    the next page. An empty cursor indicates no more pages are available.

    Args:
        limit (Union[Unset, int]): Parameter to specify the number of results per page. Defaults
            to 100. Maximum value is 200.
        cursor (Union[Unset, str]): Parameter to specify the pagination cursor. Use the cursor
            value returned from the previous response to get the next page of results. Leave empty for
            the first page.
        with_nested_markets (Union[Unset, bool]): Parameter to specify if nested markets should be
            included in the response. When true, each event will include a 'markets' field containing
            a list of Market objects associated with that event.
        status (Union[Unset, str]): Filter by event status. Possible values: 'open', 'closed',
            'settled'. Leave empty to return events with any status.
        series_ticker (Union[Unset, str]): Filter events by series ticker. Returns only events
            belonging to the specified series.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetEventsResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        with_nested_markets=with_nested_markets,
        status=status,
        series_ticker=series_ticker,
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
    with_nested_markets: Union[Unset, bool] = UNSET,
    status: Union[Unset, str] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetEventsResponse]:
    """Get Events

      Endpoint for getting data about all events.  An event represents a real-world occurrence that can
    be traded on, such as an election, sports game, or economic indicator release. Events contain one or
    more markets where users can place trades on different outcomes.  This endpoint returns a paginated
    response. Use the 'limit' parameter to control page size (1-200, defaults to 100). The response
    includes a 'cursor' field - pass this value in the 'cursor' parameter of your next request to get
    the next page. An empty cursor indicates no more pages are available.

    Args:
        limit (Union[Unset, int]): Parameter to specify the number of results per page. Defaults
            to 100. Maximum value is 200.
        cursor (Union[Unset, str]): Parameter to specify the pagination cursor. Use the cursor
            value returned from the previous response to get the next page of results. Leave empty for
            the first page.
        with_nested_markets (Union[Unset, bool]): Parameter to specify if nested markets should be
            included in the response. When true, each event will include a 'markets' field containing
            a list of Market objects associated with that event.
        status (Union[Unset, str]): Filter by event status. Possible values: 'open', 'closed',
            'settled'. Leave empty to return events with any status.
        series_ticker (Union[Unset, str]): Filter events by series ticker. Returns only events
            belonging to the specified series.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetEventsResponse
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        with_nested_markets=with_nested_markets,
        status=status,
        series_ticker=series_ticker,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    with_nested_markets: Union[Unset, bool] = UNSET,
    status: Union[Unset, str] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetEventsResponse]:
    """Get Events

      Endpoint for getting data about all events.  An event represents a real-world occurrence that can
    be traded on, such as an election, sports game, or economic indicator release. Events contain one or
    more markets where users can place trades on different outcomes.  This endpoint returns a paginated
    response. Use the 'limit' parameter to control page size (1-200, defaults to 100). The response
    includes a 'cursor' field - pass this value in the 'cursor' parameter of your next request to get
    the next page. An empty cursor indicates no more pages are available.

    Args:
        limit (Union[Unset, int]): Parameter to specify the number of results per page. Defaults
            to 100. Maximum value is 200.
        cursor (Union[Unset, str]): Parameter to specify the pagination cursor. Use the cursor
            value returned from the previous response to get the next page of results. Leave empty for
            the first page.
        with_nested_markets (Union[Unset, bool]): Parameter to specify if nested markets should be
            included in the response. When true, each event will include a 'markets' field containing
            a list of Market objects associated with that event.
        status (Union[Unset, str]): Filter by event status. Possible values: 'open', 'closed',
            'settled'. Leave empty to return events with any status.
        series_ticker (Union[Unset, str]): Filter events by series ticker. Returns only events
            belonging to the specified series.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetEventsResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        with_nested_markets=with_nested_markets,
        status=status,
        series_ticker=series_ticker,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    with_nested_markets: Union[Unset, bool] = UNSET,
    status: Union[Unset, str] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetEventsResponse]:
    """Get Events

      Endpoint for getting data about all events.  An event represents a real-world occurrence that can
    be traded on, such as an election, sports game, or economic indicator release. Events contain one or
    more markets where users can place trades on different outcomes.  This endpoint returns a paginated
    response. Use the 'limit' parameter to control page size (1-200, defaults to 100). The response
    includes a 'cursor' field - pass this value in the 'cursor' parameter of your next request to get
    the next page. An empty cursor indicates no more pages are available.

    Args:
        limit (Union[Unset, int]): Parameter to specify the number of results per page. Defaults
            to 100. Maximum value is 200.
        cursor (Union[Unset, str]): Parameter to specify the pagination cursor. Use the cursor
            value returned from the previous response to get the next page of results. Leave empty for
            the first page.
        with_nested_markets (Union[Unset, bool]): Parameter to specify if nested markets should be
            included in the response. When true, each event will include a 'markets' field containing
            a list of Market objects associated with that event.
        status (Union[Unset, str]): Filter by event status. Possible values: 'open', 'closed',
            'settled'. Leave empty to return events with any status.
        series_ticker (Union[Unset, str]): Filter events by series ticker. Returns only events
            belonging to the specified series.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetEventsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            with_nested_markets=with_nested_markets,
            status=status,
            series_ticker=series_ticker,
        )
    ).parsed
