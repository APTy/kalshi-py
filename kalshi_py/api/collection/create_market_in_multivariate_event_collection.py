from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_market_in_multivariate_event_collection_request import (
    CreateMarketInMultivariateEventCollectionRequest,
)
from ...models.create_market_in_multivariate_event_collection_response import (
    CreateMarketInMultivariateEventCollectionResponse,
)
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    collection_ticker: str,
    *,
    body: CreateMarketInMultivariateEventCollectionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/multivariate_event_collections/{collection_ticker}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateMarketInMultivariateEventCollectionResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = CreateMarketInMultivariateEventCollectionResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CreateMarketInMultivariateEventCollectionResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_ticker: str,
    *,
    client: AuthenticatedClient,
    body: CreateMarketInMultivariateEventCollectionRequest,
) -> Response[Union[CreateMarketInMultivariateEventCollectionResponse, ErrorResponse]]:
    """Create Market In Multivariate Event Collection

      Endpoint for looking up an individual market in a multivariate event collection. This endpoint must
    be hit at least once before trading or looking up a market.

    Args:
        collection_ticker (str):
        body (CreateMarketInMultivariateEventCollectionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateMarketInMultivariateEventCollectionResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        collection_ticker=collection_ticker,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_ticker: str,
    *,
    client: AuthenticatedClient,
    body: CreateMarketInMultivariateEventCollectionRequest,
) -> Optional[Union[CreateMarketInMultivariateEventCollectionResponse, ErrorResponse]]:
    """Create Market In Multivariate Event Collection

      Endpoint for looking up an individual market in a multivariate event collection. This endpoint must
    be hit at least once before trading or looking up a market.

    Args:
        collection_ticker (str):
        body (CreateMarketInMultivariateEventCollectionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateMarketInMultivariateEventCollectionResponse, ErrorResponse]
    """

    return sync_detailed(
        collection_ticker=collection_ticker,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    collection_ticker: str,
    *,
    client: AuthenticatedClient,
    body: CreateMarketInMultivariateEventCollectionRequest,
) -> Response[Union[CreateMarketInMultivariateEventCollectionResponse, ErrorResponse]]:
    """Create Market In Multivariate Event Collection

      Endpoint for looking up an individual market in a multivariate event collection. This endpoint must
    be hit at least once before trading or looking up a market.

    Args:
        collection_ticker (str):
        body (CreateMarketInMultivariateEventCollectionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateMarketInMultivariateEventCollectionResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        collection_ticker=collection_ticker,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_ticker: str,
    *,
    client: AuthenticatedClient,
    body: CreateMarketInMultivariateEventCollectionRequest,
) -> Optional[Union[CreateMarketInMultivariateEventCollectionResponse, ErrorResponse]]:
    """Create Market In Multivariate Event Collection

      Endpoint for looking up an individual market in a multivariate event collection. This endpoint must
    be hit at least once before trading or looking up a market.

    Args:
        collection_ticker (str):
        body (CreateMarketInMultivariateEventCollectionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateMarketInMultivariateEventCollectionResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            collection_ticker=collection_ticker,
            client=client,
            body=body,
        )
    ).parsed
