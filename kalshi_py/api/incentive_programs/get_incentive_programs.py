from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.controllers_webcontroller_error_response import ControllersWebcontrollerErrorResponse
from ...models.model_get_incentive_programs_response import ModelGetIncentiveProgramsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/incentive_programs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ControllersWebcontrollerErrorResponse, ModelGetIncentiveProgramsResponse]]:
    if response.status_code == 200:
        response_200 = ModelGetIncentiveProgramsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ControllersWebcontrollerErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 500:
        response_500 = ControllersWebcontrollerErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ControllersWebcontrollerErrorResponse, ModelGetIncentiveProgramsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[ControllersWebcontrollerErrorResponse, ModelGetIncentiveProgramsResponse]]:
    """Get Incentives

      List volume incentives with optional filters. Volume incentives are rewards programs for trading
    activity on specific markets.

    Args:
        limit (Union[Unset, int]): Number of results per page. Defaults to 100. Maximum value is
            10000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ControllersWebcontrollerErrorResponse, ModelGetIncentiveProgramsResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[ControllersWebcontrollerErrorResponse, ModelGetIncentiveProgramsResponse]]:
    """Get Incentives

      List volume incentives with optional filters. Volume incentives are rewards programs for trading
    activity on specific markets.

    Args:
        limit (Union[Unset, int]): Number of results per page. Defaults to 100. Maximum value is
            10000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ControllersWebcontrollerErrorResponse, ModelGetIncentiveProgramsResponse]
    """

    return sync_detailed(
        client=client,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[ControllersWebcontrollerErrorResponse, ModelGetIncentiveProgramsResponse]]:
    """Get Incentives

      List volume incentives with optional filters. Volume incentives are rewards programs for trading
    activity on specific markets.

    Args:
        limit (Union[Unset, int]): Number of results per page. Defaults to 100. Maximum value is
            10000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ControllersWebcontrollerErrorResponse, ModelGetIncentiveProgramsResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[ControllersWebcontrollerErrorResponse, ModelGetIncentiveProgramsResponse]]:
    """Get Incentives

      List volume incentives with optional filters. Volume incentives are rewards programs for trading
    activity on specific markets.

    Args:
        limit (Union[Unset, int]): Number of results per page. Defaults to 100. Maximum value is
            10000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ControllersWebcontrollerErrorResponse, ModelGetIncentiveProgramsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
        )
    ).parsed
