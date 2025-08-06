#!/usr/bin/env python3

from kalshi_py import Client
from kalshi_py.api.market import get_markets


def main():
    # Create a client for public endpoints (no authentication required)
    client = Client(base_url="https://api.elections.kalshi.com/trade-api/v2")

    print("=== Kalshi API Client Example ===\n")

    # Example 1: Get markets (public endpoint)
    print("1. Fetching markets...")
    try:
        with client as client:
            markets_response = get_markets.sync(client=client, limit=5)
            if markets_response and markets_response.markets:
                print(f"Found {len(markets_response.markets)} markets")
                for market in markets_response.markets[:3]:
                    print(f"  - {market.ticker}: {market.title}")
                    print(f"    Status: {market.status}, Volume: {market.volume}")
                    print(f"    Yes Bid: {market.yes_bid}, Yes Ask: {market.yes_ask}")
                    print()
            else:
                print("No markets found or error occurred")
    except Exception as e:
        print(f"Error fetching markets: {e}")

    # Example 2: Get specific market details
    print("2. Fetching specific market details...")
    try:
        with client as client:
            # You would need a valid market ticker here
            # market_response = get_market.sync(client=client, ticker="MARKET-TICKER")
            # if market_response:
            #     print(f"Market: {market_response.market.title}")
            #     print(f"Status: {market_response.market.status}")
            print("(Skipping specific market fetch - need valid ticker)")
    except Exception as e:
        print(f"Error fetching market details: {e}")

    # Example 3: Authenticated client (for private endpoints)
    print("3. Authenticated client example...")
    print("To use authenticated endpoints, you would need API credentials:")
    print("""
    # Example with authentication:
    auth_client = AuthenticatedClient(
        base_url="https://api.elections.kalshi.com/trade-api/v2",
        token="your_api_token_here"
    )

    with auth_client as client:
        balance = get_balance.sync(client=client)
        if balance:
            print(f"Account balance: {balance.balance}")
    """)

    print("\n=== Available API Modules ===")
    print("The generated client includes these API modules:")
    print("- market: Market data, events, order books")
    print("- portfolio: Account balance, positions, orders")
    print("- api_keys: API key management")
    print("- communications: Announcements and communications")
    print("- collection: Event collections")
    print("- milestone: Milestone tracking")
    print("- structured_target: Structured targets")
    print("- default: Untagged endpoints")

    print("\n=== Usage Patterns ===")
    print("Each endpoint provides 4 functions:")
    print("- sync(): Synchronous call, returns parsed data")
    print("- sync_detailed(): Synchronous call, returns Response object")
    print("- asyncio(): Asynchronous call, returns parsed data")
    print("- asyncio_detailed(): Asynchronous call, returns Response object")


if __name__ == "__main__":
    main()
