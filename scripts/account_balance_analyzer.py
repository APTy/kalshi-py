#!/usr/bin/env python3

"""
Account Balance Analyzer

This script calls get_positions and analyzes the account balance by summing up
various position metrics to understand the total account value and composition.
"""

from kalshi_py import create_client
from kalshi_py.api.portfolio import get_balance, get_positions
from kalshi_py.models.model_get_positions_response import ModelGetPositionsResponse


def format_currency(amount_cents: int) -> str:
    """Convert cents to formatted dollar string with commas."""
    dollars = amount_cents / 100
    return f"${dollars:,.2f}"


def format_number(value: int) -> str:
    """Format integer with commas."""
    return f"{value:,}"


def safe_add(current: int, value) -> int:
    """Safely add a value to current, handling None and UNSET."""
    if value is None:
        return current
    try:
        return current + int(value)
    except (ValueError, TypeError):
        return current


def analyze_positions(positions: ModelGetPositionsResponse) -> dict:
    """Analyze positions and calculate various totals."""
    analysis = {
        "market_positions": {
            "count": 0,
            "total_market_exposure": 0,
            "total_realized_pnl": 0,
            "total_fees_paid": 0,
            "total_resting_orders": 0,
            "total_traded": 0,
        },
        "event_positions": {
            "count": 0,
            "total_event_exposure": 0,
            "total_realized_pnl": 0,
            "total_fees_paid": 0,
            "total_resting_orders": 0,
            "total_cost": 0,
        },
        "combined": {
            "total_exposure": 0,
            "total_realized_pnl": 0,
            "total_fees_paid": 0,
            "total_resting_orders": 0,
        },
    }

    if positions.market_positions:
        for pos in positions.market_positions:
            analysis["market_positions"]["count"] += 1

            analysis["market_positions"]["total_market_exposure"] = safe_add(
                analysis["market_positions"]["total_market_exposure"], getattr(pos, "market_exposure", 0)
            )
            analysis["combined"]["total_exposure"] = safe_add(
                analysis["combined"]["total_exposure"], getattr(pos, "market_exposure", 0)
            )

            analysis["market_positions"]["total_realized_pnl"] = safe_add(
                analysis["market_positions"]["total_realized_pnl"], getattr(pos, "realized_pnl", 0)
            )
            analysis["combined"]["total_realized_pnl"] = safe_add(
                analysis["combined"]["total_realized_pnl"], getattr(pos, "realized_pnl", 0)
            )

            analysis["market_positions"]["total_fees_paid"] = safe_add(
                analysis["market_positions"]["total_fees_paid"], getattr(pos, "fees_paid", 0)
            )
            analysis["combined"]["total_fees_paid"] = safe_add(
                analysis["combined"]["total_fees_paid"], getattr(pos, "fees_paid", 0)
            )

            analysis["market_positions"]["total_resting_orders"] = safe_add(
                analysis["market_positions"]["total_resting_orders"], getattr(pos, "resting_orders_count", 0)
            )
            analysis["combined"]["total_resting_orders"] = safe_add(
                analysis["combined"]["total_resting_orders"], getattr(pos, "resting_orders_count", 0)
            )

            analysis["market_positions"]["total_traded"] = safe_add(
                analysis["market_positions"]["total_traded"], getattr(pos, "total_traded", 0)
            )

    if positions.event_positions:
        for pos in positions.event_positions:
            analysis["event_positions"]["count"] += 1

            analysis["event_positions"]["total_event_exposure"] = safe_add(
                analysis["event_positions"]["total_event_exposure"], getattr(pos, "event_exposure", 0)
            )
            analysis["combined"]["total_exposure"] = safe_add(
                analysis["combined"]["total_exposure"], getattr(pos, "event_exposure", 0)
            )

            analysis["event_positions"]["total_realized_pnl"] = safe_add(
                analysis["event_positions"]["total_realized_pnl"], getattr(pos, "realized_pnl", 0)
            )
            analysis["combined"]["total_realized_pnl"] = safe_add(
                analysis["combined"]["total_realized_pnl"], getattr(pos, "realized_pnl", 0)
            )

            analysis["event_positions"]["total_fees_paid"] = safe_add(
                analysis["event_positions"]["total_fees_paid"], getattr(pos, "fees_paid", 0)
            )
            analysis["combined"]["total_fees_paid"] = safe_add(
                analysis["combined"]["total_fees_paid"], getattr(pos, "fees_paid", 0)
            )

            analysis["event_positions"]["total_resting_orders"] = safe_add(
                analysis["event_positions"]["total_resting_orders"], getattr(pos, "resting_order_count", 0)
            )
            analysis["combined"]["total_resting_orders"] = safe_add(
                analysis["combined"]["total_resting_orders"], getattr(pos, "resting_order_count", 0)
            )

            analysis["event_positions"]["total_cost"] = safe_add(
                analysis["event_positions"]["total_cost"], getattr(pos, "total_cost", 0)
            )

    return analysis


def print_analysis(analysis: dict, account_balance: int):
    """Print the analysis results in a formatted way."""
    print("=" * 60)
    print("ACCOUNT BALANCE ANALYSIS")
    print("=" * 60)

    print(f"\nAccount Balance: {format_currency(account_balance)}")

    print("\n" + "-" * 40)
    print("MARKET POSITIONS")
    print("-" * 40)
    market = analysis["market_positions"]
    print(f"Count: {format_number(market['count'])}")
    print(f"Total Market Exposure: {format_currency(market['total_market_exposure'])}")
    print(f"Total Realized P&L: {format_currency(market['total_realized_pnl'])}")
    print(f"Total Fees Paid: {format_currency(market['total_fees_paid'])}")
    print(f"Total Resting Orders: {format_number(market['total_resting_orders'])}")
    print(f"Total Traded: {format_number(market['total_traded'])}")

    print("\n" + "-" * 40)
    print("EVENT POSITIONS")
    print("-" * 40)
    event = analysis["event_positions"]
    print(f"Count: {format_number(event['count'])}")
    print(f"Total Event Exposure: {format_currency(event['total_event_exposure'])}")
    print(f"Total Realized P&L: {format_currency(event['total_realized_pnl'])}")
    print(f"Total Fees Paid: {format_currency(event['total_fees_paid'])}")
    print(f"Total Resting Orders: {format_number(event['total_resting_orders'])}")
    print(f"Total Cost: {format_currency(event['total_cost'])}")

    print("\n" + "-" * 40)
    print("COMBINED TOTALS")
    print("-" * 40)
    combined = analysis["combined"]
    print(f"Total Exposure: {format_currency(combined['total_exposure'])}")
    print(f"Total Realized P&L: {format_currency(combined['total_realized_pnl'])}")
    print(f"Total Fees Paid: {format_currency(combined['total_fees_paid'])}")
    print(f"Total Resting Orders: {format_number(combined['total_resting_orders'])}")

    print("\n" + "-" * 40)
    print("BALANCE ANALYSIS")
    print("-" * 40)

    total_exposure = combined["total_exposure"]
    total_realized_pnl = combined["total_realized_pnl"]
    total_fees_paid = combined["total_fees_paid"]

    calculated_balance = account_balance + total_exposure + total_realized_pnl - total_fees_paid
    print(f"Account Balance: {format_currency(account_balance)}")
    print(f"Total Exposure: {format_currency(total_exposure)}")
    print(f"Total Realized P&L: {format_currency(total_realized_pnl)}")
    print(f"Total Fees Paid: {format_currency(total_fees_paid)}")
    print(f"Calculated Net: {format_currency(calculated_balance)}")

    if calculated_balance != account_balance:
        print(
            f"\nNote: Calculated balance ({format_currency(calculated_balance)}) "
            f"differs from account balance ({format_currency(account_balance)})"
        )
        print("This may be due to:")
        print("- Unrealized P&L not included in position data")
        print("- Pending orders affecting available balance")
        print("- Other account adjustments")
    else:
        print("\n✓ Account balance matches calculated total")


def main():
    """Main function to run the account balance analysis."""
    print("Account Balance Analyzer")
    print("=" * 30)

    try:
        client = create_client()

        print("Fetching account balance...")
        balance_response = get_balance.sync(client=client)
        if balance_response is None:
            print("Error: Could not fetch account balance")
            return

        account_balance = balance_response.balance or 0

        print("Fetching positions...")
        positions_response = get_positions.sync(client=client)
        if positions_response is None:
            print("Error: Could not fetch positions")
            return

        print("Analyzing positions...")
        analysis = analyze_positions(positions_response)

        print_analysis(analysis, account_balance)

    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure you have set up your authentication credentials:")
        print("- KALSHI_API_KEY_ID environment variable")
        print("- KALSHI_PRIVATE_KEY_PATH environment variable")
        print("Or pass them directly to create_client()")


if __name__ == "__main__":
    main()
