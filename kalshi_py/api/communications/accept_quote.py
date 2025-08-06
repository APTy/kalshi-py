from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_accept_quote_request import (
    GithubComKalshiExchangeInfraSvcApi2ModelAcceptQuoteRequest,
)
from ...types import Response


def _get_kwargs(
    quote_id: str,
    *,
    body: GithubComKalshiExchangeInfraSvcApi2ModelAcceptQuoteRequest,
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


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 204:
        return None
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
    quote_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: GithubComKalshiExchangeInfraSvcApi2ModelAcceptQuoteRequest,
) -> Response[Any]:
    """Accept Quote

      Endpoint for accepting a quote. This will require the quoter to confirm

    Args:
        quote_id (str): Quote ID
        body (GithubComKalshiExchangeInfraSvcApi2ModelAcceptQuoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        quote_id=quote_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    quote_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: GithubComKalshiExchangeInfraSvcApi2ModelAcceptQuoteRequest,
) -> Response[Any]:
    """Accept Quote

      Endpoint for accepting a quote. This will require the quoter to confirm

    Args:
        quote_id (str): Quote ID
        body (GithubComKalshiExchangeInfraSvcApi2ModelAcceptQuoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        quote_id=quote_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
