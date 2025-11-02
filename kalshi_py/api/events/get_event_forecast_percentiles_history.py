from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_event_forecast_percentiles_history_period_interval import (
    GetEventForecastPercentilesHistoryPeriodInterval,
)
from ...models.get_event_forecast_percentiles_history_response import GetEventForecastPercentilesHistoryResponse
from ...types import UNSET, Response


def _get_kwargs(
    series_ticker: str,
    ticker: str,
    *,
    percentiles: list[int],
    start_ts: int,
    end_ts: int,
    period_interval: GetEventForecastPercentilesHistoryPeriodInterval,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_percentiles = percentiles

    params["percentiles"] = json_percentiles

    params["start_ts"] = start_ts

    params["end_ts"] = end_ts

    json_period_interval = period_interval.value
    params["period_interval"] = json_period_interval

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/series/{series_ticker}/events/{ticker}/forecast_percentile_history",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetEventForecastPercentilesHistoryResponse]]:
    if response.status_code == 200:
        response_200 = GetEventForecastPercentilesHistoryResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetEventForecastPercentilesHistoryResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    series_ticker: str,
    ticker: str,
    *,
    client: AuthenticatedClient,
    percentiles: list[int],
    start_ts: int,
    end_ts: int,
    period_interval: GetEventForecastPercentilesHistoryPeriodInterval,
) -> Response[Union[Any, GetEventForecastPercentilesHistoryResponse]]:
    """Get Event Forecast Percentile History

     Endpoint for getting the historical raw and formatted forecast numbers for an event at specific
    percentiles.

    Args:
        series_ticker (str):
        ticker (str):
        percentiles (list[int]):
        start_ts (int):
        end_ts (int):
        period_interval (GetEventForecastPercentilesHistoryPeriodInterval):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetEventForecastPercentilesHistoryResponse]]
    """

    kwargs = _get_kwargs(
        series_ticker=series_ticker,
        ticker=ticker,
        percentiles=percentiles,
        start_ts=start_ts,
        end_ts=end_ts,
        period_interval=period_interval,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    series_ticker: str,
    ticker: str,
    *,
    client: AuthenticatedClient,
    percentiles: list[int],
    start_ts: int,
    end_ts: int,
    period_interval: GetEventForecastPercentilesHistoryPeriodInterval,
) -> Optional[Union[Any, GetEventForecastPercentilesHistoryResponse]]:
    """Get Event Forecast Percentile History

     Endpoint for getting the historical raw and formatted forecast numbers for an event at specific
    percentiles.

    Args:
        series_ticker (str):
        ticker (str):
        percentiles (list[int]):
        start_ts (int):
        end_ts (int):
        period_interval (GetEventForecastPercentilesHistoryPeriodInterval):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetEventForecastPercentilesHistoryResponse]
    """

    return sync_detailed(
        series_ticker=series_ticker,
        ticker=ticker,
        client=client,
        percentiles=percentiles,
        start_ts=start_ts,
        end_ts=end_ts,
        period_interval=period_interval,
    ).parsed


async def asyncio_detailed(
    series_ticker: str,
    ticker: str,
    *,
    client: AuthenticatedClient,
    percentiles: list[int],
    start_ts: int,
    end_ts: int,
    period_interval: GetEventForecastPercentilesHistoryPeriodInterval,
) -> Response[Union[Any, GetEventForecastPercentilesHistoryResponse]]:
    """Get Event Forecast Percentile History

     Endpoint for getting the historical raw and formatted forecast numbers for an event at specific
    percentiles.

    Args:
        series_ticker (str):
        ticker (str):
        percentiles (list[int]):
        start_ts (int):
        end_ts (int):
        period_interval (GetEventForecastPercentilesHistoryPeriodInterval):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetEventForecastPercentilesHistoryResponse]]
    """

    kwargs = _get_kwargs(
        series_ticker=series_ticker,
        ticker=ticker,
        percentiles=percentiles,
        start_ts=start_ts,
        end_ts=end_ts,
        period_interval=period_interval,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    series_ticker: str,
    ticker: str,
    *,
    client: AuthenticatedClient,
    percentiles: list[int],
    start_ts: int,
    end_ts: int,
    period_interval: GetEventForecastPercentilesHistoryPeriodInterval,
) -> Optional[Union[Any, GetEventForecastPercentilesHistoryResponse]]:
    """Get Event Forecast Percentile History

     Endpoint for getting the historical raw and formatted forecast numbers for an event at specific
    percentiles.

    Args:
        series_ticker (str):
        ticker (str):
        percentiles (list[int]):
        start_ts (int):
        end_ts (int):
        period_interval (GetEventForecastPercentilesHistoryPeriodInterval):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetEventForecastPercentilesHistoryResponse]
    """

    return (
        await asyncio_detailed(
            series_ticker=series_ticker,
            ticker=ticker,
            client=client,
            percentiles=percentiles,
            start_ts=start_ts,
            end_ts=end_ts,
            period_interval=period_interval,
        )
    ).parsed
