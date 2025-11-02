from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_user_data_timestamp_response import GetUserDataTimestampResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/exchange/user_data_timestamp",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetUserDataTimestampResponse]]:
    if response.status_code == 200:
        response_200 = GetUserDataTimestampResponse.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetUserDataTimestampResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetUserDataTimestampResponse]]:
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
        Response[Union[Any, GetUserDataTimestampResponse]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetUserDataTimestampResponse]]:
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
        Union[Any, GetUserDataTimestampResponse]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetUserDataTimestampResponse]]:
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
        Response[Union[Any, GetUserDataTimestampResponse]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetUserDataTimestampResponse]]:
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
        Union[Any, GetUserDataTimestampResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
