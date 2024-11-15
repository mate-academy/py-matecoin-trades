import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    """
    Reads a JSON file with Matecoin trades, calculates the profit,
    and writes the results to profit.json.

    :param file_name: Name of the input JSON file containing trade data.
    """
    # Load trades data from the input file
    with open(file_name, "r") as f:
        trades = json.load(f)

    # Initialize variables to track earned money and Matecoin account balance
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    # Process each trade
    for trade in trades:
        # Parse values using Decimal for precise arithmetic
        bought = Decimal(trade.get("bought", "0") or "0")
        sold = Decimal(trade.get("sold", "0") or "0")
        price = Decimal(trade["matecoin_price"])

        # Update balances
        matecoin_account += bought - sold
        earned_money -= bought * price
        earned_money += sold * price

    # Prepare results as strings for JSON compatibility
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    # Write the results to profit.json
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)  # Use 2 spaces for indentation
