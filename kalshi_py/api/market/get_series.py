from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_series_response import GetSeriesResponse
from ...types import Response


def _get_kwargs(
    series_ticker: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/series/{series_ticker}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetSeriesResponse]]:
    if response.status_code == 200:
        response_200 = GetSeriesResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetSeriesResponse]]:
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
) -> Response[Union[ErrorResponse, GetSeriesResponse]]:
    r"""Get Series

      Endpoint for getting data about a specific series by its ticker.  A series represents a template
    for recurring events that follow the same format and rules (e.g., \"Monthly Jobs Report\", \"Weekly
    Initial Jobless Claims\", \"Daily Weather in NYC\"). Series define the structure, settlement
    sources, and metadata that will be applied to each recurring event instance within that series.

    Args:
        series_ticker (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetSeriesResponse]]
    """

    kwargs = _get_kwargs(
        series_ticker=series_ticker,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    series_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetSeriesResponse]]:
    r"""Get Series

      Endpoint for getting data about a specific series by its ticker.  A series represents a template
    for recurring events that follow the same format and rules (e.g., \"Monthly Jobs Report\", \"Weekly
    Initial Jobless Claims\", \"Daily Weather in NYC\"). Series define the structure, settlement
    sources, and metadata that will be applied to each recurring event instance within that series.

    Args:
        series_ticker (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetSeriesResponse]
    """

    return sync_detailed(
        series_ticker=series_ticker,
        client=client,
    ).parsed


async def asyncio_detailed(
    series_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetSeriesResponse]]:
    r"""Get Series

      Endpoint for getting data about a specific series by its ticker.  A series represents a template
    for recurring events that follow the same format and rules (e.g., \"Monthly Jobs Report\", \"Weekly
    Initial Jobless Claims\", \"Daily Weather in NYC\"). Series define the structure, settlement
    sources, and metadata that will be applied to each recurring event instance within that series.

    Args:
        series_ticker (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetSeriesResponse]]
    """

    kwargs = _get_kwargs(
        series_ticker=series_ticker,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    series_ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetSeriesResponse]]:
    r"""Get Series

      Endpoint for getting data about a specific series by its ticker.  A series represents a template
    for recurring events that follow the same format and rules (e.g., \"Monthly Jobs Report\", \"Weekly
    Initial Jobless Claims\", \"Daily Weather in NYC\"). Series define the structure, settlement
    sources, and metadata that will be applied to each recurring event instance within that series.

    Args:
        series_ticker (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetSeriesResponse]
    """

    return (
        await asyncio_detailed(
            series_ticker=series_ticker,
            client=client,
        )
    ).parsed
