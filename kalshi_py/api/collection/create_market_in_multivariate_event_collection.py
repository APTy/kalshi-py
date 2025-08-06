from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_create_market_in_multivariate_event_collection_request import (
    GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionRequest,
)
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_create_market_in_multivariate_event_collection_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionResponse,
)
from ...types import Response


def _get_kwargs(
    collection_ticker: str,
    *,
    body: GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionRequest,
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
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionResponse]:
    if response.status_code == 200:
        response_200 = (
            GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionResponse.from_dict(
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
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionResponse]:
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
    body: GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionRequest,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionResponse]:
    """Create Market In Multivariate Event Collection

      Endpoint for looking up an individual market in a multivariate event collection. This endpoint must
    be hit at least once before trading or looking up a market.

    Args:
        collection_ticker (str): Collection ticker
        body (GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionReq
            uest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionResponse]
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
    client: Union[AuthenticatedClient, Client],
    body: GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionRequest,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionResponse]:
    """Create Market In Multivariate Event Collection

      Endpoint for looking up an individual market in a multivariate event collection. This endpoint must
    be hit at least once before trading or looking up a market.

    Args:
        collection_ticker (str): Collection ticker
        body (GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionReq
            uest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionResponse
    """

    return sync_detailed(
        collection_ticker=collection_ticker,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    collection_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionRequest,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionResponse]:
    """Create Market In Multivariate Event Collection

      Endpoint for looking up an individual market in a multivariate event collection. This endpoint must
    be hit at least once before trading or looking up a market.

    Args:
        collection_ticker (str): Collection ticker
        body (GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionReq
            uest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionResponse]
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
    client: Union[AuthenticatedClient, Client],
    body: GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionRequest,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionResponse]:
    """Create Market In Multivariate Event Collection

      Endpoint for looking up an individual market in a multivariate event collection. This endpoint must
    be hit at least once before trading or looking up a market.

    Args:
        collection_ticker (str): Collection ticker
        body (GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionReq
            uest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelCreateMarketInMultivariateEventCollectionResponse
    """

    return (
        await asyncio_detailed(
            collection_ticker=collection_ticker,
            client=client,
            body=body,
        )
    ).parsed
