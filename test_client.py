#!/usr/bin/env python3

import asyncio

from kalshi_py import Client
from kalshi_py.api.market import get_markets


def test_sync_client():
    """Test synchronous client functionality."""
    print("Testing synchronous client...")

    client = Client(base_url="https://api.elections.kalshi.com/trade-api/v2")

    try:
        with client as client:
            response = get_markets.sync(client=client, limit=3)

            if response and response.markets:
                print(f"✓ Successfully fetched {len(response.markets)} markets")
                for market in response.markets:
                    print(f"  - {market.ticker}: {market.title[:50]}...")
                return True
            else:
                print("✗ No markets returned")
                return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


async def test_async_client():
    """Test asynchronous client functionality."""
    print("Testing asynchronous client...")

    client = Client(base_url="https://api.elections.kalshi.com/trade-api/v2")

    try:
        async with client as client:
            response = await get_markets.asyncio(client=client, limit=3)

            if response and response.markets:
                print(f"✓ Successfully fetched {len(response.markets)} markets (async)")
                return True
            else:
                print("✗ No markets returned (async)")
                return False
    except Exception as e:
        print(f"✗ Error (async): {e}")
        return False


def main():
    """Run all tests."""
    print("=== Kalshi Python Client Library Tests ===\n")

    # Test sync client
    sync_success = test_sync_client()
    print()

    # Test async client
    async_success = asyncio.run(test_async_client())
    print()

    # Summary
    print("=== Test Results ===")
    print(f"Synchronous client: {'✓ PASS' if sync_success else '✗ FAIL'}")
    print(f"Asynchronous client: {'✓ PASS' if async_success else '✗ FAIL'}")

    if sync_success and async_success:
        print("\n🎉 All tests passed! The client library is working correctly.")
        return 0
    else:
        print("\n❌ Some tests failed. Please check the errors above.")
        return 1


if __name__ == "__main__":
    exit(main())
