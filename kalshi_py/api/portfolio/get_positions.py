from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_get_positions_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    count_filter: Union[Unset, str] = UNSET,
    settlement_status: Union[Unset, str] = UNSET,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    params["count_filter"] = count_filter

    params["settlement_status"] = settlement_status

    params["ticker"] = ticker

    params["event_ticker"] = event_ticker

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/portfolio/positions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponse]:
    if response.status_code == 200:
        response_200 = GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    count_filter: Union[Unset, str] = UNSET,
    settlement_status: Union[Unset, str] = UNSET,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponse]:
    """Get Positions

      Endpoint for getting all market positions for the member.

    Args:
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in
            the pagination. Use the value returned from the previous response to get the next page.
        limit (Union[Unset, int]): Parameter to specify the number of results per page. Defaults
            to 100.
        count_filter (Union[Unset, str]): Restricts the positions to those with any of following
            fields with non-zero values, as a comma separated list. The following values are accepted:
            position, total_traded, resting_order_count
        settlement_status (Union[Unset, str]): Settlement status of the markets to return.
            Defaults to unsettled.
        ticker (Union[Unset, str]): Ticker of desired positions.
        event_ticker (Union[Unset, str]): Event ticker of desired positions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponse]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        count_filter=count_filter,
        settlement_status=settlement_status,
        ticker=ticker,
        event_ticker=event_ticker,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    count_filter: Union[Unset, str] = UNSET,
    settlement_status: Union[Unset, str] = UNSET,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponse]:
    """Get Positions

      Endpoint for getting all market positions for the member.

    Args:
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in
            the pagination. Use the value returned from the previous response to get the next page.
        limit (Union[Unset, int]): Parameter to specify the number of results per page. Defaults
            to 100.
        count_filter (Union[Unset, str]): Restricts the positions to those with any of following
            fields with non-zero values, as a comma separated list. The following values are accepted:
            position, total_traded, resting_order_count
        settlement_status (Union[Unset, str]): Settlement status of the markets to return.
            Defaults to unsettled.
        ticker (Union[Unset, str]): Ticker of desired positions.
        event_ticker (Union[Unset, str]): Event ticker of desired positions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponse
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        limit=limit,
        count_filter=count_filter,
        settlement_status=settlement_status,
        ticker=ticker,
        event_ticker=event_ticker,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    count_filter: Union[Unset, str] = UNSET,
    settlement_status: Union[Unset, str] = UNSET,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponse]:
    """Get Positions

      Endpoint for getting all market positions for the member.

    Args:
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in
            the pagination. Use the value returned from the previous response to get the next page.
        limit (Union[Unset, int]): Parameter to specify the number of results per page. Defaults
            to 100.
        count_filter (Union[Unset, str]): Restricts the positions to those with any of following
            fields with non-zero values, as a comma separated list. The following values are accepted:
            position, total_traded, resting_order_count
        settlement_status (Union[Unset, str]): Settlement status of the markets to return.
            Defaults to unsettled.
        ticker (Union[Unset, str]): Ticker of desired positions.
        event_ticker (Union[Unset, str]): Event ticker of desired positions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponse]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        count_filter=count_filter,
        settlement_status=settlement_status,
        ticker=ticker,
        event_ticker=event_ticker,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    count_filter: Union[Unset, str] = UNSET,
    settlement_status: Union[Unset, str] = UNSET,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponse]:
    """Get Positions

      Endpoint for getting all market positions for the member.

    Args:
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in
            the pagination. Use the value returned from the previous response to get the next page.
        limit (Union[Unset, int]): Parameter to specify the number of results per page. Defaults
            to 100.
        count_filter (Union[Unset, str]): Restricts the positions to those with any of following
            fields with non-zero values, as a comma separated list. The following values are accepted:
            position, total_traded, resting_order_count
        settlement_status (Union[Unset, str]): Settlement status of the markets to return.
            Defaults to unsettled.
        ticker (Union[Unset, str]): Ticker of desired positions.
        event_ticker (Union[Unset, str]): Event ticker of desired positions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetPositionsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            limit=limit,
            count_filter=count_filter,
            settlement_status=settlement_status,
            ticker=ticker,
            event_ticker=event_ticker,
        )
    ).parsed
