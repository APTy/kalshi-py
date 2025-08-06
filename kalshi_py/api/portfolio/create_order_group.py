from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_create_order_group_request import (
    GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupRequest,
)
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_create_order_group_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupResponse,
)
from ...types import Response


def _get_kwargs(
    *,
    body: GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/portfolio/order_groups/create",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupResponse]:
    if response.status_code == 201:
        response_201 = GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupResponse.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupRequest,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupResponse]:
    """Create Order Group

      Creates a new order group with a contracts limit. When the limit is hit, all orders in the group
    are cancelled and no new orders can be placed until reset.

    Args:
        body (GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupResponse]
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
    body: GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupRequest,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupResponse]:
    """Create Order Group

      Creates a new order group with a contracts limit. When the limit is hit, all orders in the group
    are cancelled and no new orders can be placed until reset.

    Args:
        body (GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupRequest,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupResponse]:
    """Create Order Group

      Creates a new order group with a contracts limit. When the limit is hit, all orders in the group
    are cancelled and no new orders can be placed until reset.

    Args:
        body (GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupRequest,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupResponse]:
    """Create Order Group

      Creates a new order group with a contracts limit. When the limit is hit, all orders in the group
    are cancelled and no new orders can be placed until reset.

    Args:
        body (GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderGroupResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
