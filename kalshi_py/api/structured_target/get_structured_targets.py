from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_get_structured_targets_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelGetStructuredTargetsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: Union[Unset, str] = UNSET,
    competition: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
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
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetStructuredTargetsResponse]:
    if response.status_code == 200:
        response_200 = GithubComKalshiExchangeInfraSvcApi2ModelGetStructuredTargetsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetStructuredTargetsResponse]:
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
    page_size: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetStructuredTargetsResponse]:
    """Get Structured Targets

      Endpoint for getting data about structured targets.

    Args:
        type_ (Union[Unset, str]): Type of structured target
        competition (Union[Unset, str]): Competition filter
        page_size (Union[Unset, int]): Page size (min: 1, max: 2000)
        cursor (Union[Unset, str]): Pagination cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetStructuredTargetsResponse]
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
    page_size: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetStructuredTargetsResponse]:
    """Get Structured Targets

      Endpoint for getting data about structured targets.

    Args:
        type_ (Union[Unset, str]): Type of structured target
        competition (Union[Unset, str]): Competition filter
        page_size (Union[Unset, int]): Page size (min: 1, max: 2000)
        cursor (Union[Unset, str]): Pagination cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetStructuredTargetsResponse
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
    page_size: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetStructuredTargetsResponse]:
    """Get Structured Targets

      Endpoint for getting data about structured targets.

    Args:
        type_ (Union[Unset, str]): Type of structured target
        competition (Union[Unset, str]): Competition filter
        page_size (Union[Unset, int]): Page size (min: 1, max: 2000)
        cursor (Union[Unset, str]): Pagination cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetStructuredTargetsResponse]
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
    page_size: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetStructuredTargetsResponse]:
    """Get Structured Targets

      Endpoint for getting data about structured targets.

    Args:
        type_ (Union[Unset, str]): Type of structured target
        competition (Union[Unset, str]): Competition filter
        page_size (Union[Unset, int]): Page size (min: 1, max: 2000)
        cursor (Union[Unset, str]): Pagination cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetStructuredTargetsResponse
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
