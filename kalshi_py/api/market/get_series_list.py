from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    category: str,
    include_product_metadata: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["category"] = category

    params["include_product_metadata"] = include_product_metadata

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/series",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    category: str,
    include_product_metadata: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    r"""Get Series List

      Endpoint for getting data about multiple series with specified filters.  A series represents a
    template for recurring events that follow the same format and rules (e.g., \"Monthly Jobs Report\",
    \"Weekly Initial Jobless Claims\", \"Daily Weather in NYC\"). This endpoint allows you to browse and
    discover available series templates by category.

    Args:
        category (str): Filter series by category. Returns only series belonging to the specified
            category.
        include_product_metadata (Union[Unset, bool]): Include additional product metadata in the
            response for each series.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        category=category,
        include_product_metadata=include_product_metadata,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    category: str,
    include_product_metadata: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    r"""Get Series List

      Endpoint for getting data about multiple series with specified filters.  A series represents a
    template for recurring events that follow the same format and rules (e.g., \"Monthly Jobs Report\",
    \"Weekly Initial Jobless Claims\", \"Daily Weather in NYC\"). This endpoint allows you to browse and
    discover available series templates by category.

    Args:
        category (str): Filter series by category. Returns only series belonging to the specified
            category.
        include_product_metadata (Union[Unset, bool]): Include additional product metadata in the
            response for each series.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        category=category,
        include_product_metadata=include_product_metadata,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
