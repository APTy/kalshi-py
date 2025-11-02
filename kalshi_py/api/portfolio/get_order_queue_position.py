from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_order_queue_position_response import GetOrderQueuePositionResponse
from ...types import Response


def _get_kwargs(
    order_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/portfolio/orders/{order_id}/queue_position",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetOrderQueuePositionResponse]]:
    if response.status_code == 200:
        response_200 = GetOrderQueuePositionResponse.from_dict(response.json())

        return response_200
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
) -> Response[Union[ErrorResponse, GetOrderQueuePositionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    order_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, GetOrderQueuePositionResponse]]:
    """Get Order Queue Position

      Endpoint for getting an order's queue position in the order book. This represents the amount of
    orders that need to be matched before this order receives a partial or full match. Queue position is
    determined using a price-time priority.

    Args:
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetOrderQueuePositionResponse]]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, GetOrderQueuePositionResponse]]:
    """Get Order Queue Position

      Endpoint for getting an order's queue position in the order book. This represents the amount of
    orders that need to be matched before this order receives a partial or full match. Queue position is
    determined using a price-time priority.

    Args:
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetOrderQueuePositionResponse]
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    order_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, GetOrderQueuePositionResponse]]:
    """Get Order Queue Position

      Endpoint for getting an order's queue position in the order book. This represents the amount of
    orders that need to be matched before this order receives a partial or full match. Queue position is
    determined using a price-time priority.

    Args:
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetOrderQueuePositionResponse]]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, GetOrderQueuePositionResponse]]:
    """Get Order Queue Position

      Endpoint for getting an order's queue position in the order book. This represents the amount of
    orders that need to be matched before this order receives a partial or full match. Queue position is
    determined using a price-time priority.

    Args:
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetOrderQueuePositionResponse]
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
        )
    ).parsed
