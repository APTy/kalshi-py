from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_multivariate_event_collection_lookup_history_lookback_seconds import (
    GetMultivariateEventCollectionLookupHistoryLookbackSeconds,
)
from ...models.get_multivariate_event_collection_lookup_history_response import (
    GetMultivariateEventCollectionLookupHistoryResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    collection_ticker: str,
    *,
    lookback_seconds: GetMultivariateEventCollectionLookupHistoryLookbackSeconds,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_lookback_seconds = lookback_seconds.value
    params["lookback_seconds"] = json_lookback_seconds

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/multivariate_event_collections/{collection_ticker}/lookup",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetMultivariateEventCollectionLookupHistoryResponse]]:
    if response.status_code == 200:
        response_200 = GetMultivariateEventCollectionLookupHistoryResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetMultivariateEventCollectionLookupHistoryResponse]]:
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
    lookback_seconds: GetMultivariateEventCollectionLookupHistoryLookbackSeconds,
) -> Response[Union[ErrorResponse, GetMultivariateEventCollectionLookupHistoryResponse]]:
    """Get Multivariate Event Collection Lookup History

      Endpoint for retrieving which markets in an event collection were recently looked up.

    Args:
        collection_ticker (str):
        lookback_seconds (GetMultivariateEventCollectionLookupHistoryLookbackSeconds):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetMultivariateEventCollectionLookupHistoryResponse]]
    """

    kwargs = _get_kwargs(
        collection_ticker=collection_ticker,
        lookback_seconds=lookback_seconds,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
    lookback_seconds: GetMultivariateEventCollectionLookupHistoryLookbackSeconds,
) -> Optional[Union[ErrorResponse, GetMultivariateEventCollectionLookupHistoryResponse]]:
    """Get Multivariate Event Collection Lookup History

      Endpoint for retrieving which markets in an event collection were recently looked up.

    Args:
        collection_ticker (str):
        lookback_seconds (GetMultivariateEventCollectionLookupHistoryLookbackSeconds):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetMultivariateEventCollectionLookupHistoryResponse]
    """

    return sync_detailed(
        collection_ticker=collection_ticker,
        client=client,
        lookback_seconds=lookback_seconds,
    ).parsed


async def asyncio_detailed(
    collection_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
    lookback_seconds: GetMultivariateEventCollectionLookupHistoryLookbackSeconds,
) -> Response[Union[ErrorResponse, GetMultivariateEventCollectionLookupHistoryResponse]]:
    """Get Multivariate Event Collection Lookup History

      Endpoint for retrieving which markets in an event collection were recently looked up.

    Args:
        collection_ticker (str):
        lookback_seconds (GetMultivariateEventCollectionLookupHistoryLookbackSeconds):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetMultivariateEventCollectionLookupHistoryResponse]]
    """

    kwargs = _get_kwargs(
        collection_ticker=collection_ticker,
        lookback_seconds=lookback_seconds,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
    lookback_seconds: GetMultivariateEventCollectionLookupHistoryLookbackSeconds,
) -> Optional[Union[ErrorResponse, GetMultivariateEventCollectionLookupHistoryResponse]]:
    """Get Multivariate Event Collection Lookup History

      Endpoint for retrieving which markets in an event collection were recently looked up.

    Args:
        collection_ticker (str):
        lookback_seconds (GetMultivariateEventCollectionLookupHistoryLookbackSeconds):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetMultivariateEventCollectionLookupHistoryResponse]
    """

    return (
        await asyncio_detailed(
            collection_ticker=collection_ticker,
            client=client,
            lookback_seconds=lookback_seconds,
        )
    ).parsed
