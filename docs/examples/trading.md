# Trading Examples

## Placing Orders

### Market Order

```python
from kalshi_py import create_client
from kalshi_py.api.portfolio import create_order

client = create_client()

order = create_order.sync(
    client=client,
    ticker="MARKET-TICKER",
    side="yes",
    type="market",
    action="buy",
    count=10
)
print(f"Order placed: {order.order.order_id}")
```

### Limit Order

```python
from kalshi_py import create_client
from kalshi_py.api.portfolio import create_order

client = create_client()

order = create_order.sync(
    client=client,
    ticker="MARKET-TICKER",
    side="yes",
    type="limit",
    action="buy",
    count=10,
    yes_price=50  # 50 cents
)
print(f"Limit order placed: {order.order.order_id}")
```

## Canceling Orders

```python
from kalshi_py import create_client
from kalshi_py.api.portfolio import cancel_order

client = create_client()

result = cancel_order.sync(client=client, order_id="ORDER-ID")
print(f"Order canceled: {result.order.order_id}")
```

## Getting Order Status

```python
from kalshi_py import create_client
from kalshi_py.api.portfolio import get_order

client = create_client()

order = get_order.sync(client=client, order_id="ORDER-ID")
print(f"Order status: {order.order.status}")
print(f"Filled count: {order.order.filled_count}")
```

## Batch Operations

### Batch Create Orders

```python
from kalshi_py import create_client
from kalshi_py.api.portfolio import batch_create_orders

client = create_client()

orders = batch_create_orders.sync(
    client=client,
    orders=[
        {
            "ticker": "MARKET-TICKER",
            "side": "yes",
            "type": "limit",
            "action": "buy",
            "count": 10,
            "yes_price": 50
        },
        {
            "ticker": "MARKET-TICKER",
            "side": "no",
            "type": "limit",
            "action": "sell",
            "count": 5,
            "no_price": 60
        }
    ]
)

for order in orders.orders:
    print(f"Order {order.order_id}: {order.status}")
```

### Batch Cancel Orders

```python
from kalshi_py import create_client
from kalshi_py.api.portfolio import batch_cancel_orders

client = create_client()

result = batch_cancel_orders.sync(
    client=client,
    order_ids=["ORDER-ID-1", "ORDER-ID-2"]
)

for order in result.orders:
    print(f"Order {order.order_id}: {order.status}")
```

## Getting Positions

```python
from kalshi_py import create_client
from kalshi_py.api.portfolio import get_positions

client = create_client()

positions = get_positions.sync(client=client)

for position in positions.market_positions:
    print(f"Market: {position.ticker}")
    print(f"  Yes position: {position.yes_position}")
    print(f"  No position: {position.no_position}")
    print(f"  Total value: ${position.total_value}")
```

## Getting Fills

```python
from kalshi_py import create_client
from kalshi_py.api.portfolio import get_fills

client = create_client()

fills = get_fills.sync(client=client, limit=10)

for fill in fills.fills:
    print(f"Fill: {fill.fill_id}")
    print(f"  Market: {fill.ticker}")
    print(f"  Side: {fill.side}")
    print(f"  Count: {fill.count}")
    print(f"  Price: {fill.price}")
    print(f"  Time: {fill.created_time}")
```
