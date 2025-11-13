import json
from decimal import Decimal
import os


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r", encoding="utf-8") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"]:
            bought = Decimal(trade["bought"])
            earned_money -= bought * price
            matecoin_account += bought

        if trade["sold"]:
            sold = Decimal(trade["sold"])
            earned_money += sold * price
            matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    project_root = os.path.dirname(os.path.dirname(__file__))
    profit_path = os.path.join(project_root, "profit.json")

    with open(profit_path, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
