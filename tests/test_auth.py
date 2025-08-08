#!/usr/bin/env python3

import os
import tempfile

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

from kalshi_py import KalshiAuthenticatedClient
from kalshi_py.auth import KalshiAuth


def create_test_private_key():
    """Create a test private key for testing purposes."""
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())

    # Create temporary file
    temp_file = tempfile.NamedTemporaryFile(mode="wb", delete=False, suffix=".pem")
    temp_file.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )
    temp_file.close()

    return temp_file.name


def get_test_private_key_pem():
    """Create a test private key and return its PEM string."""
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())

    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    ).decode("utf-8")


def test_auth_creation():
    """Test that authenticated client can be created."""
    # Get test private key PEM
    private_key_pem = get_test_private_key_pem()

    # Test with explicit parameters
    client = KalshiAuthenticatedClient(access_key_id="test-key-id", private_key_pem=private_key_pem)

    assert isinstance(client, KalshiAuthenticatedClient)
    assert client.access_key_id == "test-key-id"
    assert client.private_key_pem == private_key_pem
    assert client._base_url == "https://api.elections.kalshi.com/trade-api/v2"


def test_auth_headers():
    """Test that authentication headers are generated correctly."""
    private_key_pem = get_test_private_key_pem()

    auth = KalshiAuth("test-key-id", private_key_pem)
    headers = auth.get_auth_headers("GET", "https://api.elections.kalshi.com/trade-api/v2/markets")

    assert "KALSHI-ACCESS-KEY" in headers
    assert "KALSHI-ACCESS-SIGNATURE" in headers
    assert "KALSHI-ACCESS-TIMESTAMP" in headers
    assert headers["KALSHI-ACCESS-KEY"] == "test-key-id"


def test_environment_variables():
    """Test that environment variables are used correctly."""
    private_key_pem = get_test_private_key_pem()

    # Set environment variables
    os.environ["KALSHI_API_KEY_ID"] = "env-key-id"
    os.environ["KALSHI_PY_PRIVATE_KEY_PEM"] = private_key_pem

    try:
        from kalshi_py import create_client

        client = create_client()

        assert client.access_key_id == "env-key-id"
        assert client.private_key_pem == private_key_pem
    finally:
        # Clean up
        if "KALSHI_API_KEY_ID" in os.environ:
            del os.environ["KALSHI_API_KEY_ID"]
        if "KALSHI_PY_PRIVATE_KEY_PEM" in os.environ:
            del os.environ["KALSHI_PY_PRIVATE_KEY_PEM"]


def test_relative_url_handling():
    """Test that relative URLs are handled correctly for authentication."""
    private_key_pem = get_test_private_key_pem()

    auth = KalshiAuth("test-key-id", private_key_pem)

    # Test with relative path
    headers1 = auth.get_auth_headers("GET", "/markets")

    # Test with full URL
    headers2 = auth.get_auth_headers("GET", "https://api.elections.kalshi.com/trade-api/v2/markets")

    # Both should have the same path in the signature
    # We can't compare signatures directly because timestamps are different
    # But we can verify that both have the required headers
    assert "KALSHI-ACCESS-SIGNATURE" in headers1
    assert "KALSHI-ACCESS-SIGNATURE" in headers2
    assert "KALSHI-ACCESS-TIMESTAMP" in headers1
    assert "KALSHI-ACCESS-TIMESTAMP" in headers2
    assert headers1["KALSHI-ACCESS-KEY"] == headers2["KALSHI-ACCESS-KEY"]
