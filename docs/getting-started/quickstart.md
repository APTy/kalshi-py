# Quick Start

This guide will help you get started with kalshi-py in just a few minutes.

## Basic Usage (Public Endpoints)

For public endpoints that don't require authentication:

```python
from kalshi_py import Client
from kalshi_py.api.market import get_markets

# Create a client for public endpoints
client = Client(base_url="https://api.elections.kalshi.com/trade-api/v2")

# Get markets
with client as client:
    response = get_markets.sync(client=client, limit=10)
    print(f"Found {len(response.markets)} markets")

    for market in response.markets[:3]:
        print(f"- {market.ticker}: {market.title}")
```

## Authenticated Usage (Trading Endpoints)

For trading endpoints that require authentication:

```python
from kalshi_py import create_client
from kalshi_py.api.portfolio import get_balance

# Create authenticated client
client = create_client()

# Get account balance
with client as client:
    balance = get_balance.sync(client=client)
    print(f"Account balance: ${balance.balance}")
```

## Async Usage

The client also supports async operations:

```python
import asyncio
from kalshi_py import create_client
from kalshi_py.api.market import get_markets
from kalshi_py.api.portfolio import get_balance

async def main():
    client = create_client()
    async with client as client:
        # Get markets
        markets = await get_markets.asyncio(client=client, limit=5)
        print(f"Found {len(markets.markets)} markets")

        # Get balance
        balance = await get_balance.asyncio(client=client)
        print(f"Balance: ${balance.balance}")

asyncio.run(main())
```

## Environment Variables

You can set environment variables to avoid passing credentials explicitly:

```bash
export KALSHI_API_KEY_ID="your-access-key-id"
export KALSHI_PY_PRIVATE_KEY_PEM="-----BEGIN PRIVATE KEY-----\n..."
```

Then create the client without parameters:

```python
from kalshi_py import create_client

client = create_client()  # Uses environment variables
```

## Next Steps

- [Authentication](authentication.md) - Learn about RSA-PSS authentication
- [API Reference](../api/client.md) - Explore all available endpoints
- [Examples](../examples/basic-usage.md) - More detailed examples
