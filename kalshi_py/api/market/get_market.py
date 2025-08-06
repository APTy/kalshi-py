from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_get_market_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelGetMarketResponse,
)
from ...types import Response


def _get_kwargs(
    ticker: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/markets/{ticker}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketResponse]:
    if response.status_code == 200:
        response_200 = GithubComKalshiExchangeInfraSvcApi2ModelGetMarketResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketResponse]:
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
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketResponse]:
    r"""Get Market

      Endpoint for getting data about a specific market by its ticker. A market represents a specific
    binary outcome within an event that users can trade on (e.g., \"Will candidate X win?\"). Markets
    have yes/no positions, current prices, volume, and settlement rules.

    Args:
        ticker (str): Market ticker - unique identifier for the specific market

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketResponse]
    """

    kwargs = _get_kwargs(
        ticker=ticker,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketResponse]:
    r"""Get Market

      Endpoint for getting data about a specific market by its ticker. A market represents a specific
    binary outcome within an event that users can trade on (e.g., \"Will candidate X win?\"). Markets
    have yes/no positions, current prices, volume, and settlement rules.

    Args:
        ticker (str): Market ticker - unique identifier for the specific market

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetMarketResponse
    """

    return sync_detailed(
        ticker=ticker,
        client=client,
    ).parsed


async def asyncio_detailed(
    ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketResponse]:
    r"""Get Market

      Endpoint for getting data about a specific market by its ticker. A market represents a specific
    binary outcome within an event that users can trade on (e.g., \"Will candidate X win?\"). Markets
    have yes/no positions, current prices, volume, and settlement rules.

    Args:
        ticker (str): Market ticker - unique identifier for the specific market

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketResponse]
    """

    kwargs = _get_kwargs(
        ticker=ticker,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetMarketResponse]:
    r"""Get Market

      Endpoint for getting data about a specific market by its ticker. A market represents a specific
    binary outcome within an event that users can trade on (e.g., \"Will candidate X win?\"). Markets
    have yes/no positions, current prices, volume, and settlement rules.

    Args:
        ticker (str): Market ticker - unique identifier for the specific market

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetMarketResponse
    """

    return (
        await asyncio_detailed(
            ticker=ticker,
            client=client,
        )
    ).parsed
