from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_get_multivariate_event_collection_lookup_history_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionLookupHistoryResponse,
)
from ...types import Response


def _get_kwargs(
    collection_ticker: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/multivariate_event_collections/{collection_ticker}/lookup",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionLookupHistoryResponse]:
    if response.status_code == 200:
        response_200 = (
            GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionLookupHistoryResponse.from_dict(
                response.json()
            )
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionLookupHistoryResponse]:
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
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionLookupHistoryResponse]:
    """Get Multivariate Event Collection Lookup History

      Endpoint for retrieving which markets in an event collection were recently looked up.

    Args:
        collection_ticker (str): Collection ticker

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionLookupHistoryResponse]
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
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionLookupHistoryResponse]:
    """Get Multivariate Event Collection Lookup History

      Endpoint for retrieving which markets in an event collection were recently looked up.

    Args:
        collection_ticker (str): Collection ticker

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionLookupHistoryResponse
    """

    return sync_detailed(
        collection_ticker=collection_ticker,
        client=client,
    ).parsed


async def asyncio_detailed(
    collection_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionLookupHistoryResponse]:
    """Get Multivariate Event Collection Lookup History

      Endpoint for retrieving which markets in an event collection were recently looked up.

    Args:
        collection_ticker (str): Collection ticker

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionLookupHistoryResponse]
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
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionLookupHistoryResponse]:
    """Get Multivariate Event Collection Lookup History

      Endpoint for retrieving which markets in an event collection were recently looked up.

    Args:
        collection_ticker (str): Collection ticker

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionLookupHistoryResponse
    """

    return (
        await asyncio_detailed(
            collection_ticker=collection_ticker,
            client=client,
        )
    ).parsed
