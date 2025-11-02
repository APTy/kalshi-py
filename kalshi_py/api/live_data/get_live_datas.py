from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_live_datas_response import GetLiveDatasResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    milestone_ids: list[str],
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_milestone_ids = milestone_ids

    params["milestone_ids"] = json_milestone_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/live_data/batch",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetLiveDatasResponse]]:
    if response.status_code == 200:
        response_200 = GetLiveDatasResponse.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetLiveDatasResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    milestone_ids: list[str],
) -> Response[Union[Any, GetLiveDatasResponse]]:
    """Get Multiple Live Data

     Get live data for multiple milestones

    Args:
        milestone_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetLiveDatasResponse]]
    """

    kwargs = _get_kwargs(
        milestone_ids=milestone_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    milestone_ids: list[str],
) -> Optional[Union[Any, GetLiveDatasResponse]]:
    """Get Multiple Live Data

     Get live data for multiple milestones

    Args:
        milestone_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetLiveDatasResponse]
    """

    return sync_detailed(
        client=client,
        milestone_ids=milestone_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    milestone_ids: list[str],
) -> Response[Union[Any, GetLiveDatasResponse]]:
    """Get Multiple Live Data

     Get live data for multiple milestones

    Args:
        milestone_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetLiveDatasResponse]]
    """

    kwargs = _get_kwargs(
        milestone_ids=milestone_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    milestone_ids: list[str],
) -> Optional[Union[Any, GetLiveDatasResponse]]:
    """Get Multiple Live Data

     Get live data for multiple milestones

    Args:
        milestone_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetLiveDatasResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            milestone_ids=milestone_ids,
        )
    ).parsed
