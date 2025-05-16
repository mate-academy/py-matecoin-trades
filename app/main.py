import json
import os
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r", encoding="utf-8") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        price = Decimal(trade["matecoin_price"])

        matecoin_account += bought
        matecoin_account -= sold
        earned_money += sold * price
        earned_money -= bought * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    output_dir = "py-matecoin-trades/tests"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "profit.json")
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
