from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_kalshi_exchange_infra_svc_api_2_model_get_fills_response import (
    GithubComKalshiExchangeInfraSvcApi2ModelGetFillsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ticker: Union[Unset, str] = UNSET,
    order_id: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    use_dollars: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ticker"] = ticker

    params["order_id"] = order_id

    params["min_ts"] = min_ts

    params["max_ts"] = max_ts

    params["limit"] = limit

    params["cursor"] = cursor

    params["use_dollars"] = use_dollars

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/portfolio/fills",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetFillsResponse]:
    if response.status_code == 200:
        response_200 = GithubComKalshiExchangeInfraSvcApi2ModelGetFillsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetFillsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ticker: Union[Unset, str] = UNSET,
    order_id: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    use_dollars: Union[Unset, bool] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetFillsResponse]:
    """Get Fills

      Endpoint for getting all fills for the member. A fill is when a trade you have is matched.

    Args:
        ticker (Union[Unset, str]): Restricts the response to trades in a specific market.
        order_id (Union[Unset, str]): Restricts the response to trades related to a specific
            order.
        min_ts (Union[Unset, int]): Restricts the response to trades after a timestamp.
        max_ts (Union[Unset, int]): Restricts the response to trades before a timestamp.
        limit (Union[Unset, int]): Parameter to specify the number of results per page. Defaults
            to 100.
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in
            the pagination. Use the value returned from the previous response to get the next page.
        use_dollars (Union[Unset, bool]): Whether to return prices in centi-cent format (0.0001)
            instead of cent format (0.01).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetFillsResponse]
    """

    kwargs = _get_kwargs(
        ticker=ticker,
        order_id=order_id,
        min_ts=min_ts,
        max_ts=max_ts,
        limit=limit,
        cursor=cursor,
        use_dollars=use_dollars,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    ticker: Union[Unset, str] = UNSET,
    order_id: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    use_dollars: Union[Unset, bool] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetFillsResponse]:
    """Get Fills

      Endpoint for getting all fills for the member. A fill is when a trade you have is matched.

    Args:
        ticker (Union[Unset, str]): Restricts the response to trades in a specific market.
        order_id (Union[Unset, str]): Restricts the response to trades related to a specific
            order.
        min_ts (Union[Unset, int]): Restricts the response to trades after a timestamp.
        max_ts (Union[Unset, int]): Restricts the response to trades before a timestamp.
        limit (Union[Unset, int]): Parameter to specify the number of results per page. Defaults
            to 100.
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in
            the pagination. Use the value returned from the previous response to get the next page.
        use_dollars (Union[Unset, bool]): Whether to return prices in centi-cent format (0.0001)
            instead of cent format (0.01).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetFillsResponse
    """

    return sync_detailed(
        client=client,
        ticker=ticker,
        order_id=order_id,
        min_ts=min_ts,
        max_ts=max_ts,
        limit=limit,
        cursor=cursor,
        use_dollars=use_dollars,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ticker: Union[Unset, str] = UNSET,
    order_id: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    use_dollars: Union[Unset, bool] = UNSET,
) -> Response[GithubComKalshiExchangeInfraSvcApi2ModelGetFillsResponse]:
    """Get Fills

      Endpoint for getting all fills for the member. A fill is when a trade you have is matched.

    Args:
        ticker (Union[Unset, str]): Restricts the response to trades in a specific market.
        order_id (Union[Unset, str]): Restricts the response to trades related to a specific
            order.
        min_ts (Union[Unset, int]): Restricts the response to trades after a timestamp.
        max_ts (Union[Unset, int]): Restricts the response to trades before a timestamp.
        limit (Union[Unset, int]): Parameter to specify the number of results per page. Defaults
            to 100.
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in
            the pagination. Use the value returned from the previous response to get the next page.
        use_dollars (Union[Unset, bool]): Whether to return prices in centi-cent format (0.0001)
            instead of cent format (0.01).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComKalshiExchangeInfraSvcApi2ModelGetFillsResponse]
    """

    kwargs = _get_kwargs(
        ticker=ticker,
        order_id=order_id,
        min_ts=min_ts,
        max_ts=max_ts,
        limit=limit,
        cursor=cursor,
        use_dollars=use_dollars,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    ticker: Union[Unset, str] = UNSET,
    order_id: Union[Unset, str] = UNSET,
    min_ts: Union[Unset, int] = UNSET,
    max_ts: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    use_dollars: Union[Unset, bool] = UNSET,
) -> Optional[GithubComKalshiExchangeInfraSvcApi2ModelGetFillsResponse]:
    """Get Fills

      Endpoint for getting all fills for the member. A fill is when a trade you have is matched.

    Args:
        ticker (Union[Unset, str]): Restricts the response to trades in a specific market.
        order_id (Union[Unset, str]): Restricts the response to trades related to a specific
            order.
        min_ts (Union[Unset, int]): Restricts the response to trades after a timestamp.
        max_ts (Union[Unset, int]): Restricts the response to trades before a timestamp.
        limit (Union[Unset, int]): Parameter to specify the number of results per page. Defaults
            to 100.
        cursor (Union[Unset, str]): The Cursor represents a pointer to the next page of records in
            the pagination. Use the value returned from the previous response to get the next page.
        use_dollars (Union[Unset, bool]): Whether to return prices in centi-cent format (0.0001)
            instead of cent format (0.01).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComKalshiExchangeInfraSvcApi2ModelGetFillsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            ticker=ticker,
            order_id=order_id,
            min_ts=min_ts,
            max_ts=max_ts,
            limit=limit,
            cursor=cursor,
            use_dollars=use_dollars,
        )
    ).parsed
