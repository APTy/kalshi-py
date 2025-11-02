from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.accept_quote_request import AcceptQuoteRequest
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    quote_id: str,
    *,
    body: AcceptQuoteRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/communications/quotes/{quote_id}/accept",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
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
) -> Response[Union[Any, ErrorResponse]]:
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
    body: AcceptQuoteRequest,
) -> Response[Union[Any, ErrorResponse]]:
    """Accept Quote

      Endpoint for accepting a quote. This will require the quoter to confirm

    Args:
        quote_id (str):
        body (AcceptQuoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        quote_id=quote_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    quote_id: str,
    *,
    client: AuthenticatedClient,
    body: AcceptQuoteRequest,
) -> Optional[Union[Any, ErrorResponse]]:
    """Accept Quote

      Endpoint for accepting a quote. This will require the quoter to confirm

    Args:
        quote_id (str):
        body (AcceptQuoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return sync_detailed(
        quote_id=quote_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    quote_id: str,
    *,
    client: AuthenticatedClient,
    body: AcceptQuoteRequest,
) -> Response[Union[Any, ErrorResponse]]:
    """Accept Quote

      Endpoint for accepting a quote. This will require the quoter to confirm

    Args:
        quote_id (str):
        body (AcceptQuoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        quote_id=quote_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    quote_id: str,
    *,
    client: AuthenticatedClient,
    body: AcceptQuoteRequest,
) -> Optional[Union[Any, ErrorResponse]]:
    """Accept Quote

      Endpoint for accepting a quote. This will require the quoter to confirm

    Args:
        quote_id (str):
        body (AcceptQuoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            quote_id=quote_id,
            client=client,
            body=body,
        )
    ).parsed
