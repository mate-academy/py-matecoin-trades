import json
from decimal import Decimal
from typing import Dict, Any
import os


def calculate_profit(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        price = Decimal(trade["matecoin_price"])

        if bought is not None:
            bought_amount = Decimal(bought)
            matecoin_account += bought_amount
            earned_money -= bought_amount * price

        if sold is not None:
            sold_amount = Decimal(sold)
            matecoin_account -= sold_amount
            earned_money += sold_amount * price

    result: Dict[str, Any] = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(result, file)


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    trades_path = os.path.join(base_dir, "..", "trades.json")
    trades_path = os.path.normpath(trades_path)

    calculate_profit(trades_path)
    print("Profit calculated and saved to profit.json")
