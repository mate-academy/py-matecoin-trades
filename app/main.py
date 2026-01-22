import json
import os
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(filename) as f:
        trades = json.load(f)

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            earned_money -= bought * price
            matecoin_account += bought
        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            earned_money += sold * price
            matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    profit_file_path = os.path.join(base_dir, "profit.json")

    with open(profit_file_path, "w") as f:
        json.dump(result, f, indent=2)

    return None
