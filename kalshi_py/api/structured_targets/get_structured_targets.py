from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_structured_targets_response import GetStructuredTargetsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: Union[Unset, str] = UNSET,
    competition: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["type"] = type_

    params["competition"] = competition

    params["page_size"] = page_size

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/structured_targets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetStructuredTargetsResponse]]:
    if response.status_code == 200:
        response_200 = GetStructuredTargetsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetStructuredTargetsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, str] = UNSET,
    competition: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetStructuredTargetsResponse]]:
    """Get Structured Targets

     Page size (min: 1, max: 2000)

    Args:
        type_ (Union[Unset, str]):
        competition (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetStructuredTargetsResponse]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        competition=competition,
        page_size=page_size,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, str] = UNSET,
    competition: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetStructuredTargetsResponse]]:
    """Get Structured Targets

     Page size (min: 1, max: 2000)

    Args:
        type_ (Union[Unset, str]):
        competition (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetStructuredTargetsResponse]
    """

    return sync_detailed(
        client=client,
        type_=type_,
        competition=competition,
        page_size=page_size,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, str] = UNSET,
    competition: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetStructuredTargetsResponse]]:
    """Get Structured Targets

     Page size (min: 1, max: 2000)

    Args:
        type_ (Union[Unset, str]):
        competition (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetStructuredTargetsResponse]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        competition=competition,
        page_size=page_size,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, str] = UNSET,
    competition: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetStructuredTargetsResponse]]:
    """Get Structured Targets

     Page size (min: 1, max: 2000)

    Args:
        type_ (Union[Unset, str]):
        competition (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetStructuredTargetsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            competition=competition,
            page_size=page_size,
            cursor=cursor,
        )
    ).parsed
