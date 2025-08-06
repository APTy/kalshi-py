from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_get_orders_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelGetOrdersResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    status: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ticker"] = ticker

    params["event_ticker"] = event_ticker

    params["min_ts"] = min_ts

    params["max_ts"] = max_ts

    params["status"] = status

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/portfolio/orders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetOrdersResponse]:
    if response.status_code == 200:
        response_200 = GithubComKalshiExchangeInfraSvcApi2ModelGetOrdersResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetOrdersResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    status: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetOrdersResponse]:
    """Get Orders

      Endpoint for getting all orders for the member.

    Args:
        ticker (Union[Unset, str]): Restricts the response to orders in a single market.
        event_ticker (Union[Unset, str]): Restricts the response to orders in a single event.
        min_ts (Union[Unset, int]): Restricts the response to orders after a timestamp, formatted
            as a Unix Timestamp.
        max_ts (Union[Unset, int]): Restricts the response to orders before a timestamp, formatted
            as a Unix Timestamp.
        status (Union[Unset, str]): Restricts the response to orders that have a certain status:
            resting, canceled, or executed.
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in
            the pagination. Use the value returned from the previous response to get the next page.
        limit (Union[Unset, int]): Parameter to specify the number of results per page. Defaults
            to 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetOrdersResponse]
    """

    kwargs = _get_kwargs(
        ticker=ticker,
        event_ticker=event_ticker,
        min_ts=min_ts,
        max_ts=max_ts,
        status=status,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    status: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetOrdersResponse]:
    """Get Orders

      Endpoint for getting all orders for the member.

    Args:
        ticker (Union[Unset, str]): Restricts the response to orders in a single market.
        event_ticker (Union[Unset, str]): Restricts the response to orders in a single event.
        min_ts (Union[Unset, int]): Restricts the response to orders after a timestamp, formatted
            as a Unix Timestamp.
        max_ts (Union[Unset, int]): Restricts the response to orders before a timestamp, formatted
            as a Unix Timestamp.
        status (Union[Unset, str]): Restricts the response to orders that have a certain status:
            resting, canceled, or executed.
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in
            the pagination. Use the value returned from the previous response to get the next page.
        limit (Union[Unset, int]): Parameter to specify the number of results per page. Defaults
            to 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetOrdersResponse
    """

    return sync_detailed(
        client=client,
        ticker=ticker,
        event_ticker=event_ticker,
        min_ts=min_ts,
        max_ts=max_ts,
        status=status,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    status: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetOrdersResponse]:
    """Get Orders

      Endpoint for getting all orders for the member.

    Args:
        ticker (Union[Unset, str]): Restricts the response to orders in a single market.
        event_ticker (Union[Unset, str]): Restricts the response to orders in a single event.
        min_ts (Union[Unset, int]): Restricts the response to orders after a timestamp, formatted
            as a Unix Timestamp.
        max_ts (Union[Unset, int]): Restricts the response to orders before a timestamp, formatted
            as a Unix Timestamp.
        status (Union[Unset, str]): Restricts the response to orders that have a certain status:
            resting, canceled, or executed.
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in
            the pagination. Use the value returned from the previous response to get the next page.
        limit (Union[Unset, int]): Parameter to specify the number of results per page. Defaults
            to 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetOrdersResponse]
    """

    kwargs = _get_kwargs(
        ticker=ticker,
        event_ticker=event_ticker,
        min_ts=min_ts,
        max_ts=max_ts,
        status=status,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    status: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetOrdersResponse]:
    """Get Orders

      Endpoint for getting all orders for the member.

    Args:
        ticker (Union[Unset, str]): Restricts the response to orders in a single market.
        event_ticker (Union[Unset, str]): Restricts the response to orders in a single event.
        min_ts (Union[Unset, int]): Restricts the response to orders after a timestamp, formatted
            as a Unix Timestamp.
        max_ts (Union[Unset, int]): Restricts the response to orders before a timestamp, formatted
            as a Unix Timestamp.
        status (Union[Unset, str]): Restricts the response to orders that have a certain status:
            resting, canceled, or executed.
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in
            the pagination. Use the value returned from the previous response to get the next page.
        limit (Union[Unset, int]): Parameter to specify the number of results per page. Defaults
            to 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetOrdersResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            ticker=ticker,
            event_ticker=event_ticker,
            min_ts=min_ts,
            max_ts=max_ts,
            status=status,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
