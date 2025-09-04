import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    # Load trades from JSON file
    with open(filename, "r") as f:
        trades = json.load(f)

    # Initialize totals
    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    # Process each trade
    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade.get("bought"):
            amount = Decimal(trade["bought"])
            matecoin_account += amount
            earned_money -= amount * price  # spending money
        elif trade.get("sold"):
            amount = Decimal(trade["sold"])
            matecoin_account -= amount
            earned_money += amount * price  # earning money

    # Prepare result as strings
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    # Save to profit.json
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
