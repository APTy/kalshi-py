from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_common_api_json_error import (
    GithubComKalshiExchangeInfraCommonApiJSONError,
)
from ...models.model_get_series_fee_changes_response import ModelGetSeriesFeeChangesResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/series/fee_changes",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetSeriesFeeChangesResponse]]:
    if response.status_code == 200:
        response_200 = ModelGetSeriesFeeChangesResponse.from_dict(response.json())

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
    if response.status_code == 404:
        response_404 = GithubComKalshiExchangeInfraCommonApiJSONError.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = GithubComKalshiExchangeInfraCommonApiJSONError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetSeriesFeeChangesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetSeriesFeeChangesResponse]]:
    """End-point for getting data about all upcoming series fee changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetSeriesFeeChangesResponse]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetSeriesFeeChangesResponse]]:
    """End-point for getting data about all upcoming series fee changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetSeriesFeeChangesResponse]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetSeriesFeeChangesResponse]]:
    """End-point for getting data about all upcoming series fee changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetSeriesFeeChangesResponse]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetSeriesFeeChangesResponse]]:
    """End-point for getting data about all upcoming series fee changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GithubComKalshiExchangeInfraCommonApiJSONError, ModelGetSeriesFeeChangesResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
