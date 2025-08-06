from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_get_milestones_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelGetMilestonesResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    minimum_start_date: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    competition: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    related_event_ticker: Union[Unset, str] = UNSET,
    limit: int,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["minimum_start_date"] = minimum_start_date

    params["category"] = category

    params["competition"] = competition

    params["type"] = type_

    params["related_event_ticker"] = related_event_ticker

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/milestones",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetMilestonesResponse]:
    if response.status_code == 200:
        response_200 = GithubComKalshiExchangeInfraSvcApi2ModelGetMilestonesResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMilestonesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    minimum_start_date: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    competition: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    related_event_ticker: Union[Unset, str] = UNSET,
    limit: int,
    cursor: Union[Unset, str] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMilestonesResponse]:
    """Get Milestones

      Endpoint for getting data about milestones with optional filtering.

    Args:
        minimum_start_date (Union[Unset, str]): Minimum start date to filter milestones. Format:
            RFC3339 timestamp
        category (Union[Unset, str]): Filter by milestone category
        competition (Union[Unset, str]): Filter by competition
        type_ (Union[Unset, str]): Filter by milestone type
        related_event_ticker (Union[Unset, str]): Filter by related event ticker
        limit (int): Number of milestones to return per page
        cursor (Union[Unset, str]): Pagination cursor. Use the cursor value returned from the
            previous response to get the next page of results

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMilestonesResponse]
    """

    kwargs = _get_kwargs(
        minimum_start_date=minimum_start_date,
        category=category,
        competition=competition,
        type_=type_,
        related_event_ticker=related_event_ticker,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    minimum_start_date: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    competition: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    related_event_ticker: Union[Unset, str] = UNSET,
    limit: int,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetMilestonesResponse]:
    """Get Milestones

      Endpoint for getting data about milestones with optional filtering.

    Args:
        minimum_start_date (Union[Unset, str]): Minimum start date to filter milestones. Format:
            RFC3339 timestamp
        category (Union[Unset, str]): Filter by milestone category
        competition (Union[Unset, str]): Filter by competition
        type_ (Union[Unset, str]): Filter by milestone type
        related_event_ticker (Union[Unset, str]): Filter by related event ticker
        limit (int): Number of milestones to return per page
        cursor (Union[Unset, str]): Pagination cursor. Use the cursor value returned from the
            previous response to get the next page of results

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetMilestonesResponse
    """

    return sync_detailed(
        client=client,
        minimum_start_date=minimum_start_date,
        category=category,
        competition=competition,
        type_=type_,
        related_event_ticker=related_event_ticker,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    minimum_start_date: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    competition: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    related_event_ticker: Union[Unset, str] = UNSET,
    limit: int,
    cursor: Union[Unset, str] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMilestonesResponse]:
    """Get Milestones

      Endpoint for getting data about milestones with optional filtering.

    Args:
        minimum_start_date (Union[Unset, str]): Minimum start date to filter milestones. Format:
            RFC3339 timestamp
        category (Union[Unset, str]): Filter by milestone category
        competition (Union[Unset, str]): Filter by competition
        type_ (Union[Unset, str]): Filter by milestone type
        related_event_ticker (Union[Unset, str]): Filter by related event ticker
        limit (int): Number of milestones to return per page
        cursor (Union[Unset, str]): Pagination cursor. Use the cursor value returned from the
            previous response to get the next page of results

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMilestonesResponse]
    """

    kwargs = _get_kwargs(
        minimum_start_date=minimum_start_date,
        category=category,
        competition=competition,
        type_=type_,
        related_event_ticker=related_event_ticker,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    minimum_start_date: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    competition: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    related_event_ticker: Union[Unset, str] = UNSET,
    limit: int,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetMilestonesResponse]:
    """Get Milestones

      Endpoint for getting data about milestones with optional filtering.

    Args:
        minimum_start_date (Union[Unset, str]): Minimum start date to filter milestones. Format:
            RFC3339 timestamp
        category (Union[Unset, str]): Filter by milestone category
        competition (Union[Unset, str]): Filter by competition
        type_ (Union[Unset, str]): Filter by milestone type
        related_event_ticker (Union[Unset, str]): Filter by related event ticker
        limit (int): Number of milestones to return per page
        cursor (Union[Unset, str]): Pagination cursor. Use the cursor value returned from the
            previous response to get the next page of results

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetMilestonesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            minimum_start_date=minimum_start_date,
            category=category,
            competition=competition,
            type_=type_,
            related_event_ticker=related_event_ticker,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
