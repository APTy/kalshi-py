# Authentication

kalshi-py uses RSA-PSS signature authentication for secure API access. This guide explains how to set up and use authentication.

## Overview

The Kalshi API uses RSA-PSS signature authentication where each request is signed with:

1. **Timestamp**: Current time in milliseconds
2. **Method**: HTTP method (GET, POST, etc.)
3. **Path**: API endpoint path
4. **Signature**: RSA-PSS signature of `timestamp + method + path`

## Setting Up Authentication

### 1. Get Your API Credentials

You'll need:

- **Access Key ID**: Your Kalshi access key identifier
- **Private Key**: RSA private key in PEM format

### 2. Create the Client

#### Using Environment Variables (Recommended)

Set your credentials as environment variables:

```bash
export KALSHI_API_KEY_ID="your-access-key-id"
export KALSHI_PY_PRIVATE_KEY_PEM="-----BEGIN PRIVATE KEY-----\n..."
```

Then create the client:

```python
from kalshi_py import create_client

client = create_client()  # Uses environment variables
```

#### Using File Path

```python
from kalshi_py import create_client

client = create_client(
    access_key_id="your-access-key-id",
    private_key_path="/path/to/your/private-key.pem"
)
```

#### Using PEM Data Directly

```python
from kalshi_py import create_client

client = create_client(
    access_key_id="your-access-key-id",
    private_key_data="-----BEGIN PRIVATE KEY-----\n..."
)
```

## How It Works

The client automatically handles:

1. **Loading your private key** from file or environment
2. **Generating timestamps** for each request
3. **Creating signatures** using RSA-PSS
4. **Adding required headers**:
   - `KALSHI-ACCESS-KEY`: Your access key ID
   - `KALSHI-ACCESS-SIGNATURE`: RSA-PSS signature
   - `KALSHI-ACCESS-TIMESTAMP`: Request timestamp

## Example Request Flow

```python
from kalshi_py import create_client
from kalshi_py.api.portfolio import get_balance

# Create authenticated client
client = create_client()

# Make authenticated request
balance = get_balance.sync(client=client)
print(f"Balance: ${balance.balance}")
```

Behind the scenes, the client:

1. Generates a timestamp
2. Creates signature: `RSA-PSS(timestamp + "GET" + "/v2/balance")`
3. Sends request with authentication headers

## Security Best Practices

### Store Credentials Securely

```bash
# Use environment variables (recommended)
export KALSHI_API_KEY_ID="your-key-id"
export KALSHI_PY_PRIVATE_KEY_PEM="$(cat /path/to/private-key.pem)"

# Or use a .env file (don't commit to version control)
echo "KALSHI_API_KEY_ID=your-key-id" >> .env
echo "KALSHI_PY_PRIVATE_KEY_PEM=$(cat /path/to/private-key.pem)" >> .env
```

### Rotate Keys Regularly

- Generate new API keys periodically
- Keep private keys secure and never share them
- Use different keys for different environments

### Monitor Usage

```python
def log_request(request):
    print(f"Making request to: {request.method} {request.url}")

client = create_client(
    httpx_args={
        "event_hooks": {
            "request": [log_request]
        }
    }
)
```

## Troubleshooting

### Common Issues

**"access_key_id must be provided"**

- Set `KALSHI_API_KEY_ID` environment variable
- Or pass `access_key_id` parameter to `create_client()`

**"Cannot specify both private_key_path and private_key_data"**

- Use only one method to provide the private key

**"Invalid signature"**

- Check that your private key is correct
- Ensure your system clock is synchronized
- Verify the access key ID matches your private key

### Debug Mode

Enable debug logging to see authentication details:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

client = create_client()
```

## Legacy Bearer Token Authentication

For compatibility with older systems, you can also use bearer token authentication:

```python
from kalshi_py import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://api.elections.kalshi.com/trade-api/v2",
    token="your-bearer-token"
)
```

**Note**: Bearer token authentication is not recommended for trading operations.

## Next Steps

- [Examples](examples.md) - See authentication in action
- [API Reference](api/client.md) - Explore all available endpoints
