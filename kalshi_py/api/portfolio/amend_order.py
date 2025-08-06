from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.model_amend_order_request import ModelAmendOrderRequest
from ...models.model_amend_order_response import ModelAmendOrderResponse
from ...types import Response


def _get_kwargs(
    order_id: str,
    *,
    body: ModelAmendOrderRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/portfolio/orders/{order_id}/amend",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ModelAmendOrderResponse]:
    if response.status_code == 200:
        response_200 = ModelAmendOrderResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ModelAmendOrderResponse]:
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
    body: ModelAmendOrderRequest,
) -> Response[ModelAmendOrderResponse]:
    """Amend Order

      Endpoint for amending the max number of fillable contracts and/or price in an existing order. Max
    fillable contracts is `remaining_count` + `fill_count`.

    Args:
        order_id (str): Order ID
        body (ModelAmendOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelAmendOrderResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ModelAmendOrderRequest,
) -> Optional[ModelAmendOrderResponse]:
    """Amend Order

      Endpoint for amending the max number of fillable contracts and/or price in an existing order. Max
    fillable contracts is `remaining_count` + `fill_count`.

    Args:
        order_id (str): Order ID
        body (ModelAmendOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelAmendOrderResponse
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ModelAmendOrderRequest,
) -> Response[ModelAmendOrderResponse]:
    """Amend Order

      Endpoint for amending the max number of fillable contracts and/or price in an existing order. Max
    fillable contracts is `remaining_count` + `fill_count`.

    Args:
        order_id (str): Order ID
        body (ModelAmendOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelAmendOrderResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ModelAmendOrderRequest,
) -> Optional[ModelAmendOrderResponse]:
    """Amend Order

      Endpoint for amending the max number of fillable contracts and/or price in an existing order. Max
    fillable contracts is `remaining_count` + `fill_count`.

    Args:
        order_id (str): Order ID
        body (ModelAmendOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelAmendOrderResponse
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
            body=body,
        )
    ).parsed
