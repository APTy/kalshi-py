# Basic Usage Examples

## Getting Started

Here are some basic examples to get you started with kalshi-py.

## Fetching Markets

```python
from kalshi_py import Client
from kalshi_py.api.market import get_markets

client = Client(base_url="https://api.elections.kalshi.com/trade-api/v2")

response = get_markets.sync(client=client, limit=10)
print(f"Found {len(response.markets)} markets")

for market in response.markets:
    print(f"- {market.ticker}: {market.title}")
    print(f"  Status: {market.status}")
    print(f"  Volume: {market.volume}")
```

## Getting Account Balance

```python
from kalshi_py import create_client
from kalshi_py.api.portfolio import get_balance

client = create_client()

balance = get_balance.sync(client=client)
print(f"Account balance: ${balance.balance}")
```

## Fetching Market Details

```python
from kalshi_py import Client
from kalshi_py.api.market import get_market

client = Client(base_url="https://api.elections.kalshi.com/trade-api/v2")

market = get_market.sync(client=client, ticker="MARKET-TICKER")
print(f"Market: {market.market.title}")
print(f"Status: {market.market.status}")
print(f"Volume: {market.market.volume}")
```

## Error Handling

```python
from kalshi_py import Client
from kalshi_py.errors import UnexpectedStatus

client = Client(base_url="https://api.elections.kalshi.com/trade-api/v2")

try:
    response = get_markets.sync(client=client, limit=10)
    print(f"Found {len(response.markets)} markets")
except UnexpectedStatus as e:
    print(f"API error: {e.status_code} - {e.response.text}")
except Exception as e:
    print(f"Unexpected error: {e}")
```
