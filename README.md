# Kalshi Python Client Library

A modern, type-safe Python client library for the [Kalshi Trade API](https://docs.kalshi.com/), generated from the official OpenAPI specification using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).

## Features

- **Type-safe**: Full type hints and validation using Pydantic models
- **Modern**: Built with Python 3.9+ and modern async/await support
- **Comprehensive**: Covers all Kalshi API endpoints including markets, orders, portfolio, and more
- **Flexible**: Supports both synchronous and asynchronous usage patterns
- **Well-documented**: Auto-generated documentation for all models and endpoints

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for dependency management and packaging.

```bash
# Clone the repository
git clone https://github.com/APTy/kalshi-py.git
cd kalshi-py

# Install dependencies
uv sync

# Install the client library
uv pip install -e .
```

## Quick Start

### Basic Usage

```python
from kalshi_py import Client
from kalshi_py.api.market import get_markets

# Create a client for public endpoints
client = Client(base_url="https://api.elections.kalshi.com/trade-api/v2")

# Fetch markets
with client as client:
    markets = get_markets.sync(client=client, limit=10)
    if markets and markets.markets:
        for market in markets.markets:
            print(f"{market.ticker}: {market.title}")
```

### Authenticated Usage

```python
from kalshi_py import AuthenticatedClient
from kalshi_py.api.portfolio import get_balance

# Create an authenticated client
auth_client = AuthenticatedClient(
    base_url="https://api.elections.kalshi.com/trade-api/v2",
    token="your_api_token_here"
)

# Fetch account balance
with auth_client as client:
    balance = get_balance.sync(client=client)
    if balance:
        print(f"Account balance: {balance.balance}")
```

### Async Usage

```python
import asyncio
from kalshi_py import Client
from kalshi_py.api.market import get_markets

async def fetch_markets():
    client = Client(base_url="https://api.elections.kalshi.com/trade-api/v2")

    async with client as client:
        markets = await get_markets.asyncio(client=client, limit=5)
        if markets and markets.markets:
            for market in markets.markets:
                print(f"{market.ticker}: {market.title}")

# Run the async function
asyncio.run(fetch_markets())
```

## API Modules

The generated client includes the following API modules:

- **`market`**: Market data, events, order books, candlesticks
- **`portfolio`**: Account balance, positions, orders, fills
- **`api_keys`**: API key management
- **`communications`**: Announcements and communications
- **`collection`**: Event collections and multivariate events
- **`milestone`**: Milestone tracking
- **`structured_target`**: Structured targets
- **`default`**: Untagged endpoints

## Usage Patterns

Each API endpoint provides four functions:

1. **`sync()`**: Synchronous call that returns parsed data
2. **`sync_detailed()`**: Synchronous call that returns a `Response` object with metadata
3. **`asyncio()`**: Asynchronous call that returns parsed data
4. **`asyncio_detailed()`**: Asynchronous call that returns a `Response` object with metadata

### Example: Creating Orders

```python
from kalshi_py import AuthenticatedClient
from kalshi_py.api.portfolio import create_order
from kalshi_py.models import (
    GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequest
)

auth_client = AuthenticatedClient(
    base_url="https://api.elections.kalshi.com/trade-api/v2",
    token="your_api_token_here"
)

# Create an order request
order_request = GithubComKalshiExchangeInfraSvcApi2ModelCreateOrderRequest(
    ticker="MARKET-TICKER",
    side="yes",
    type="limit",
    yes_price=50,
    no_price=50,
    count=1
)

with auth_client as client:
    response = create_order.sync(client=client, json_body=order_request)
    if response:
        print(f"Order created: {response.order_id}")
```

## Configuration

### Client Options

Both `Client` and `AuthenticatedClient` accept the following configuration options:

- **`base_url`**: The base URL for the API (required)
- **`timeout`**: Request timeout in seconds
- **`verify_ssl`**: Whether to verify SSL certificates (default: `True`)
- **`headers`**: Additional headers to send with requests
- **`cookies`**: Additional cookies to send with requests

### Error Handling

The client includes comprehensive error handling:

```python
from kalshi_py import errors

try:
    with client as client:
        response = get_markets.sync(client=client)
except errors.UnexpectedStatus as e:
    print(f"API returned unexpected status: {e.status_code}")
except errors.ClientError as e:
    print(f"Client error: {e}")
```

## Development

### Regenerating the Client

To regenerate the client from the OpenAPI specification:

```bash
# Install the generator
uv add openapi-python-client --dev

# Regenerate the client
uv run openapi-python-client generate --path openapi.yaml --meta uv --output-path .
```

### Running Tests

```bash
# Run the example
uv run python example.py

# Run the test suite
uv run python test_client.py

# Run linting
uv run ruff check kalshi_py/
```

## Project Structure

```
kalshi-py/
├── kalshi_py/                     # Generated client library
│   ├── api/                       # API endpoint modules
│   ├── models/                    # Pydantic models
│   ├── client.py                  # Client classes
│   └── types.py                   # Type definitions
├── openapi.yaml                   # OpenAPI specification
├── example.py                     # Usage examples
├── test_client.py                 # Test suite
├── pyproject.toml                 # Project configuration
└── README.md                      # This documentation
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:

- Check the [Kalshi API documentation](https://docs.kalshi.com/)
- Open an issue on this repository
- Review the generated client documentation
