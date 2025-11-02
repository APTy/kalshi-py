from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_multivariate_event_collection_response import GetMultivariateEventCollectionResponse
from ...types import Response


def _get_kwargs(
    collection_ticker: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/multivariate_event_collections/{collection_ticker}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetMultivariateEventCollectionResponse]]:
    if response.status_code == 200:
        response_200 = GetMultivariateEventCollectionResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetMultivariateEventCollectionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetMultivariateEventCollectionResponse]]:
    """Get Multivariate Event Collection

      Endpoint for getting data about a multivariate event collection by its ticker.

    Args:
        collection_ticker (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetMultivariateEventCollectionResponse]]
    """

    kwargs = _get_kwargs(
        collection_ticker=collection_ticker,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetMultivariateEventCollectionResponse]]:
    """Get Multivariate Event Collection

      Endpoint for getting data about a multivariate event collection by its ticker.

    Args:
        collection_ticker (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetMultivariateEventCollectionResponse]
    """

    return sync_detailed(
        collection_ticker=collection_ticker,
        client=client,
    ).parsed


async def asyncio_detailed(
    collection_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetMultivariateEventCollectionResponse]]:
    """Get Multivariate Event Collection

      Endpoint for getting data about a multivariate event collection by its ticker.

    Args:
        collection_ticker (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetMultivariateEventCollectionResponse]]
    """

    kwargs = _get_kwargs(
        collection_ticker=collection_ticker,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetMultivariateEventCollectionResponse]]:
    """Get Multivariate Event Collection

      Endpoint for getting data about a multivariate event collection by its ticker.

    Args:
        collection_ticker (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetMultivariateEventCollectionResponse]
    """

    return (
        await asyncio_detailed(
            collection_ticker=collection_ticker,
            client=client,
        )
    ).parsed
