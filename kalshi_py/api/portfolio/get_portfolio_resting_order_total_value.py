from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_get_user_resting_order_total_value_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelGetUserRestingOrderTotalValueResponse,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/portfolio/summary/total_resting_order_value",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetUserRestingOrderTotalValueResponse]:
    if response.status_code == 200:
        response_200 = GithubComKalshiExchangeInfraSvcApi2ModelGetUserRestingOrderTotalValueResponse.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetUserRestingOrderTotalValueResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetUserRestingOrderTotalValueResponse]:
    """Get Portfolio Resting Order Total Value

      Endpoint for getting the total value, in cents, of resting orders. This endpoint is only intended
    for use by FCM members (rare). Note: If you're uncertain about this endpoint, it likely does not
    apply to you.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetUserRestingOrderTotalValueResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetUserRestingOrderTotalValueResponse]:
    """Get Portfolio Resting Order Total Value

      Endpoint for getting the total value, in cents, of resting orders. This endpoint is only intended
    for use by FCM members (rare). Note: If you're uncertain about this endpoint, it likely does not
    apply to you.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetUserRestingOrderTotalValueResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetUserRestingOrderTotalValueResponse]:
    """Get Portfolio Resting Order Total Value

      Endpoint for getting the total value, in cents, of resting orders. This endpoint is only intended
    for use by FCM members (rare). Note: If you're uncertain about this endpoint, it likely does not
    apply to you.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetUserRestingOrderTotalValueResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetUserRestingOrderTotalValueResponse]:
    """Get Portfolio Resting Order Total Value

      Endpoint for getting the total value, in cents, of resting orders. This endpoint is only intended
    for use by FCM members (rare). Note: If you're uncertain about this endpoint, it likely does not
    apply to you.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetUserRestingOrderTotalValueResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
