from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_quotes_response import GetQuotesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 500,
    market_ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    quote_creator_user_id: Union[Unset, str] = UNSET,
    rfq_creator_user_id: Union[Unset, str] = UNSET,
    rfq_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    params["market_ticker"] = market_ticker

    params["event_ticker"] = event_ticker

    params["status"] = status

    params["quote_creator_user_id"] = quote_creator_user_id

    params["rfq_creator_user_id"] = rfq_creator_user_id

    params["rfq_id"] = rfq_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/communications/quotes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetQuotesResponse]]:
    if response.status_code == 200:
        response_200 = GetQuotesResponse.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetQuotesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 500,
    market_ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    quote_creator_user_id: Union[Unset, str] = UNSET,
    rfq_creator_user_id: Union[Unset, str] = UNSET,
    rfq_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetQuotesResponse]]:
    """Get Quotes

      Endpoint for getting quotes

    Args:
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 500.
        market_ticker (Union[Unset, str]):
        event_ticker (Union[Unset, str]):
        status (Union[Unset, str]):
        quote_creator_user_id (Union[Unset, str]):
        rfq_creator_user_id (Union[Unset, str]):
        rfq_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetQuotesResponse]]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        market_ticker=market_ticker,
        event_ticker=event_ticker,
        status=status,
        quote_creator_user_id=quote_creator_user_id,
        rfq_creator_user_id=rfq_creator_user_id,
        rfq_id=rfq_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 500,
    market_ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    quote_creator_user_id: Union[Unset, str] = UNSET,
    rfq_creator_user_id: Union[Unset, str] = UNSET,
    rfq_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetQuotesResponse]]:
    """Get Quotes

      Endpoint for getting quotes

    Args:
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 500.
        market_ticker (Union[Unset, str]):
        event_ticker (Union[Unset, str]):
        status (Union[Unset, str]):
        quote_creator_user_id (Union[Unset, str]):
        rfq_creator_user_id (Union[Unset, str]):
        rfq_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetQuotesResponse]
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        limit=limit,
        market_ticker=market_ticker,
        event_ticker=event_ticker,
        status=status,
        quote_creator_user_id=quote_creator_user_id,
        rfq_creator_user_id=rfq_creator_user_id,
        rfq_id=rfq_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 500,
    market_ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    quote_creator_user_id: Union[Unset, str] = UNSET,
    rfq_creator_user_id: Union[Unset, str] = UNSET,
    rfq_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetQuotesResponse]]:
    """Get Quotes

      Endpoint for getting quotes

    Args:
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 500.
        market_ticker (Union[Unset, str]):
        event_ticker (Union[Unset, str]):
        status (Union[Unset, str]):
        quote_creator_user_id (Union[Unset, str]):
        rfq_creator_user_id (Union[Unset, str]):
        rfq_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetQuotesResponse]]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        market_ticker=market_ticker,
        event_ticker=event_ticker,
        status=status,
        quote_creator_user_id=quote_creator_user_id,
        rfq_creator_user_id=rfq_creator_user_id,
        rfq_id=rfq_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 500,
    market_ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    quote_creator_user_id: Union[Unset, str] = UNSET,
    rfq_creator_user_id: Union[Unset, str] = UNSET,
    rfq_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetQuotesResponse]]:
    """Get Quotes

      Endpoint for getting quotes

    Args:
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 500.
        market_ticker (Union[Unset, str]):
        event_ticker (Union[Unset, str]):
        status (Union[Unset, str]):
        quote_creator_user_id (Union[Unset, str]):
        rfq_creator_user_id (Union[Unset, str]):
        rfq_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetQuotesResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            limit=limit,
            market_ticker=market_ticker,
            event_ticker=event_ticker,
            status=status,
            quote_creator_user_id=quote_creator_user_id,
            rfq_creator_user_id=rfq_creator_user_id,
            rfq_id=rfq_id,
        )
    ).parsed
