from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch_create_orders_request import BatchCreateOrdersRequest
from ...models.batch_create_orders_response import BatchCreateOrdersResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: BatchCreateOrdersRequest,
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
) -> Optional[Union[BatchCreateOrdersResponse, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = BatchCreateOrdersResponse.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BatchCreateOrdersResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BatchCreateOrdersRequest,
) -> Response[Union[BatchCreateOrdersResponse, ErrorResponse]]:
    """Batch Create Orders

      Endpoint for submitting a batch of orders. Each order in the batch is counted against the total
    rate limit for order operations. Consequently, the size of the batch is capped by the current per-
    second rate-limit configuration applicable to the user. At the moment of writing, the limit is 20
    orders per batch. Available to members with advanced access only.

    Args:
        body (BatchCreateOrdersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BatchCreateOrdersResponse, ErrorResponse]]
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
    client: AuthenticatedClient,
    body: BatchCreateOrdersRequest,
) -> Optional[Union[BatchCreateOrdersResponse, ErrorResponse]]:
    """Batch Create Orders

      Endpoint for submitting a batch of orders. Each order in the batch is counted against the total
    rate limit for order operations. Consequently, the size of the batch is capped by the current per-
    second rate-limit configuration applicable to the user. At the moment of writing, the limit is 20
    orders per batch. Available to members with advanced access only.

    Args:
        body (BatchCreateOrdersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BatchCreateOrdersResponse, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BatchCreateOrdersRequest,
) -> Response[Union[BatchCreateOrdersResponse, ErrorResponse]]:
    """Batch Create Orders

      Endpoint for submitting a batch of orders. Each order in the batch is counted against the total
    rate limit for order operations. Consequently, the size of the batch is capped by the current per-
    second rate-limit configuration applicable to the user. At the moment of writing, the limit is 20
    orders per batch. Available to members with advanced access only.

    Args:
        body (BatchCreateOrdersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BatchCreateOrdersResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BatchCreateOrdersRequest,
) -> Optional[Union[BatchCreateOrdersResponse, ErrorResponse]]:
    """Batch Create Orders

      Endpoint for submitting a batch of orders. Each order in the batch is counted against the total
    rate limit for order operations. Consequently, the size of the batch is capped by the current per-
    second rate-limit configuration applicable to the user. At the moment of writing, the limit is 20
    orders per batch. Available to members with advanced access only.

    Args:
        body (BatchCreateOrdersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BatchCreateOrdersResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
