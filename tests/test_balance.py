import os

import pytest

from kalshi_py import create_client
from kalshi_py.api.portfolio import get_balance


@pytest.mark.skipif(
    not os.getenv("KALSHI_API_KEY_ID") or not os.getenv("KALSHI_PY_PRIVATE_KEY_PEM"),
    reason="Requires KALSHI_API_KEY_ID and KALSHI_PY_PRIVATE_KEY_PEM environment variables"
)
def test_balance():
    """Test that we can fetch account balance."""
    client = create_client()

    balance = get_balance.sync(client=client)
    assert balance is not None
    assert hasattr(balance, 'balance')
    assert isinstance(balance.balance, (int, float))
