from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_positions_response import GetPositionsResponse
from ...models.get_positions_settlement_status import GetPositionsSettlementStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    count_filter: Union[Unset, str] = UNSET,
    settlement_status: Union[Unset, GetPositionsSettlementStatus] = GetPositionsSettlementStatus.UNSETTLED,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    params["count_filter"] = count_filter

    json_settlement_status: Union[Unset, str] = UNSET
    if not isinstance(settlement_status, Unset):
        json_settlement_status = settlement_status.value

    params["settlement_status"] = json_settlement_status

    params["ticker"] = ticker

    params["event_ticker"] = event_ticker

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/portfolio/positions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetPositionsResponse]]:
    if response.status_code == 200:
        response_200 = GetPositionsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
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
) -> Response[Union[ErrorResponse, GetPositionsResponse]]:
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
    limit: Union[Unset, int] = 100,
    count_filter: Union[Unset, str] = UNSET,
    settlement_status: Union[Unset, GetPositionsSettlementStatus] = GetPositionsSettlementStatus.UNSETTLED,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetPositionsResponse]]:
    """Get Positions

     Restricts the positions to those with any of following fields with non-zero values, as a comma
    separated list. The following values are accepted: position, total_traded, resting_order_count

    Args:
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.
        count_filter (Union[Unset, str]):
        settlement_status (Union[Unset, GetPositionsSettlementStatus]):  Default:
            GetPositionsSettlementStatus.UNSETTLED.
        ticker (Union[Unset, str]):
        event_ticker (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetPositionsResponse]]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        count_filter=count_filter,
        settlement_status=settlement_status,
        ticker=ticker,
        event_ticker=event_ticker,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    count_filter: Union[Unset, str] = UNSET,
    settlement_status: Union[Unset, GetPositionsSettlementStatus] = GetPositionsSettlementStatus.UNSETTLED,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetPositionsResponse]]:
    """Get Positions

     Restricts the positions to those with any of following fields with non-zero values, as a comma
    separated list. The following values are accepted: position, total_traded, resting_order_count

    Args:
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.
        count_filter (Union[Unset, str]):
        settlement_status (Union[Unset, GetPositionsSettlementStatus]):  Default:
            GetPositionsSettlementStatus.UNSETTLED.
        ticker (Union[Unset, str]):
        event_ticker (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetPositionsResponse]
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        limit=limit,
        count_filter=count_filter,
        settlement_status=settlement_status,
        ticker=ticker,
        event_ticker=event_ticker,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    count_filter: Union[Unset, str] = UNSET,
    settlement_status: Union[Unset, GetPositionsSettlementStatus] = GetPositionsSettlementStatus.UNSETTLED,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetPositionsResponse]]:
    """Get Positions

     Restricts the positions to those with any of following fields with non-zero values, as a comma
    separated list. The following values are accepted: position, total_traded, resting_order_count

    Args:
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.
        count_filter (Union[Unset, str]):
        settlement_status (Union[Unset, GetPositionsSettlementStatus]):  Default:
            GetPositionsSettlementStatus.UNSETTLED.
        ticker (Union[Unset, str]):
        event_ticker (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetPositionsResponse]]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        count_filter=count_filter,
        settlement_status=settlement_status,
        ticker=ticker,
        event_ticker=event_ticker,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    count_filter: Union[Unset, str] = UNSET,
    settlement_status: Union[Unset, GetPositionsSettlementStatus] = GetPositionsSettlementStatus.UNSETTLED,
    ticker: Union[Unset, str] = UNSET,
    event_ticker: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetPositionsResponse]]:
    """Get Positions

     Restricts the positions to those with any of following fields with non-zero values, as a comma
    separated list. The following values are accepted: position, total_traded, resting_order_count

    Args:
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.
        count_filter (Union[Unset, str]):
        settlement_status (Union[Unset, GetPositionsSettlementStatus]):  Default:
            GetPositionsSettlementStatus.UNSETTLED.
        ticker (Union[Unset, str]):
        event_ticker (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetPositionsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            limit=limit,
            count_filter=count_filter,
            settlement_status=settlement_status,
            ticker=ticker,
            event_ticker=event_ticker,
        )
    ).parsed
