from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_batch_cancel_orders_request import (
    GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersRequest,
)
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_batch_cancel_orders_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersResponse,
)
from ...types import Response


def _get_kwargs(
    *,
    body: GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/portfolio/orders/batched",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersResponse]:
    if response.status_code == 200:
        response_200 = GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersRequest,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersResponse]:
    """Batch Cancel Orders

      Endpoint for cancelling up to 20 orders at once. Available to members with advanced access only.

    Args:
        body (GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersRequest,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersResponse]:
    """Batch Cancel Orders

      Endpoint for cancelling up to 20 orders at once. Available to members with advanced access only.

    Args:
        body (GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersRequest,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersResponse]:
    """Batch Cancel Orders

      Endpoint for cancelling up to 20 orders at once. Available to members with advanced access only.

    Args:
        body (GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersRequest,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersResponse]:
    """Batch Cancel Orders

      Endpoint for cancelling up to 20 orders at once. Available to members with advanced access only.

    Args:
        body (GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelBatchCancelOrdersResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
