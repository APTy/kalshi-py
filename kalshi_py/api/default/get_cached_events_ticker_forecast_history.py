from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_common_api_json_error import (
    GithubComKalshiExchangeInfraCommonApiJSONError,
)
from ...models.model_get_event_forecast_percentiles_history_response import (
    ModelGetEventForecastPercentilesHistoryResponse,
)
from ...types import Response


def _get_kwargs(
    ticker: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/cached/events/{ticker}/forecast_history",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetEventForecastPercentilesHistoryResponse]]:
    if response.status_code == 200:
        response_200 = ModelGetEventForecastPercentilesHistoryResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = GithubComKalshiExchangeInfraCommonApiJSONError.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = GithubComKalshiExchangeInfraCommonApiJSONError.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = GithubComKalshiExchangeInfraCommonApiJSONError.from_dict(response.json())

        return response_403
    if response.status_code == 500:
        response_500 = GithubComKalshiExchangeInfraCommonApiJSONError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetEventForecastPercentilesHistoryResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetEventForecastPercentilesHistoryResponse]]:
    """End-point for getting the historical raw and formatted forecast numbers for an event. See the
    response body for full information on what is returned. Data is cached and so is slightly lagged.

    Args:
        ticker (str): Ticker

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetEventForecastPercentilesHistoryResponse]]
    """

    kwargs = _get_kwargs(
        ticker=ticker,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetEventForecastPercentilesHistoryResponse]]:
    """End-point for getting the historical raw and formatted forecast numbers for an event. See the
    response body for full information on what is returned. Data is cached and so is slightly lagged.

    Args:
        ticker (str): Ticker

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetEventForecastPercentilesHistoryResponse]
    """

    return sync_detailed(
        ticker=ticker,
        client=client,
    ).parsed


async def asyncio_detailed(
    ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetEventForecastPercentilesHistoryResponse]]:
    """End-point for getting the historical raw and formatted forecast numbers for an event. See the
    response body for full information on what is returned. Data is cached and so is slightly lagged.

    Args:
        ticker (str): Ticker

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetEventForecastPercentilesHistoryResponse]]
    """

    kwargs = _get_kwargs(
        ticker=ticker,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetEventForecastPercentilesHistoryResponse]]:
    """End-point for getting the historical raw and formatted forecast numbers for an event. See the
    response body for full information on what is returned. Data is cached and so is slightly lagged.

    Args:
        ticker (str): Ticker

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetEventForecastPercentilesHistoryResponse]
    """

    return (
        await asyncio_detailed(
            ticker=ticker,
            client=client,
        )
    ).parsed
