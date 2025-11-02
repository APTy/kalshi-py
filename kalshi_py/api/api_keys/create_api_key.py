from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_api_key_request import CreateApiKeyRequest
from ...models.create_api_key_response import CreateApiKeyResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateApiKeyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api_keys",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateApiKeyResponse]]:
    if response.status_code == 201:
        response_201 = CreateApiKeyResponse.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, CreateApiKeyResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateApiKeyRequest,
) -> Response[Union[Any, CreateApiKeyResponse]]:
    """Create API Key

      Endpoint for creating a new API key with a user-provided public key.  This endpoint allows users
    with Premier or Market Maker API usage levels to create API keys by providing their own RSA public
    key. The platform will use this public key to verify signatures on API requests.

    Args:
        body (CreateApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateApiKeyResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateApiKeyRequest,
) -> Optional[Union[Any, CreateApiKeyResponse]]:
    """Create API Key

      Endpoint for creating a new API key with a user-provided public key.  This endpoint allows users
    with Premier or Market Maker API usage levels to create API keys by providing their own RSA public
    key. The platform will use this public key to verify signatures on API requests.

    Args:
        body (CreateApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateApiKeyResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateApiKeyRequest,
) -> Response[Union[Any, CreateApiKeyResponse]]:
    """Create API Key

      Endpoint for creating a new API key with a user-provided public key.  This endpoint allows users
    with Premier or Market Maker API usage levels to create API keys by providing their own RSA public
    key. The platform will use this public key to verify signatures on API requests.

    Args:
        body (CreateApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateApiKeyResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateApiKeyRequest,
) -> Optional[Union[Any, CreateApiKeyResponse]]:
    """Create API Key

      Endpoint for creating a new API key with a user-provided public key.  This endpoint allows users
    with Premier or Market Maker API usage levels to create API keys by providing their own RSA public
    key. The platform will use this public key to verify signatures on API requests.

    Args:
        body (CreateApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateApiKeyResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
