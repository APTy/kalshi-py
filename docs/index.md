# kalshi-py

A modern, type-safe Python client library for the Kalshi Trade API.

## Features

- **Type Safety**: Full type hints and validation
- **Async Support**: Both synchronous and asynchronous APIs
- **Authentication**: Built-in RSA-PSS signature authentication
- **Auto-generated**: Generated from OpenAPI specification
- **Modern**: Built with httpx and attrs

## Quick Start

```python
from kalshi_py import create_client

# Create authenticated client
client = create_client()

# Get account balance
with client as client:
    from kalshi_py.api.portfolio import get_balance
    balance = get_balance.sync(client=client)
    print(f"Balance: ${balance.balance}")
```

## Installation

```bash
pip install kalshi-py
```

## Documentation

- **[Getting Started](getting-started/installation.md)** - Installation and setup
- **[Quick Start](getting-started/quickstart.md)** - Your first API calls
- **[Authentication](getting-started/authentication.md)** - Setting up authentication
- **[API Reference](api/client.md)** - Complete API documentation
- **[Examples](examples/basic-usage.md)** - Code examples and patterns

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
