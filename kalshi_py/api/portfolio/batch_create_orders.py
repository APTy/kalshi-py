from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_batch_create_orders_request import (
    GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersRequest,
)
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_batch_create_orders_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersResponse,
)
from ...types import Response


def _get_kwargs(
    *,
    body: GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/portfolio/orders/batched",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersResponse]:
    if response.status_code == 201:
        response_201 = GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersResponse.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersRequest,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersResponse]:
    """Batch Create Orders

      Endpoint for submitting a batch of orders. Each order in the batch is counted against the total
    rate limit for order operations. Consequently, the size of the batch is capped by the current per-
    second rate-limit configuration applicable to the user. At the moment of writing, the limit is 20
    orders per batch. Available to members with advanced access only.

    Args:
        body (GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersResponse]
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
    body: GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersRequest,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersResponse]:
    """Batch Create Orders

      Endpoint for submitting a batch of orders. Each order in the batch is counted against the total
    rate limit for order operations. Consequently, the size of the batch is capped by the current per-
    second rate-limit configuration applicable to the user. At the moment of writing, the limit is 20
    orders per batch. Available to members with advanced access only.

    Args:
        body (GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersRequest,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersResponse]:
    """Batch Create Orders

      Endpoint for submitting a batch of orders. Each order in the batch is counted against the total
    rate limit for order operations. Consequently, the size of the batch is capped by the current per-
    second rate-limit configuration applicable to the user. At the moment of writing, the limit is 20
    orders per batch. Available to members with advanced access only.

    Args:
        body (GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersRequest,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersResponse]:
    """Batch Create Orders

      Endpoint for submitting a batch of orders. Each order in the batch is counted against the total
    rate limit for order operations. Consequently, the size of the batch is capped by the current per-
    second rate-limit configuration applicable to the user. At the moment of writing, the limit is 20
    orders per batch. Available to members with advanced access only.

    Args:
        body (GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelBatchCreateOrdersResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
