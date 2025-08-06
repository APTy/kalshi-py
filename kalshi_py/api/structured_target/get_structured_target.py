from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.model_get_structured_target_response import ModelGetStructuredTargetResponse
from ...types import Response


def _get_kwargs(
    structured_target_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/structured_targets/{structured_target_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ModelGetStructuredTargetResponse]:
    if response.status_code == 200:
        response_200 = ModelGetStructuredTargetResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ModelGetStructuredTargetResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    structured_target_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ModelGetStructuredTargetResponse]:
    """Get Structured Target

      Endpoint for getting data about a specific structured target by its ID.

    Args:
        structured_target_id (str): Structured Target ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelGetStructuredTargetResponse]
    """

    kwargs = _get_kwargs(
        structured_target_id=structured_target_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    structured_target_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ModelGetStructuredTargetResponse]:
    """Get Structured Target

      Endpoint for getting data about a specific structured target by its ID.

    Args:
        structured_target_id (str): Structured Target ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelGetStructuredTargetResponse
    """

    return sync_detailed(
        structured_target_id=structured_target_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    structured_target_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ModelGetStructuredTargetResponse]:
    """Get Structured Target

      Endpoint for getting data about a specific structured target by its ID.

    Args:
        structured_target_id (str): Structured Target ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelGetStructuredTargetResponse]
    """

    kwargs = _get_kwargs(
        structured_target_id=structured_target_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    structured_target_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ModelGetStructuredTargetResponse]:
    """Get Structured Target

      Endpoint for getting data about a specific structured target by its ID.

    Args:
        structured_target_id (str): Structured Target ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelGetStructuredTargetResponse
    """

    return (
        await asyncio_detailed(
            structured_target_id=structured_target_id,
            client=client,
        )
    ).parsed
