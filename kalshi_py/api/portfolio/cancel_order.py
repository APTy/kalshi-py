from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_cancel_order_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelCancelOrderResponse,
)
from ...types import Response


def _get_kwargs(
    order_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/portfolio/orders/{order_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelCancelOrderResponse]:
    if response.status_code == 200:
        response_200 = GithubComKalshiExchangeInfraSvcApi2ModelCancelOrderResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelCancelOrderResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelCancelOrderResponse]:
    """Cancel Order

      Endpoint for canceling orders. The value for the orderId should match the id field of the order you
    want to decrease. Commonly, DELETE-type endpoints return 204 status with no body content on success.
    But we can't completely delete the order, as it may be partially filled already. Instead, the
    DeleteOrder endpoint reduce the order completely, essentially zeroing the remaining resting
    contracts on it. The zeroed order is returned on the response payload as a form of validation for
    the client.

    Args:
        order_id (str): Order ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelCancelOrderResponse]
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
    client: Union[AuthenticatedClient, Client],
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelCancelOrderResponse]:
    """Cancel Order

      Endpoint for canceling orders. The value for the orderId should match the id field of the order you
    want to decrease. Commonly, DELETE-type endpoints return 204 status with no body content on success.
    But we can't completely delete the order, as it may be partially filled already. Instead, the
    DeleteOrder endpoint reduce the order completely, essentially zeroing the remaining resting
    contracts on it. The zeroed order is returned on the response payload as a form of validation for
    the client.

    Args:
        order_id (str): Order ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelCancelOrderResponse
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelCancelOrderResponse]:
    """Cancel Order

      Endpoint for canceling orders. The value for the orderId should match the id field of the order you
    want to decrease. Commonly, DELETE-type endpoints return 204 status with no body content on success.
    But we can't completely delete the order, as it may be partially filled already. Instead, the
    DeleteOrder endpoint reduce the order completely, essentially zeroing the remaining resting
    contracts on it. The zeroed order is returned on the response payload as a form of validation for
    the client.

    Args:
        order_id (str): Order ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelCancelOrderResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelCancelOrderResponse]:
    """Cancel Order

      Endpoint for canceling orders. The value for the orderId should match the id field of the order you
    want to decrease. Commonly, DELETE-type endpoints return 204 status with no body content on success.
    But we can't completely delete the order, as it may be partially filled already. Instead, the
    DeleteOrder endpoint reduce the order completely, essentially zeroing the remaining resting
    contracts on it. The zeroed order is returned on the response payload as a form of validation for
    the client.

    Args:
        order_id (str): Order ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelCancelOrderResponse
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
        )
    ).parsed
