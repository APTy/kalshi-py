from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.model_get_user_data_timestamp_response import ModelGetUserDataTimestampResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/exchange/user_data_timestamp",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ModelGetUserDataTimestampResponse]:
    if response.status_code == 200:
        response_200 = ModelGetUserDataTimestampResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ModelGetUserDataTimestampResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ModelGetUserDataTimestampResponse]:
    """Get User Data Timestamp

      There is typically a short delay before exchange events are reflected in the API endpoints.
    Whenever possible, combine API responses to PUT/POST/DELETE requests with websocket data to obtain
    the most accurate view of the exchange state. This endpoint provides an approximate indication of
    when the data from the following endpoints was last validated: GetBalance, GetOrder(s), GetFills,
    GetPositions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelGetUserDataTimestampResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ModelGetUserDataTimestampResponse]:
    """Get User Data Timestamp

      There is typically a short delay before exchange events are reflected in the API endpoints.
    Whenever possible, combine API responses to PUT/POST/DELETE requests with websocket data to obtain
    the most accurate view of the exchange state. This endpoint provides an approximate indication of
    when the data from the following endpoints was last validated: GetBalance, GetOrder(s), GetFills,
    GetPositions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelGetUserDataTimestampResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ModelGetUserDataTimestampResponse]:
    """Get User Data Timestamp

      There is typically a short delay before exchange events are reflected in the API endpoints.
    Whenever possible, combine API responses to PUT/POST/DELETE requests with websocket data to obtain
    the most accurate view of the exchange state. This endpoint provides an approximate indication of
    when the data from the following endpoints was last validated: GetBalance, GetOrder(s), GetFills,
    GetPositions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelGetUserDataTimestampResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ModelGetUserDataTimestampResponse]:
    """Get User Data Timestamp

      There is typically a short delay before exchange events are reflected in the API endpoints.
    Whenever possible, combine API responses to PUT/POST/DELETE requests with websocket data to obtain
    the most accurate view of the exchange state. This endpoint provides an approximate indication of
    when the data from the following endpoints was last validated: GetBalance, GetOrder(s), GetFills,
    GetPositions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelGetUserDataTimestampResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
