from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ticker: str,
    *,
    depth: Union[Unset, int] = 0,
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


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ErrorResponse]:
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ticker: str,
    *,
    client: AuthenticatedClient,
    depth: Union[Unset, int] = 0,
) -> Response[ErrorResponse]:
    """Get Market Orderbook

      Endpoint for getting the current order book for a specific market.  The order book shows all active
    bid orders for both yes and no sides of a binary market. It returns yes bids and no bids only (no
    asks are returned). This is because in binary markets, a bid for yes at price X is equivalent to an
    ask for no at price (100-X). For example, a yes bid at 7¢ is the same as a no ask at 93¢, with
    identical contract sizes.  Each side shows price levels with their corresponding quantities and
    order counts, organized from best to worst prices.

    Args:
        ticker (str):
        depth (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
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
    client: AuthenticatedClient,
    depth: Union[Unset, int] = 0,
) -> Optional[ErrorResponse]:
    """Get Market Orderbook

      Endpoint for getting the current order book for a specific market.  The order book shows all active
    bid orders for both yes and no sides of a binary market. It returns yes bids and no bids only (no
    asks are returned). This is because in binary markets, a bid for yes at price X is equivalent to an
    ask for no at price (100-X). For example, a yes bid at 7¢ is the same as a no ask at 93¢, with
    identical contract sizes.  Each side shows price levels with their corresponding quantities and
    order counts, organized from best to worst prices.

    Args:
        ticker (str):
        depth (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return sync_detailed(
        ticker=ticker,
        client=client,
        depth=depth,
    ).parsed


async def asyncio_detailed(
    ticker: str,
    *,
    client: AuthenticatedClient,
    depth: Union[Unset, int] = 0,
) -> Response[ErrorResponse]:
    """Get Market Orderbook

      Endpoint for getting the current order book for a specific market.  The order book shows all active
    bid orders for both yes and no sides of a binary market. It returns yes bids and no bids only (no
    asks are returned). This is because in binary markets, a bid for yes at price X is equivalent to an
    ask for no at price (100-X). For example, a yes bid at 7¢ is the same as a no ask at 93¢, with
    identical contract sizes.  Each side shows price levels with their corresponding quantities and
    order counts, organized from best to worst prices.

    Args:
        ticker (str):
        depth (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
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
    client: AuthenticatedClient,
    depth: Union[Unset, int] = 0,
) -> Optional[ErrorResponse]:
    """Get Market Orderbook

      Endpoint for getting the current order book for a specific market.  The order book shows all active
    bid orders for both yes and no sides of a binary market. It returns yes bids and no bids only (no
    asks are returned). This is because in binary markets, a bid for yes at price X is equivalent to an
    ask for no at price (100-X). For example, a yes bid at 7¢ is the same as a no ask at 93¢, with
    identical contract sizes.  Each side shows price levels with their corresponding quantities and
    order counts, organized from best to worst prices.

    Args:
        ticker (str):
        depth (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return (
        await asyncio_detailed(
            ticker=ticker,
            client=client,
            depth=depth,
        )
    ).parsed
