from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_user_generate_api_key_request import (
    GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyRequest,
)
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_user_generate_api_key_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyResponse,
)
from ...types import Response


def _get_kwargs(
    *,
    body: GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api_keys/generate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyResponse]:
    if response.status_code == 201:
        response_201 = GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyResponse.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyRequest,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyResponse]:
    """Generate API Key

      Endpoint for generating a new API key with an automatically created key pair.  This endpoint
    generates both a public and private RSA key pair. The public key is stored on the platform, while
    the private key is returned to the user and must be stored securely. The private key cannot be
    retrieved again.

    Args:
        body (GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyResponse]
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
    body: GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyRequest,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyResponse]:
    """Generate API Key

      Endpoint for generating a new API key with an automatically created key pair.  This endpoint
    generates both a public and private RSA key pair. The public key is stored on the platform, while
    the private key is returned to the user and must be stored securely. The private key cannot be
    retrieved again.

    Args:
        body (GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyRequest,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyResponse]:
    """Generate API Key

      Endpoint for generating a new API key with an automatically created key pair.  This endpoint
    generates both a public and private RSA key pair. The public key is stored on the platform, while
    the private key is returned to the user and must be stored securely. The private key cannot be
    retrieved again.

    Args:
        body (GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyRequest,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyResponse]:
    """Generate API Key

      Endpoint for generating a new API key with an automatically created key pair.  This endpoint
    generates both a public and private RSA key pair. The public key is stored on the platform, while
    the private key is returned to the user and must be stored securely. The private key cannot be
    retrieved again.

    Args:
        body (GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelUserGenerateApiKeyResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
