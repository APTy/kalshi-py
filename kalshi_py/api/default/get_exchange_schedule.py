from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.svc_api_2_model_get_exchange_schedule_response import SvcApi2ModelGetExchangeScheduleResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/exchange/schedule",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SvcApi2ModelGetExchangeScheduleResponse]:
    if response.status_code == 200:
        response_200 = SvcApi2ModelGetExchangeScheduleResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SvcApi2ModelGetExchangeScheduleResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[SvcApi2ModelGetExchangeScheduleResponse]:
    """Get Exchange Schedule

      Endpoint for getting the exchange schedule.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SvcApi2ModelGetExchangeScheduleResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[SvcApi2ModelGetExchangeScheduleResponse]:
    """Get Exchange Schedule

      Endpoint for getting the exchange schedule.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SvcApi2ModelGetExchangeScheduleResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[SvcApi2ModelGetExchangeScheduleResponse]:
    """Get Exchange Schedule

      Endpoint for getting the exchange schedule.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SvcApi2ModelGetExchangeScheduleResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[SvcApi2ModelGetExchangeScheduleResponse]:
    """Get Exchange Schedule

      Endpoint for getting the exchange schedule.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SvcApi2ModelGetExchangeScheduleResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
