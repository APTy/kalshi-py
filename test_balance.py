from kalshi_py import create_client
from kalshi_py.api.portfolio import get_balance

client = create_client()

balance = get_balance.sync(client=client)
if balance is None:
    raise Exception("Balance is None")

print(f"Account balance: ${balance.balance}")
