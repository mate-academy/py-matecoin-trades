import json
from decimal import Decimal
import os


def calculate_profit(trades_json: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(trades_json, "r") as file:
        trades = json.load(file)

    for trade in trades:
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        price = Decimal(trade["matecoin_price"])

        earned_money += (sold * price) - (bought * price)
        matecoin_account += bought - sold

    result = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}

    profit_file_path = os.path.join("..", "profit.json")
    with open(profit_file_path, "w") as file:
        json.dump(result, file, indent=2)
