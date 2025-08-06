# Advanced Examples

## Async Operations

### Async Market Data

```python
import asyncio
from kalshi_py import create_client
from kalshi_py.api.market import get_markets, get_market_orderbook

async def get_market_data():
    client = create_client()

    # Get markets
    markets = await get_markets.asyncio(client=client, limit=5)

    # Get order book for first market
    if markets.markets:
        ticker = markets.markets[0].ticker
        orderbook = await get_market_orderbook.asyncio(client=client, ticker=ticker)
        print(f"Order book for {ticker}:")
        print(f"  Yes bids: {len(orderbook.orderbook.yes_bids)}")
        print(f"  Yes asks: {len(orderbook.orderbook.yes_asks)}")

asyncio.run(get_market_data())
```

### Concurrent API Calls

```python
import asyncio
from kalshi_py import create_client
from kalshi_py.api.portfolio import get_balance, get_positions, get_orders

async def get_account_overview():
    client = create_client()

    # Make concurrent API calls
    balance_task = get_balance.asyncio(client=client)
    positions_task = get_positions.asyncio(client=client)
    orders_task = get_orders.asyncio(client=client)

    balance, positions, orders = await asyncio.gather(
        balance_task, positions_task, orders_task
    )

    print(f"Balance: ${balance.balance}")
    print(f"Active positions: {len(positions.market_positions)}")
    print(f"Open orders: {len(orders.orders)}")

asyncio.run(get_account_overview())
```

## Custom SSL Configuration

```python
from kalshi_py import create_client

# Custom SSL certificate
client = create_client(verify_ssl="/path/to/certificate_bundle.pem")

# Disable SSL verification (not recommended for production)
client = create_client(verify_ssl=False)
```

## Request Logging

```python
from kalshi_py import create_client

def log_request(request):
    print(f"Request: {request.method} {request.url}")
    print(f"Headers: {dict(request.headers)}")

def log_response(response):
    print(f"Response: {response.status_code}")
    print(f"Response headers: {dict(response.headers)}")

client = create_client(
    httpx_args={
        "event_hooks": {
            "request": [log_request],
            "response": [log_response]
        }
    }
)
```

## Custom Timeouts

```python
import httpx
from kalshi_py import create_client

# Set custom timeout
client = create_client(
    timeout=httpx.Timeout(30.0, connect=10.0)
)

# Or use different timeouts for different operations
client = create_client(
    timeout=httpx.Timeout(
        timeout=30.0,
        connect=5.0,
        read=25.0,
        write=10.0,
        pool=1.0
    )
)
```

## Custom Headers

```python
from kalshi_py import create_client

client = create_client(
    headers={
        "User-Agent": "MyApp/1.0",
        "X-Custom-Header": "custom-value"
    }
)
```

## Error Handling with Retries

```python
import time
from kalshi_py import create_client
from kalshi_py.errors import UnexpectedStatus

def api_call_with_retry(func, max_retries=3, delay=1):
    for attempt in range(max_retries):
        try:
            return func()
        except UnexpectedStatus as e:
            if e.status_code == 429:  # Rate limit
                if attempt < max_retries - 1:
                    time.sleep(delay * (2 ** attempt))  # Exponential backoff
                    continue
            raise
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(delay)
                continue
            raise

# Usage
client = create_client()

from kalshi_py.api.portfolio import get_balance

balance = api_call_with_retry(
    lambda: get_balance.sync(client=client)
)
print(f"Balance: ${balance.balance}")
```

## WebSocket-like Polling

```python
import time
from kalshi_py import create_client
from kalshi_py.api.market import get_market_orderbook

def monitor_orderbook(ticker, interval=5):
    client = create_client()
    last_orderbook = None

    while True:
        try:
            orderbook = get_market_orderbook.sync(client=client, ticker=ticker)

            # Check if orderbook changed
            if last_orderbook != orderbook.orderbook:
                print(f"Order book updated for {ticker}")
                print(f"  Yes bid: {orderbook.orderbook.yes_bids[0].price if orderbook.orderbook.yes_bids else 'None'}")
                print(f"  Yes ask: {orderbook.orderbook.yes_asks[0].price if orderbook.orderbook.yes_asks else 'None'}")
                last_orderbook = orderbook.orderbook

            time.sleep(interval)

        except KeyboardInterrupt:
            print("Monitoring stopped")
            break
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(interval)

# Usage: monitor_orderbook("MARKET-TICKER")
```
