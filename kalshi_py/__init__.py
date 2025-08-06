"""A client library for accessing Kalshi Trade API"""

import os

from .auth import KalshiAuthenticatedClient
from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
    "KalshiAuthenticatedClient",
    "create_client",
)


def create_client(
    base_url: str = "https://api.elections.kalshi.com/trade-api/v2",
    access_key_id: str | None = None,
    private_key_path: str | None = None,
    private_key_data: str | None = None,
    **kwargs,
) -> KalshiAuthenticatedClient:
    """Create an authenticated Kalshi client with RSA-PSS signature authentication.

    Args:
        base_url: API base URL (defaults to elections API)
        access_key_id: Kalshi access key ID (from environment if not provided)
        private_key_path: Path to private key file (mutually exclusive with private_key_data)
        private_key_data: PEM-encoded private key string (mutually exclusive with private_key_path)
        **kwargs: Additional arguments passed to the client

    Returns:
        Authenticated client instance

    Example:
        ```python
        from kalshi_py import create_client

        # Using environment variables
        client = create_client()

        # Or with file path
        client = create_client(
            access_key_id="your-key-id",
            private_key_path="/path/to/private-key.pem"
        )

        # Or with PEM data
        client = create_client(
            access_key_id="your-key-id",
            private_key_data="-----BEGIN PRIVATE KEY-----\n..."
        )
        ```
    """
    # Get access key ID from parameters or environment
    final_access_key_id = access_key_id or os.getenv("KALSHI_API_KEY_ID")

    if not final_access_key_id:
        raise ValueError("access_key_id must be provided or set in KALSHI_API_KEY_ID environment variable")

    # Handle private key - check for mutual exclusivity
    if private_key_path and private_key_data:
        raise ValueError("Cannot specify both private_key_path and private_key_data")

    if private_key_path:
        # Read from file
        with open(private_key_path) as f:
            final_private_key_data = f.read()
    elif private_key_data:
        # Use provided PEM data
        final_private_key_data = private_key_data
    else:
        # Try environment variable
        final_private_key_data = os.getenv("KALSHI_PY_PRIVATE_KEY_PEM")

    if not final_private_key_data:
        raise ValueError(
            "private_key_path, private_key_data, or KALSHI_PY_PRIVATE_KEY_PEM environment variable must be provided"
        )

    return KalshiAuthenticatedClient(
        base_url=base_url,
        access_key_id=final_access_key_id,
        private_key_pem=final_private_key_data,
        raise_on_unexpected_status=True,
        **kwargs,
    )
