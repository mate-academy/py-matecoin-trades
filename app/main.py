import json
from decimal import Decimal
import os


def calculate_profit(file_name: str) -> None:
    if not os.path.exists(file_name):
        return

    with open(file_name, "r") as file:
        trades = json.load(file)

    matecoin_account = Decimal("0.0")
    earned_money = Decimal("0.0")

    for trade in trades:
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        matecoin_price = Decimal(trade["matecoin_price"])

        matecoin_account += bought - sold
        earned_money += (sold * matecoin_price) - (bought * matecoin_price)

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
