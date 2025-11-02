from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_multivariate_event_collections_response import GetMultivariateEventCollectionsResponse
from ...models.get_multivariate_event_collections_status import GetMultivariateEventCollectionsStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: Union[Unset, GetMultivariateEventCollectionsStatus] = UNSET,
    associated_event_ticker: Union[Unset, str] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["associated_event_ticker"] = associated_event_ticker

    params["series_ticker"] = series_ticker

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/multivariate_event_collections",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetMultivariateEventCollectionsResponse]]:
    if response.status_code == 200:
        response_200 = GetMultivariateEventCollectionsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetMultivariateEventCollectionsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, GetMultivariateEventCollectionsStatus] = UNSET,
    associated_event_ticker: Union[Unset, str] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetMultivariateEventCollectionsResponse]]:
    """Get Multivariate Event Collections

      Endpoint for getting data about multivariate event collections.

    Args:
        status (Union[Unset, GetMultivariateEventCollectionsStatus]):
        associated_event_ticker (Union[Unset, str]):
        series_ticker (Union[Unset, str]):
        limit (Union[Unset, int]):
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetMultivariateEventCollectionsResponse]]
    """

    kwargs = _get_kwargs(
        status=status,
        associated_event_ticker=associated_event_ticker,
        series_ticker=series_ticker,
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
    status: Union[Unset, GetMultivariateEventCollectionsStatus] = UNSET,
    associated_event_ticker: Union[Unset, str] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetMultivariateEventCollectionsResponse]]:
    """Get Multivariate Event Collections

      Endpoint for getting data about multivariate event collections.

    Args:
        status (Union[Unset, GetMultivariateEventCollectionsStatus]):
        associated_event_ticker (Union[Unset, str]):
        series_ticker (Union[Unset, str]):
        limit (Union[Unset, int]):
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetMultivariateEventCollectionsResponse]
    """

    return sync_detailed(
        client=client,
        status=status,
        associated_event_ticker=associated_event_ticker,
        series_ticker=series_ticker,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, GetMultivariateEventCollectionsStatus] = UNSET,
    associated_event_ticker: Union[Unset, str] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetMultivariateEventCollectionsResponse]]:
    """Get Multivariate Event Collections

      Endpoint for getting data about multivariate event collections.

    Args:
        status (Union[Unset, GetMultivariateEventCollectionsStatus]):
        associated_event_ticker (Union[Unset, str]):
        series_ticker (Union[Unset, str]):
        limit (Union[Unset, int]):
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetMultivariateEventCollectionsResponse]]
    """

    kwargs = _get_kwargs(
        status=status,
        associated_event_ticker=associated_event_ticker,
        series_ticker=series_ticker,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, GetMultivariateEventCollectionsStatus] = UNSET,
    associated_event_ticker: Union[Unset, str] = UNSET,
    series_ticker: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetMultivariateEventCollectionsResponse]]:
    """Get Multivariate Event Collections

      Endpoint for getting data about multivariate event collections.

    Args:
        status (Union[Unset, GetMultivariateEventCollectionsStatus]):
        associated_event_ticker (Union[Unset, str]):
        series_ticker (Union[Unset, str]):
        limit (Union[Unset, int]):
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetMultivariateEventCollectionsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            associated_event_ticker=associated_event_ticker,
            series_ticker=series_ticker,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
