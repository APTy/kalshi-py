from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_event_metadata_response import GetEventMetadataResponse
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
) -> Optional[Union[Any, GetEventMetadataResponse]]:
    if response.status_code == 200:
        response_200 = GetEventMetadataResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
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
) -> Response[Union[Any, GetEventMetadataResponse]]:
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
) -> Response[Union[Any, GetEventMetadataResponse]]:
    """Get Event Metadata

      Endpoint for getting metadata about an event by its ticker.  Returns only the metadata information
    for an event.

    Args:
        event_ticker (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetEventMetadataResponse]]
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
) -> Optional[Union[Any, GetEventMetadataResponse]]:
    """Get Event Metadata

      Endpoint for getting metadata about an event by its ticker.  Returns only the metadata information
    for an event.

    Args:
        event_ticker (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetEventMetadataResponse]
    """

    return sync_detailed(
        event_ticker=event_ticker,
        client=client,
    ).parsed


async def asyncio_detailed(
    event_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetEventMetadataResponse]]:
    """Get Event Metadata

      Endpoint for getting metadata about an event by its ticker.  Returns only the metadata information
    for an event.

    Args:
        event_ticker (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetEventMetadataResponse]]
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
) -> Optional[Union[Any, GetEventMetadataResponse]]:
    """Get Event Metadata

      Endpoint for getting metadata about an event by its ticker.  Returns only the metadata information
    for an event.

    Args:
        event_ticker (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetEventMetadataResponse]
    """

    return (
        await asyncio_detailed(
            event_ticker=event_ticker,
            client=client,
        )
    ).parsed
