from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.lookup_tickers_for_market_in_multivariate_event_collection_request import (
    LookupTickersForMarketInMultivariateEventCollectionRequest,
)
from ...models.lookup_tickers_for_market_in_multivariate_event_collection_response import (
    LookupTickersForMarketInMultivariateEventCollectionResponse,
)
from ...types import Response


def _get_kwargs(
    collection_ticker: str,
    *,
    body: LookupTickersForMarketInMultivariateEventCollectionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/multivariate_event_collections/{collection_ticker}/lookup",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, LookupTickersForMarketInMultivariateEventCollectionResponse]]:
    if response.status_code == 200:
        response_200 = LookupTickersForMarketInMultivariateEventCollectionResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
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
) -> Response[Union[ErrorResponse, LookupTickersForMarketInMultivariateEventCollectionResponse]]:
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
    body: LookupTickersForMarketInMultivariateEventCollectionRequest,
) -> Response[Union[ErrorResponse, LookupTickersForMarketInMultivariateEventCollectionResponse]]:
    """Lookup Tickers For Market In Multivariate Event Collection

      Endpoint for looking up an individual market in a multivariate event collection. If
    CreateMarketInMultivariateEventCollection has never been hit with that variable combination before,
    this will return a 404.

    Args:
        collection_ticker (str):
        body (LookupTickersForMarketInMultivariateEventCollectionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, LookupTickersForMarketInMultivariateEventCollectionResponse]]
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
    body: LookupTickersForMarketInMultivariateEventCollectionRequest,
) -> Optional[Union[ErrorResponse, LookupTickersForMarketInMultivariateEventCollectionResponse]]:
    """Lookup Tickers For Market In Multivariate Event Collection

      Endpoint for looking up an individual market in a multivariate event collection. If
    CreateMarketInMultivariateEventCollection has never been hit with that variable combination before,
    this will return a 404.

    Args:
        collection_ticker (str):
        body (LookupTickersForMarketInMultivariateEventCollectionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, LookupTickersForMarketInMultivariateEventCollectionResponse]
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
    body: LookupTickersForMarketInMultivariateEventCollectionRequest,
) -> Response[Union[ErrorResponse, LookupTickersForMarketInMultivariateEventCollectionResponse]]:
    """Lookup Tickers For Market In Multivariate Event Collection

      Endpoint for looking up an individual market in a multivariate event collection. If
    CreateMarketInMultivariateEventCollection has never been hit with that variable combination before,
    this will return a 404.

    Args:
        collection_ticker (str):
        body (LookupTickersForMarketInMultivariateEventCollectionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, LookupTickersForMarketInMultivariateEventCollectionResponse]]
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
    body: LookupTickersForMarketInMultivariateEventCollectionRequest,
) -> Optional[Union[ErrorResponse, LookupTickersForMarketInMultivariateEventCollectionResponse]]:
    """Lookup Tickers For Market In Multivariate Event Collection

      Endpoint for looking up an individual market in a multivariate event collection. If
    CreateMarketInMultivariateEventCollection has never been hit with that variable combination before,
    this will return a 404.

    Args:
        collection_ticker (str):
        body (LookupTickersForMarketInMultivariateEventCollectionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, LookupTickersForMarketInMultivariateEventCollectionResponse]
    """

    return (
        await asyncio_detailed(
            collection_ticker=collection_ticker,
            client=client,
            body=body,
        )
    ).parsed
