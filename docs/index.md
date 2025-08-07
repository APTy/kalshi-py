# kalshi-py

A modern, type-safe Python client library for the Kalshi Trade API.

## Overview

### Features

- **Type Safety**: Full type hints and validation
- **Async Support**: Both synchronous and asynchronous APIs
- **Authentication**: Built-in RSA-PSS signature authentication
- **Auto-generated**: Generated from OpenAPI specification
- **Modern**: Built with httpx and attrs

## Quick Start

Get up and running in minutes:

```python
from kalshi_py import create_client
from kalshi_py.api.portfolio import get_balance

# Uses "KALSHI_API_KEY_ID" and "KALSHI_PY_PRIVATE_KEY_PEM" env vars, see Authenticate for more options
client = create_client()
balance = get_balance.sync(client=client)
print(f"Account balance: ${balance.balance}")
```

## Installation

```bash
pip install kalshi-py
```

For more installation options, see [Installation Guide](installation.md).

## Documentation Sections

- **[Installation](installation.md)** - Requirements, installation methods, dependencies
- **[Quick Start](quickstart.md)** - Basic usage, authenticated usage, async usage
- **[Authentication](authentication.md)** - RSA-PSS setup, security best practices
- **[Examples](examples.md)** - Basic, trading, and advanced code examples
- **[API Reference](api/client.md)** - Complete API documentation

## API Modules

The client is organized into logical modules:

- **Market API** - Market data, events, order books
- **Portfolio API** - Account balance, positions, orders
- **Communications API** - Announcements and communications
- **Collections API** - Event collections
- **Milestones API** - Milestone tracking
- **Structured Targets API** - Structured targets
- **API Keys API** - API key management

## Support

- [GitHub Issues](https://github.com/kalshi/kalshi-py/issues)
- [Kalshi API Documentation](https://docs.kalshi.com)
- [API Reference](api/client.md) - Complete API documentation
