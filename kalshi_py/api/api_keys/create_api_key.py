from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.model_user_create_api_key_request import ModelUserCreateApiKeyRequest
from ...models.model_user_create_api_key_response import ModelUserCreateApiKeyResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ModelUserCreateApiKeyRequest,
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
) -> Optional[ModelUserCreateApiKeyResponse]:
    if response.status_code == 201:
        response_201 = ModelUserCreateApiKeyResponse.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ModelUserCreateApiKeyResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ModelUserCreateApiKeyRequest,
) -> Response[ModelUserCreateApiKeyResponse]:
    """Create API Key

      Endpoint for creating a new API key with a user-provided public key.  This endpoint allows users
    with Premier or Market Maker API usage levels to create API keys by providing their own RSA public
    key. The platform will use this public key to verify signatures on API requests.

    Args:
        body (ModelUserCreateApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelUserCreateApiKeyResponse]
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
    client: Union[AuthenticatedClient, Client],
    body: ModelUserCreateApiKeyRequest,
) -> Optional[ModelUserCreateApiKeyResponse]:
    """Create API Key

      Endpoint for creating a new API key with a user-provided public key.  This endpoint allows users
    with Premier or Market Maker API usage levels to create API keys by providing their own RSA public
    key. The platform will use this public key to verify signatures on API requests.

    Args:
        body (ModelUserCreateApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelUserCreateApiKeyResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ModelUserCreateApiKeyRequest,
) -> Response[ModelUserCreateApiKeyResponse]:
    """Create API Key

      Endpoint for creating a new API key with a user-provided public key.  This endpoint allows users
    with Premier or Market Maker API usage levels to create API keys by providing their own RSA public
    key. The platform will use this public key to verify signatures on API requests.

    Args:
        body (ModelUserCreateApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelUserCreateApiKeyResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ModelUserCreateApiKeyRequest,
) -> Optional[ModelUserCreateApiKeyResponse]:
    """Create API Key

      Endpoint for creating a new API key with a user-provided public key.  This endpoint allows users
    with Premier or Market Maker API usage levels to create API keys by providing their own RSA public
    key. The platform will use this public key to verify signatures on API requests.

    Args:
        body (ModelUserCreateApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelUserCreateApiKeyResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
