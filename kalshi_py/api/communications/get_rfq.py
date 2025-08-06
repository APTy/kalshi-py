from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.model_get_rfq_response import ModelGetRFQResponse
from ...types import Response


def _get_kwargs(
    rfq_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/communications/rfqs/{rfq_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ModelGetRFQResponse]:
    if response.status_code == 200:
        response_200 = ModelGetRFQResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ModelGetRFQResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rfq_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ModelGetRFQResponse]:
    """Get RFQ

      Endpoint for getting a single RFQ by id

    Args:
        rfq_id (str): RFQ ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelGetRFQResponse]
    """

    kwargs = _get_kwargs(
        rfq_id=rfq_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    rfq_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ModelGetRFQResponse]:
    """Get RFQ

      Endpoint for getting a single RFQ by id

    Args:
        rfq_id (str): RFQ ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelGetRFQResponse
    """

    return sync_detailed(
        rfq_id=rfq_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    rfq_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ModelGetRFQResponse]:
    """Get RFQ

      Endpoint for getting a single RFQ by id

    Args:
        rfq_id (str): RFQ ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelGetRFQResponse]
    """

    kwargs = _get_kwargs(
        rfq_id=rfq_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    rfq_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ModelGetRFQResponse]:
    """Get RFQ

      Endpoint for getting a single RFQ by id

    Args:
        rfq_id (str): RFQ ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelGetRFQResponse
    """

    return (
        await asyncio_detailed(
            rfq_id=rfq_id,
            client=client,
        )
    ).parsed
