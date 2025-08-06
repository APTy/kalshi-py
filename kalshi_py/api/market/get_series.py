from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    series_ticker: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/series/{series_ticker}",
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
    series_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    r"""Get Series

      Endpoint for getting data about a specific series by its ticker.  A series represents a template
    for recurring events that follow the same format and rules (e.g., \"Monthly Jobs Report\", \"Weekly
    Initial Jobless Claims\", \"Daily Weather in NYC\"). Series define the structure, settlement
    sources, and metadata that will be applied to each recurring event instance within that series.

    Args:
        series_ticker (str): Series ticker - unique identifier for the specific series

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        series_ticker=series_ticker,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    series_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    r"""Get Series

      Endpoint for getting data about a specific series by its ticker.  A series represents a template
    for recurring events that follow the same format and rules (e.g., \"Monthly Jobs Report\", \"Weekly
    Initial Jobless Claims\", \"Daily Weather in NYC\"). Series define the structure, settlement
    sources, and metadata that will be applied to each recurring event instance within that series.

    Args:
        series_ticker (str): Series ticker - unique identifier for the specific series

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        series_ticker=series_ticker,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
