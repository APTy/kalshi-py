# Client API Reference

This page documents the main client classes and functions in kalshi-py.

## Client Classes

::: kalshi_py.client.Client
handler: python
options:
show_source: true
show_root_heading: true

::: kalshi_py.client.AuthenticatedClient
handler: python
options:
show_source: true
show_root_heading: true

::: kalshi_py.auth.KalshiAuthenticatedClient
handler: python
options:
show_source: true
show_root_heading: true

## Factory Functions

::: kalshi_py.create_client
handler: python
options:
show_source: true
show_root_heading: true

## Error Classes

::: kalshi_py.errors.UnexpectedStatus
handler: python
options:
show_source: true
show_root_heading: true

## Usage Examples

### Creating a Public Client

```python
from kalshi_py import Client

client = Client(base_url="https://api.elections.kalshi.com/trade-api/v2")
```

### Creating an Authenticated Client

```python
from kalshi_py import create_client

# Using environment variables
client = create_client()

# Or with explicit credentials
client = create_client(
    access_key_id="your-key-id",
    private_key_path="/path/to/private-key.pem"
)
```

### Using the Client

```python
with client as client:
    from kalshi_py.api.market import get_markets
    response = get_markets.sync(client=client, limit=10)
    print(f"Found {len(response.markets)} markets")
```

## Configuration Options

### SSL Verification

```python
# Custom SSL certificate
client = create_client(verify_ssl="/path/to/certificate_bundle.pem")

# Disable SSL verification (not recommended for production)
client = create_client(verify_ssl=False)
```

### Timeouts and Headers

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
