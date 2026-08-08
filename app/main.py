import os
import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as f:
        trades = json.load(f)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    # Process each trade
    for trade in trades:
        if trade.get("bought") is not None:
            bought = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            matecoin_account += bought
            earned_money -= bought * price

        if trade.get("sold") is not None:
            sold = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            matecoin_account -= sold
            earned_money += sold * price

    # Prepare result
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    # Write to profit.json in current working directory with indentation
    profit_path = os.path.join(os.getcwd(), "profit.json")
    with open(profit_path, "w") as f:
        json.dump(result, f, indent=2)
