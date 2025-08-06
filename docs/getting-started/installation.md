# Installation

## Requirements

- Python 3.9 or higher
- pip or uv package manager

## Install from PyPI

The easiest way to install kalshi-py is from PyPI:

```bash
pip install kalshi-py
```

## Install with uv

If you're using uv (recommended):

```bash
uv add kalshi-py
```

## Install from source

To install the latest development version:

```bash
git clone https://github.com/kalshi/kalshi-py.git
cd kalshi-py
pip install -e .
```

## Dependencies

kalshi-py has the following dependencies:

- `httpx>=0.23.0,<0.29.0` - HTTP client
- `attrs>=22.2.0` - Data classes
- `python-dateutil>=2.8.0,<3` - Date parsing
- `cryptography>=41.0.0` - RSA-PSS signatures

## Verify Installation

You can verify the installation by running:

```python
import kalshi_py
print(kalshi_py.__version__)
```

## Next Steps

- [Quick Start](quickstart.md) - Make your first API call
- [Authentication](authentication.md) - Set up API credentials
