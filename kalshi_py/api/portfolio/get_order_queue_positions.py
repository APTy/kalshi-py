from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_get_order_queue_positions_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelGetOrderQueuePositionsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    market_tickers: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["market_tickers"] = market_tickers

    params["event_ticker"] = event_ticker

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/portfolio/orders/queue_positions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetOrderQueuePositionsResponse]:
    if response.status_code == 200:
        response_200 = GithubComKalshiExchangeInfraSvcApi2ModelGetOrderQueuePositionsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetOrderQueuePositionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    market_tickers: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetOrderQueuePositionsResponse]:
    """Get Queue Positions for Orders

      Endpoint for getting queue positions for all resting orders. Queue position represents the number
    of contracts that need to be matched before an order receives a partial or full match, determined
    using price-time priority.

    Args:
        market_tickers (Union[Unset, str]): Comma-separated list of market tickers to filter by
        event_ticker (Union[Unset, str]): Event ticker to filter by

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetOrderQueuePositionsResponse]
    """

    kwargs = _get_kwargs(
        market_tickers=market_tickers,
        event_ticker=event_ticker,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    market_tickers: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetOrderQueuePositionsResponse]:
    """Get Queue Positions for Orders

      Endpoint for getting queue positions for all resting orders. Queue position represents the number
    of contracts that need to be matched before an order receives a partial or full match, determined
    using price-time priority.

    Args:
        market_tickers (Union[Unset, str]): Comma-separated list of market tickers to filter by
        event_ticker (Union[Unset, str]): Event ticker to filter by

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetOrderQueuePositionsResponse
    """

    return sync_detailed(
        client=client,
        market_tickers=market_tickers,
        event_ticker=event_ticker,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    market_tickers: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetOrderQueuePositionsResponse]:
    """Get Queue Positions for Orders

      Endpoint for getting queue positions for all resting orders. Queue position represents the number
    of contracts that need to be matched before an order receives a partial or full match, determined
    using price-time priority.

    Args:
        market_tickers (Union[Unset, str]): Comma-separated list of market tickers to filter by
        event_ticker (Union[Unset, str]): Event ticker to filter by

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetOrderQueuePositionsResponse]
    """

    kwargs = _get_kwargs(
        market_tickers=market_tickers,
        event_ticker=event_ticker,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    market_tickers: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetOrderQueuePositionsResponse]:
    """Get Queue Positions for Orders

      Endpoint for getting queue positions for all resting orders. Queue position represents the number
    of contracts that need to be matched before an order receives a partial or full match, determined
    using price-time priority.

    Args:
        market_tickers (Union[Unset, str]): Comma-separated list of market tickers to filter by
        event_ticker (Union[Unset, str]): Event ticker to filter by

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetOrderQueuePositionsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            market_tickers=market_tickers,
            event_ticker=event_ticker,
        )
    ).parsed
