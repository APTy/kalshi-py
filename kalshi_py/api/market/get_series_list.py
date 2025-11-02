from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_series_list_response import GetSeriesListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    category: Union[Unset, str] = UNSET,
    tags: Union[Unset, str] = UNSET,
    include_product_metadata: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["category"] = category

    params["tags"] = tags

    params["include_product_metadata"] = include_product_metadata

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/series",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetSeriesListResponse]]:
    if response.status_code == 200:
        response_200 = GetSeriesListResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetSeriesListResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    category: Union[Unset, str] = UNSET,
    tags: Union[Unset, str] = UNSET,
    include_product_metadata: Union[Unset, bool] = False,
) -> Response[Union[ErrorResponse, GetSeriesListResponse]]:
    r"""Get Series List

      Endpoint for getting data about multiple series with specified filters.  A series represents a
    template for recurring events that follow the same format and rules (e.g., \"Monthly Jobs Report\",
    \"Weekly Initial Jobless Claims\", \"Daily Weather in NYC\"). This endpoint allows you to browse and
    discover available series templates by category.

    Args:
        category (Union[Unset, str]):
        tags (Union[Unset, str]):
        include_product_metadata (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetSeriesListResponse]]
    """

    kwargs = _get_kwargs(
        category=category,
        tags=tags,
        include_product_metadata=include_product_metadata,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    category: Union[Unset, str] = UNSET,
    tags: Union[Unset, str] = UNSET,
    include_product_metadata: Union[Unset, bool] = False,
) -> Optional[Union[ErrorResponse, GetSeriesListResponse]]:
    r"""Get Series List

      Endpoint for getting data about multiple series with specified filters.  A series represents a
    template for recurring events that follow the same format and rules (e.g., \"Monthly Jobs Report\",
    \"Weekly Initial Jobless Claims\", \"Daily Weather in NYC\"). This endpoint allows you to browse and
    discover available series templates by category.

    Args:
        category (Union[Unset, str]):
        tags (Union[Unset, str]):
        include_product_metadata (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetSeriesListResponse]
    """

    return sync_detailed(
        client=client,
        category=category,
        tags=tags,
        include_product_metadata=include_product_metadata,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    category: Union[Unset, str] = UNSET,
    tags: Union[Unset, str] = UNSET,
    include_product_metadata: Union[Unset, bool] = False,
) -> Response[Union[ErrorResponse, GetSeriesListResponse]]:
    r"""Get Series List

      Endpoint for getting data about multiple series with specified filters.  A series represents a
    template for recurring events that follow the same format and rules (e.g., \"Monthly Jobs Report\",
    \"Weekly Initial Jobless Claims\", \"Daily Weather in NYC\"). This endpoint allows you to browse and
    discover available series templates by category.

    Args:
        category (Union[Unset, str]):
        tags (Union[Unset, str]):
        include_product_metadata (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetSeriesListResponse]]
    """

    kwargs = _get_kwargs(
        category=category,
        tags=tags,
        include_product_metadata=include_product_metadata,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    category: Union[Unset, str] = UNSET,
    tags: Union[Unset, str] = UNSET,
    include_product_metadata: Union[Unset, bool] = False,
) -> Optional[Union[ErrorResponse, GetSeriesListResponse]]:
    r"""Get Series List

      Endpoint for getting data about multiple series with specified filters.  A series represents a
    template for recurring events that follow the same format and rules (e.g., \"Monthly Jobs Report\",
    \"Weekly Initial Jobless Claims\", \"Daily Weather in NYC\"). This endpoint allows you to browse and
    discover available series templates by category.

    Args:
        category (Union[Unset, str]):
        tags (Union[Unset, str]):
        include_product_metadata (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetSeriesListResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            category=category,
            tags=tags,
            include_product_metadata=include_product_metadata,
        )
    ).parsed
