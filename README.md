# kalshi-py

A client library for accessing Kalshi Trade API

## Installation

```bash
pip install kalshi-py
```

## Usage

### Basic Usage (Public Endpoints)

For public endpoints that don't require authentication:

```python
from kalshi_py import Client

client = Client(base_url="https://api.elections.kalshi.com/trade-api/v2")

from kalshi_py.api.market import get_markets
response = get_markets.sync(client=client, limit=10)
print(f"Found {len(response.markets)} markets")
```

### Authenticated Usage (Trading Endpoints)

For trading endpoints that require authentication, use the Kalshi-specific authenticated client:

```python
from kalshi_py import create_client

# Using environment variables ("KALSHI_API_KEY_ID" and "KALSHI_PY_PRIVATE_KEY_PEM")
client = create_client()

# Or with file path
client = create_client(
    access_key_id="your-access-key-id",
    private_key_path="/path/to/your/private-key.pem"
)

# Or with PEM data directly
client = create_client(
    access_key_id="your-access-key-id",
    private_key_data="-----BEGIN PRIVATE KEY-----\n..."
)

from kalshi_py.api.portfolio import get_balance
balance = get_balance.sync(client=client)
print(f"Account balance: {balance.balance}")
```

### Direct Client Usage

You can also create the authenticated client directly if you prefer:

```python
from kalshi_py import KalshiAuthenticatedClient

# Direct usage requires explicit credentials
client = KalshiAuthenticatedClient(
    access_key_id="your-access-key-id",
    private_key_pem="-----BEGIN PRIVATE KEY-----\n..."
)

from kalshi_py.api.portfolio import get_balance
balance = get_balance.sync(client=client)
print(f"Account balance: {balance.balance}")
```

### Environment Variables

You can set the following environment variables to avoid passing credentials explicitly:

- `KALSHI_API_KEY_ID`: Your Kalshi access key ID
- `KALSHI_PY_PRIVATE_KEY_PEM`: Your RSA private key in PEM format

### API Endpoints

The client supports both synchronous and asynchronous operations:

```python
from kalshi_py import create_client
from kalshi_py.api.market import get_markets
from kalshi_py.api.portfolio import get_balance

# Synchronous usage
client = create_client()
markets = get_markets.sync(client=client, limit=5)
balance = get_balance.sync(client=client)

# Asynchronous usage
import asyncio

async def main():
    client = create_client()
    markets = await get_markets.asyncio(client=client, limit=5)
    balance = await get_balance.asyncio(client=client)

asyncio.run(main())
```

### Authentication Details

The Kalshi API uses RSA-PSS signature authentication. Each request is signed with:

1. **Timestamp**: Current time in milliseconds
2. **Method**: HTTP method (GET, POST, etc.)
3. **Path**: API endpoint path
4. **Signature**: RSA-PSS signature of `timestamp + method + path`

The client automatically handles:

- Loading your private key from file
- Generating timestamps
- Creating signatures for each request
- Adding required headers (`KALSHI-ACCESS-KEY`, `KALSHI-ACCESS-SIGNATURE`, `KALSHI-ACCESS-TIMESTAMP`)

### Legacy Bearer Token Authentication

If you need to use the legacy bearer token authentication (not recommended for trading):

```python
from kalshi_py import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://api.elections.kalshi.com/trade-api/v2",
    token="your-bearer-token"
)
```

## Advanced Customizations

### Custom SSL Configuration

```python
client = create_client(
    verify_ssl="/path/to/certificate_bundle.pem"
)

# Or disable SSL verification (not recommended for production)
client = create_client(verify_ssl=False)
```

### Custom Headers and Timeouts

```python
import httpx

client = create_client(
    timeout=httpx.Timeout(30.0),
    headers={"User-Agent": "MyApp/1.0"}
)
```

### Request Logging

```python
def log_request(request):
    print(f"Request: {request.method} {request.url}")

def log_response(response):
    print(f"Response: {response.status_code}")

client = create_client(
    httpx_args={
        "event_hooks": {
            "request": [log_request],
            "response": [log_response]
        }
    }
)
```

## API Structure

Every API endpoint becomes a Python module with four functions:

1. `sync`: Blocking request that returns parsed data
2. `sync_detailed`: Blocking request that returns full response details
3. `asyncio`: Async request that returns parsed data
4. `asyncio_detailed`: Async request that returns full response details

All path/query parameters and request bodies become function arguments.

## Building / Publishing this package

This project uses [uv](https://github.com/astral-sh/uv) to manage dependencies and packaging. Here are the basics:

1. Update the metadata in `pyproject.toml` (e.g. authors, version).
2. If you're using a private repository: https://docs.astral.sh/uv/guides/integration/alternative-indexes/
3. Build a distribution with `uv build`, builds `sdist` and `wheel` by default.
4. Publish the client with `uv publish`, see documentation for publishing to private indexes.

If you want to install this client into another project without publishing it (e.g. for development) then:

1. If that project **is using uv**, you can simply do `uv add <path-to-this-client>` from that project
2. If that project is not using uv:
   1. Build a wheel with `uv build --wheel`.
   2. Install that wheel from the other project `pip install <path-to-wheel>`.
