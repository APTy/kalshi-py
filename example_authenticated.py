#!/usr/bin/env python3

"""
Example usage of the Kalshi authenticated client.

This example demonstrates how to use the Kalshi API with RSA-PSS signature authentication.
You'll need to set up your credentials before running this example.

Environment Variables:
    KALSHI_API_KEY_ID: Your Kalshi access key ID
    KALSHI_PRIVATE_KEY_PATH: Path to your RSA private key file

Or pass them directly to create_client().
"""

import asyncio
import os

from kalshi_py import create_client
from kalshi_py.api.market import get_markets
from kalshi_py.api.portfolio import get_balance, get_positions


def sync_example():
    """Synchronous example using the authenticated client."""
    print("=== Synchronous Authenticated Client Example ===\n")

    try:
        # Create authenticated client
        # This will use environment variables if not provided
        client = create_client()

        with client as client:
            # Get account balance
            print("Fetching account balance...")
            balance = get_balance.sync(client=client)
            print(f"Account balance: ${balance.balance / 100:.2f}")  # Convert cents to dollars

            # Get positions
            print("\nFetching positions...")
            positions = get_positions.sync(client=client)
            if positions.event_positions:
                print(f"Found {len(positions.event_positions)} event positions")
                for pos in positions.event_positions[:3]:  # Show first 3
                    print(f"  - {pos.event_ticker}: {pos.position} shares")
            else:
                print("No event positions found")

            # Get markets (public endpoint, but works with authenticated client)
            print("\nFetching markets...")
            markets = get_markets.sync(client=client, limit=3)
            print(f"Found {len(markets.markets)} markets")
            for market in markets.markets:
                print(f"  - {market.ticker}: {market.title[:50]}...")

    except ValueError as e:
        print(f"Configuration error: {e}")
        print("\nPlease set the following environment variables:")
        print("  KALSHI_API_KEY_ID=your-access-key-id")
        print("  KALSHI_PY_PRIVATE_KEY_PEM=your-private-key-pem-content")
    except Exception as e:
        print(f"Error: {e}")


async def async_example():
    """Asynchronous example using the authenticated client."""
    print("\n=== Asynchronous Authenticated Client Example ===\n")

    try:
        client = create_client()

        async with client as client:
            # Get account balance
            print("Fetching account balance (async)...")
            balance = await get_balance.asyncio(client=client)
            print(f"Account balance: ${balance.balance / 100:.2f}")

            # Get markets
            print("\nFetching markets (async)...")
            markets = await get_markets.asyncio(client=client, limit=3)
            print(f"Found {len(markets.markets)} markets")
            for market in markets.markets:
                print(f"  - {market.ticker}: {market.title[:50]}...")

    except ValueError as e:
        print(f"Configuration error: {e}")
    except Exception as e:
        print(f"Error: {e}")


def demo_with_file_path():
    """Example showing how to use file path."""
    print("\n=== File Path Example ===\n")

    # This is just for demonstration - replace with your actual credentials
    access_key_id = "your-access-key-id"
    private_key_path = "/path/to/your/private-key.pem"

    try:
        client = create_client(access_key_id=access_key_id, private_key_path=private_key_path)

        with client as client:
            balance = get_balance.sync(client=client)
            print(f"Account balance: ${balance.balance / 100:.2f}")

    except FileNotFoundError:
        print("Private key file not found. Please update the path in the example.")
    except Exception as e:
        print(f"Error: {e}")


def demo_with_pem_data():
    """Example showing how to use PEM data directly."""
    print("\n=== PEM Data Example ===\n")

    # This is just for demonstration - replace with your actual credentials
    access_key_id = "your-access-key-id"
    private_key_pem = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC...
-----END PRIVATE KEY-----"""

    try:
        client = create_client(access_key_id=access_key_id, private_key_data=private_key_pem)

        with client as client:
            balance = get_balance.sync(client=client)
            print(f"Account balance: ${balance.balance / 100:.2f}")

    except Exception as e:
        print(f"Error: {e}")


def demo_direct_client():
    """Example showing direct KalshiAuthenticatedClient usage."""
    print("\n=== Direct Client Example ===\n")

    # This is just for demonstration - replace with your actual credentials
    access_key_id = "your-access-key-id"
    private_key_pem = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC...
-----END PRIVATE KEY-----"""

    try:
        # Using KalshiAuthenticatedClient directly
        from kalshi_py import KalshiAuthenticatedClient

        client = KalshiAuthenticatedClient(access_key_id=access_key_id, private_key_pem=private_key_pem)

        with client as client:
            balance = get_balance.sync(client=client)
            print(f"Account balance: ${balance.balance / 100:.2f}")

    except Exception as e:
        print(f"Error: {e}")


def main():
    """Run all examples."""
    print("Kalshi Authenticated Client Examples")
    print("=" * 40)

    # Check if credentials are available
    has_env_creds = os.getenv("KALSHI_API_KEY_ID") and os.getenv("KALSHI_PY_PRIVATE_KEY_PEM")

    if has_env_creds:
        print("✓ Environment credentials found")
        sync_example()
        asyncio.run(async_example())
    else:
        print("⚠ Environment credentials not found")
        print("Set KALSHI_API_KEY_ID and KALSHI_PY_PRIVATE_KEY_PEM to run examples")
        print("\nDemo with explicit credentials (will fail without real credentials):")
        demo_with_file_path()
        demo_with_pem_data()
        demo_direct_client()


if __name__ == "__main__":
    main()
