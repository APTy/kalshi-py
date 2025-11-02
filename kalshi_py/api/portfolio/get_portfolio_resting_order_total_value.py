from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_portfolio_resting_order_total_value_response import GetPortfolioRestingOrderTotalValueResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/portfolio/summary/total_resting_order_value",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetPortfolioRestingOrderTotalValueResponse]]:
    if response.status_code == 200:
        response_200 = GetPortfolioRestingOrderTotalValueResponse.from_dict(response.json())

        return response_200
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
) -> Response[Union[ErrorResponse, GetPortfolioRestingOrderTotalValueResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, GetPortfolioRestingOrderTotalValueResponse]]:
    """Get Total Resting Order Value

      Endpoint for getting the total value, in cents, of resting orders. This endpoint is only intended
    for use by FCM members (rare). Note: If you're uncertain about this endpoint, it likely does not
    apply to you.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetPortfolioRestingOrderTotalValueResponse]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, GetPortfolioRestingOrderTotalValueResponse]]:
    """Get Total Resting Order Value

      Endpoint for getting the total value, in cents, of resting orders. This endpoint is only intended
    for use by FCM members (rare). Note: If you're uncertain about this endpoint, it likely does not
    apply to you.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetPortfolioRestingOrderTotalValueResponse]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, GetPortfolioRestingOrderTotalValueResponse]]:
    """Get Total Resting Order Value

      Endpoint for getting the total value, in cents, of resting orders. This endpoint is only intended
    for use by FCM members (rare). Note: If you're uncertain about this endpoint, it likely does not
    apply to you.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetPortfolioRestingOrderTotalValueResponse]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, GetPortfolioRestingOrderTotalValueResponse]]:
    """Get Total Resting Order Value

      Endpoint for getting the total value, in cents, of resting orders. This endpoint is only intended
    for use by FCM members (rare). Note: If you're uncertain about this endpoint, it likely does not
    apply to you.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetPortfolioRestingOrderTotalValueResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
