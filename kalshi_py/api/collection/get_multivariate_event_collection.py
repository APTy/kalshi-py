from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.svc_api_2_model_get_multivariate_event_collection_response import (
    SvcApi2ModelGetMultivariateEventCollectionResponse,
)
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
) -> Optional[SvcApi2ModelGetMultivariateEventCollectionResponse]:
    if response.status_code == 200:
        response_200 = SvcApi2ModelGetMultivariateEventCollectionResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SvcApi2ModelGetMultivariateEventCollectionResponse]:
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
) -> Response[SvcApi2ModelGetMultivariateEventCollectionResponse]:
    """Get Multivariate Event Collection

      Endpoint for getting data about a multivariate event collection by its ticker.

    Args:
        collection_ticker (str): Collection ticker

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SvcApi2ModelGetMultivariateEventCollectionResponse]
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
) -> Optional[SvcApi2ModelGetMultivariateEventCollectionResponse]:
    """Get Multivariate Event Collection

      Endpoint for getting data about a multivariate event collection by its ticker.

    Args:
        collection_ticker (str): Collection ticker

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SvcApi2ModelGetMultivariateEventCollectionResponse
    """

    return sync_detailed(
        collection_ticker=collection_ticker,
        client=client,
    ).parsed


async def asyncio_detailed(
    collection_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[SvcApi2ModelGetMultivariateEventCollectionResponse]:
    """Get Multivariate Event Collection

      Endpoint for getting data about a multivariate event collection by its ticker.

    Args:
        collection_ticker (str): Collection ticker

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SvcApi2ModelGetMultivariateEventCollectionResponse]
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
) -> Optional[SvcApi2ModelGetMultivariateEventCollectionResponse]:
    """Get Multivariate Event Collection

      Endpoint for getting data about a multivariate event collection by its ticker.

    Args:
        collection_ticker (str): Collection ticker

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SvcApi2ModelGetMultivariateEventCollectionResponse
    """

    return (
        await asyncio_detailed(
            collection_ticker=collection_ticker,
            client=client,
        )
    ).parsed
