from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_get_event_metadata_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelGetEventMetadataResponse,
)
from ...types import Response


def _get_kwargs(
    event_ticker: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/events/{event_ticker}/metadata",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetEventMetadataResponse]:
    if response.status_code == 200:
        response_200 = GithubComKalshiExchangeInfraSvcApi2ModelGetEventMetadataResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetEventMetadataResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetEventMetadataResponse]:
    """Get Event Metadata

      Endpoint for getting metadata about an event by its ticker.  Returns only the metadata information
    for an event.

    Args:
        event_ticker (str): Event ticker

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetEventMetadataResponse]
    """

    kwargs = _get_kwargs(
        event_ticker=event_ticker,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetEventMetadataResponse]:
    """Get Event Metadata

      Endpoint for getting metadata about an event by its ticker.  Returns only the metadata information
    for an event.

    Args:
        event_ticker (str): Event ticker

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetEventMetadataResponse
    """

    return sync_detailed(
        event_ticker=event_ticker,
        client=client,
    ).parsed


async def asyncio_detailed(
    event_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetEventMetadataResponse]:
    """Get Event Metadata

      Endpoint for getting metadata about an event by its ticker.  Returns only the metadata information
    for an event.

    Args:
        event_ticker (str): Event ticker

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetEventMetadataResponse]
    """

    kwargs = _get_kwargs(
        event_ticker=event_ticker,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetEventMetadataResponse]:
    """Get Event Metadata

      Endpoint for getting metadata about an event by its ticker.  Returns only the metadata information
    for an event.

    Args:
        event_ticker (str): Event ticker

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetEventMetadataResponse
    """

    return (
        await asyncio_detailed(
            event_ticker=event_ticker,
            client=client,
        )
    ).parsed
