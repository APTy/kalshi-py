import base64
import datetime
from typing import Union
from urllib.parse import urlparse

import httpx
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey

from .client import AuthenticatedClient


def load_private_key_from_file(file_path: str) -> RSAPrivateKey:
    """Load RSA private key from PEM file."""
    with open(file_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None, backend=default_backend())
        if not isinstance(private_key, RSAPrivateKey):
            raise ValueError("Private key must be an RSA key")
        return private_key


def load_private_key_from_string(private_key_pem: str) -> RSAPrivateKey:
    """Load RSA private key from PEM string."""
    private_key = serialization.load_pem_private_key(
        private_key_pem.encode("utf-8"), password=None, backend=default_backend()
    )
    if not isinstance(private_key, RSAPrivateKey):
        raise ValueError("Private key must be an RSA key")
    return private_key


def sign_pss_text(private_key: rsa.RSAPrivateKey, text: str) -> str:
    """Sign text using RSA-PSS with SHA256."""
    message = text.encode("utf-8")

    try:
        signature = private_key.sign(
            message,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.DIGEST_LENGTH),
            hashes.SHA256(),
        )
        return base64.b64encode(signature).decode("utf-8")
    except InvalidSignature as e:
        raise ValueError("RSA sign PSS failed") from e


class KalshiAuth:
    """Authentication handler for Kalshi API using RSA-PSS signatures."""

    def __init__(self, access_key_id: str, private_key_pem: str):
        """Initialize authentication with access key ID and private key PEM string."""
        self.access_key_id = access_key_id
        self.private_key = load_private_key_from_string(private_key_pem)

    def get_auth_headers(self, method: str, url: str) -> dict[str, str]:
        """Generate authentication headers for the request."""
        current_time = datetime.datetime.now()
        timestamp = current_time.timestamp()
        current_time_milliseconds = int(timestamp * 1000)
        timestamp_str = str(current_time_milliseconds)

        # Ensure method is uppercase
        method = method.upper()

        # Handle both full URLs and relative paths
        if url.startswith("http"):
            parsed_url = urlparse(url)
            path = parsed_url.path
        else:
            # If it's a relative path, we need to construct the full path
            # The base_url is https://api.elections.kalshi.com/trade-api/v2
            # So we need to add /trade-api/v2 to the relative path
            relative_path = url if url.startswith("/") else f"/{url}"
            path = f"/trade-api/v2{relative_path}"

        msg_string = timestamp_str + method + path

        signature = sign_pss_text(self.private_key, msg_string)

        return {
            "KALSHI-ACCESS-KEY": self.access_key_id,
            "KALSHI-ACCESS-SIGNATURE": signature,
            "KALSHI-ACCESS-TIMESTAMP": timestamp_str,
        }


class AuthenticatedHTTPXClient(httpx.Client):
    """Custom httpx client that adds Kalshi authentication headers to each request."""

    def __init__(self, kalshi_auth: KalshiAuth, **kwargs):
        super().__init__(**kwargs)
        self.kalshi_auth = kalshi_auth

    def request(self, method: str, url: Union[str, httpx.URL], **kwargs):
        """Override request to add authentication headers."""
        auth_headers = self.kalshi_auth.get_auth_headers(method, str(url))

        if "headers" in kwargs:
            kwargs["headers"].update(auth_headers)
        else:
            kwargs["headers"] = auth_headers

        return super().request(method, url, **kwargs)


class AuthenticatedAsyncHTTPXClient(httpx.AsyncClient):
    """Custom async httpx client that adds Kalshi authentication headers to each request."""

    def __init__(self, kalshi_auth: KalshiAuth, **kwargs):
        super().__init__(**kwargs)
        self.kalshi_auth = kalshi_auth

    async def request(self, method: str, url: Union[str, httpx.URL], **kwargs):
        """Override request to add authentication headers."""
        auth_headers = self.kalshi_auth.get_auth_headers(method, str(url))

        if "headers" in kwargs:
            kwargs["headers"].update(auth_headers)
        else:
            kwargs["headers"] = auth_headers

        return await super().request(method, url, **kwargs)


class KalshiAuthenticatedClient(AuthenticatedClient):
    """Authenticated client for Kalshi API with RSA-PSS signature authentication."""

    def __init__(
        self,
        access_key_id: str,
        private_key_pem: str,
        base_url: str = "https://api.elections.kalshi.com/trade-api/v2",
        **kwargs,
    ):
        """Initialize authenticated client.

        Args:
            access_key_id: Kalshi access key ID (required)
            private_key_pem: PEM-encoded private key (required)
            base_url: API base URL (defaults to elections API)
            **kwargs: Additional arguments passed to base Client
        """
        self.access_key_id = access_key_id
        self.private_key_pem = private_key_pem
        self.auth = KalshiAuth(self.access_key_id, self.private_key_pem)

        # Initialize base AuthenticatedClient with a dummy token
        # We'll override the authentication in our custom httpx clients
        super().__init__(
            base_url=base_url,
            token="dummy",  # Will be overridden by our custom auth
            **kwargs,
        )

        # Set custom httpx clients with authentication
        self._client = None
        self._async_client = None

    def get_httpx_client(self):
        """Get the underlying authenticated httpx client."""
        if self._client is None:
            self._client = AuthenticatedHTTPXClient(
                kalshi_auth=self.auth,
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                **self._httpx_args,
            )
        return self._client

    def get_async_httpx_client(self):
        """Get the underlying authenticated async httpx client."""
        if self._async_client is None:
            self._async_client = AuthenticatedAsyncHTTPXClient(
                kalshi_auth=self.auth,
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                **self._httpx_args,
            )
        return self._async_client

    def __enter__(self):
        """Context manager entry."""
        self.get_httpx_client().__enter__()
        return self

    def __exit__(self, *args, **kwargs):
        """Context manager exit."""
        return self.get_httpx_client().__exit__(*args, **kwargs)

    async def __aenter__(self):
        """Async context manager entry."""
        await self.get_async_httpx_client().__aenter__()
        return self

    async def __aexit__(self, *args, **kwargs):
        """Async context manager exit."""
        return await self.get_async_httpx_client().__aexit__(*args, **kwargs)
