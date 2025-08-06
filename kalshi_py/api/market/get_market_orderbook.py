from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_get_market_orderbook_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelGetMarketOrderbookResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ticker: str,
    *,
    depth: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["depth"] = depth

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/markets/{ticker}/orderbook",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketOrderbookResponse]:
    if response.status_code == 200:
        response_200 = GithubComKalshiExchangeInfraSvcApi2ModelGetMarketOrderbookResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketOrderbookResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
    depth: Union[Unset, int] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketOrderbookResponse]:
    """Get Market Order Book

      Endpoint for getting the current order book for a specific market.  The order book shows all active
    bid orders for both yes and no sides of a binary market. It returns yes bids and no bids only (no
    asks are returned). This is because in binary markets, a bid for yes at price X is equivalent to an
    ask for no at price (100-X). For example, a yes bid at 7¢ is the same as a no ask at 93¢, with
    identical contract sizes.  Each side shows price levels with their corresponding quantities and
    order counts, organized from best to worst prices.

    Args:
        ticker (str): Market ticker - unique identifier for the specific market
        depth (Union[Unset, int]): Maximum number of price levels to return per side (yes bids/no
            bids). Defaults to all levels. Maximum value is 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketOrderbookResponse]
    """

    kwargs = _get_kwargs(
        ticker=ticker,
        depth=depth,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
    depth: Union[Unset, int] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketOrderbookResponse]:
    """Get Market Order Book

      Endpoint for getting the current order book for a specific market.  The order book shows all active
    bid orders for both yes and no sides of a binary market. It returns yes bids and no bids only (no
    asks are returned). This is because in binary markets, a bid for yes at price X is equivalent to an
    ask for no at price (100-X). For example, a yes bid at 7¢ is the same as a no ask at 93¢, with
    identical contract sizes.  Each side shows price levels with their corresponding quantities and
    order counts, organized from best to worst prices.

    Args:
        ticker (str): Market ticker - unique identifier for the specific market
        depth (Union[Unset, int]): Maximum number of price levels to return per side (yes bids/no
            bids). Defaults to all levels. Maximum value is 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetMarketOrderbookResponse
    """

    return sync_detailed(
        ticker=ticker,
        client=client,
        depth=depth,
    ).parsed


async def asyncio_detailed(
    ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
    depth: Union[Unset, int] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketOrderbookResponse]:
    """Get Market Order Book

      Endpoint for getting the current order book for a specific market.  The order book shows all active
    bid orders for both yes and no sides of a binary market. It returns yes bids and no bids only (no
    asks are returned). This is because in binary markets, a bid for yes at price X is equivalent to an
    ask for no at price (100-X). For example, a yes bid at 7¢ is the same as a no ask at 93¢, with
    identical contract sizes.  Each side shows price levels with their corresponding quantities and
    order counts, organized from best to worst prices.

    Args:
        ticker (str): Market ticker - unique identifier for the specific market
        depth (Union[Unset, int]): Maximum number of price levels to return per side (yes bids/no
            bids). Defaults to all levels. Maximum value is 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketOrderbookResponse]
    """

    kwargs = _get_kwargs(
        ticker=ticker,
        depth=depth,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
    depth: Union[Unset, int] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketOrderbookResponse]:
    """Get Market Order Book

      Endpoint for getting the current order book for a specific market.  The order book shows all active
    bid orders for both yes and no sides of a binary market. It returns yes bids and no bids only (no
    asks are returned). This is because in binary markets, a bid for yes at price X is equivalent to an
    ask for no at price (100-X). For example, a yes bid at 7¢ is the same as a no ask at 93¢, with
    identical contract sizes.  Each side shows price levels with their corresponding quantities and
    order counts, organized from best to worst prices.

    Args:
        ticker (str): Market ticker - unique identifier for the specific market
        depth (Union[Unset, int]): Maximum number of price levels to return per side (yes bids/no
            bids). Defaults to all levels. Maximum value is 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetMarketOrderbookResponse
    """

    return (
        await asyncio_detailed(
            ticker=ticker,
            client=client,
            depth=depth,
        )
    ).parsed
