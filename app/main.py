import os
import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    base_dir = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
    trades_file_path = os.path.join(base_dir, file_name)
    profit_file_path = os.path.join(base_dir, "profit.json")

    with open(trades_file_path, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in trades:
        bought_value = trade["bought"]
        bought = Decimal(bought_value) if bought_value else Decimal("0.0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0.0")
        matecoin_price = Decimal(trade["matecoin_price"])

        matecoin_account += bought
        matecoin_account -= sold

        earned_money -= bought * matecoin_price
        earned_money += sold * matecoin_price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open(profit_file_path, "w") as file:
        json.dump(result, file, indent=2)


if __name__ == "__main__":
    calculate_profit("app/trades.json")
