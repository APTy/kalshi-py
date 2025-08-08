#!/usr/bin/env python3

from kalshi_py import Client
from kalshi_py.api.market import get_markets


def test_sync_client():
    """Test synchronous client functionality."""
    client = Client(base_url="https://api.elections.kalshi.com/trade-api/v2")

    response = get_markets.sync(client=client, limit=3)

    assert response is not None
    assert response.markets is not None
    assert len(response.markets) > 0


def test_async_client():
    """Test asynchronous client functionality."""
    import asyncio

    async def _test_async():
        client = Client(base_url="https://api.elections.kalshi.com/trade-api/v2")

        response = await get_markets.asyncio(client=client, limit=3)

        assert response is not None
        assert response.markets is not None
        assert len(response.markets) > 0

    asyncio.run(_test_async())
