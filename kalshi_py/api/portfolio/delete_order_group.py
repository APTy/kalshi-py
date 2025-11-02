from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.empty_response import EmptyResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    order_group_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/portfolio/order_groups/{order_group_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[EmptyResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = EmptyResponse.from_dict(response.json())

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
) -> Response[Union[EmptyResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    order_group_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[EmptyResponse, ErrorResponse]]:
    """Delete Order Group

      Deletes an order group and cancels all orders within it. This permanently removes the group.

    Args:
        order_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EmptyResponse, ErrorResponse]]
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
    client: AuthenticatedClient,
) -> Optional[Union[EmptyResponse, ErrorResponse]]:
    """Delete Order Group

      Deletes an order group and cancels all orders within it. This permanently removes the group.

    Args:
        order_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EmptyResponse, ErrorResponse]
    """

    return sync_detailed(
        order_group_id=order_group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    order_group_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[EmptyResponse, ErrorResponse]]:
    """Delete Order Group

      Deletes an order group and cancels all orders within it. This permanently removes the group.

    Args:
        order_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EmptyResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        order_group_id=order_group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_group_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[EmptyResponse, ErrorResponse]]:
    """Delete Order Group

      Deletes an order group and cancels all orders within it. This permanently removes the group.

    Args:
        order_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EmptyResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            order_group_id=order_group_id,
            client=client,
        )
    ).parsed
