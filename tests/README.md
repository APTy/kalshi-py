# Tests

This directory contains the test suite for the Kalshi Python client library.

## Running Tests

### Using uv (recommended)

```bash
# Run all tests
uv run pytest

# Run tests with verbose output
uv run pytest -v

# Run tests with coverage
uv run pytest --cov=kalshi_py

# Run only specific test file
uv run pytest tests/test_auth.py

# Run tests matching a pattern
uv run pytest -k "auth"
```

### Using pytest directly

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v
```

## Test Structure

- `test_auth.py` - Authentication and client creation tests
- `test_client.py` - Basic client functionality tests (sync and async)
- `test_balance.py` - Account balance tests (requires authentication)
- `example.py` - Example usage scripts
- `example_authenticated.py` - Authenticated example scripts

## Test Categories

### Unit Tests

- `test_auth.py` - Tests authentication mechanisms and client creation
- `test_client.py` - Tests basic API client functionality

### Integration Tests

- `test_balance.py` - Tests authenticated API calls (skipped if no credentials)

## Environment Variables

Some tests require authentication credentials:

- `KALSHI_API_KEY_ID` - Your Kalshi API key ID
- `KALSHI_PY_PRIVATE_KEY_PEM` - Your private key in PEM format

Tests that require authentication will be skipped if these environment variables are not set.

## Coverage

The test suite includes coverage reporting. To generate a coverage report:

```bash
uv run pytest --cov=kalshi_py --cov-report=html
```

This will create an HTML coverage report in the `htmlcov/` directory.
