from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_quote_response import GetQuoteResponse
from ...types import Response


def _get_kwargs(
    quote_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/communications/quotes/{quote_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetQuoteResponse]]:
    if response.status_code == 200:
        response_200 = GetQuoteResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetQuoteResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    quote_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, GetQuoteResponse]]:
    """Get Quote

      Endpoint for getting a particular quote

    Args:
        quote_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetQuoteResponse]]
    """

    kwargs = _get_kwargs(
        quote_id=quote_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    quote_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, GetQuoteResponse]]:
    """Get Quote

      Endpoint for getting a particular quote

    Args:
        quote_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetQuoteResponse]
    """

    return sync_detailed(
        quote_id=quote_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    quote_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, GetQuoteResponse]]:
    """Get Quote

      Endpoint for getting a particular quote

    Args:
        quote_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetQuoteResponse]]
    """

    kwargs = _get_kwargs(
        quote_id=quote_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    quote_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, GetQuoteResponse]]:
    """Get Quote

      Endpoint for getting a particular quote

    Args:
        quote_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetQuoteResponse]
    """

    return (
        await asyncio_detailed(
            quote_id=quote_id,
            client=client,
        )
    ).parsed
