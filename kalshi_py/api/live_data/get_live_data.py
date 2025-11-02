from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_live_data_response import GetLiveDataResponse
from ...types import Response


def _get_kwargs(
    type_: str,
    milestone_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/live_data/{type_}/milestone/{milestone_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetLiveDataResponse]]:
    if response.status_code == 200:
        response_200 = GetLiveDataResponse.from_dict(response.json())

        return response_200
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
) -> Response[Union[Any, GetLiveDataResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_: str,
    milestone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetLiveDataResponse]]:
    """Get Live Data

     Get live data for a specific milestone

    Args:
        type_ (str):
        milestone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetLiveDataResponse]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        milestone_id=milestone_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type_: str,
    milestone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetLiveDataResponse]]:
    """Get Live Data

     Get live data for a specific milestone

    Args:
        type_ (str):
        milestone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetLiveDataResponse]
    """

    return sync_detailed(
        type_=type_,
        milestone_id=milestone_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    type_: str,
    milestone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetLiveDataResponse]]:
    """Get Live Data

     Get live data for a specific milestone

    Args:
        type_ (str):
        milestone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetLiveDataResponse]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        milestone_id=milestone_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_: str,
    milestone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetLiveDataResponse]]:
    """Get Live Data

     Get live data for a specific milestone

    Args:
        type_ (str):
        milestone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetLiveDataResponse]
    """

    return (
        await asyncio_detailed(
            type_=type_,
            milestone_id=milestone_id,
            client=client,
        )
    ).parsed
