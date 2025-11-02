from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_milestone_response import GetMilestoneResponse
from ...types import Response


def _get_kwargs(
    milestone_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/milestones/{milestone_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetMilestoneResponse]]:
    if response.status_code == 200:
        response_200 = GetMilestoneResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetMilestoneResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    milestone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetMilestoneResponse]]:
    """Get Milestone

      Endpoint for getting data about a specific milestone by its ID.

    Args:
        milestone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetMilestoneResponse]]
    """

    kwargs = _get_kwargs(
        milestone_id=milestone_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    milestone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetMilestoneResponse]]:
    """Get Milestone

      Endpoint for getting data about a specific milestone by its ID.

    Args:
        milestone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetMilestoneResponse]
    """

    return sync_detailed(
        milestone_id=milestone_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    milestone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetMilestoneResponse]]:
    """Get Milestone

      Endpoint for getting data about a specific milestone by its ID.

    Args:
        milestone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetMilestoneResponse]]
    """

    kwargs = _get_kwargs(
        milestone_id=milestone_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    milestone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetMilestoneResponse]]:
    """Get Milestone

      Endpoint for getting data about a specific milestone by its ID.

    Args:
        milestone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetMilestoneResponse]
    """

    return (
        await asyncio_detailed(
            milestone_id=milestone_id,
            client=client,
        )
    ).parsed
