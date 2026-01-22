import json
import os
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade.get("bought") is not None:
            amount = Decimal(trade["bought"])
            earned_money -= amount * price
            matecoin_account += amount

        if trade.get("sold") is not None:
            amount = Decimal(trade["sold"])
            earned_money += amount * price
            matecoin_account -= amount

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    project_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
    profit_path = os.path.join(project_root, "profit.json")
    with open(profit_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
