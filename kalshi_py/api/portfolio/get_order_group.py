from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.model_get_order_group_response import ModelGetOrderGroupResponse
from ...types import Response


def _get_kwargs(
    order_group_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/portfolio/order_groups/{order_group_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ModelGetOrderGroupResponse]:
    if response.status_code == 200:
        response_200 = ModelGetOrderGroupResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ModelGetOrderGroupResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    order_group_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ModelGetOrderGroupResponse]:
    """Get Order Group

      Retrieves details for a single order group including all order IDs and auto-cancel status.

    Args:
        order_group_id (str): Order group ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelGetOrderGroupResponse]
    """

    kwargs = _get_kwargs(
        order_group_id=order_group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_group_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ModelGetOrderGroupResponse]:
    """Get Order Group

      Retrieves details for a single order group including all order IDs and auto-cancel status.

    Args:
        order_group_id (str): Order group ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelGetOrderGroupResponse
    """

    return sync_detailed(
        order_group_id=order_group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    order_group_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ModelGetOrderGroupResponse]:
    """Get Order Group

      Retrieves details for a single order group including all order IDs and auto-cancel status.

    Args:
        order_group_id (str): Order group ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelGetOrderGroupResponse]
    """

    kwargs = _get_kwargs(
        order_group_id=order_group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_group_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ModelGetOrderGroupResponse]:
    """Get Order Group

      Retrieves details for a single order group including all order IDs and auto-cancel status.

    Args:
        order_group_id (str): Order group ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelGetOrderGroupResponse
    """

    return (
        await asyncio_detailed(
            order_group_id=order_group_id,
            client=client,
        )
    ).parsed
