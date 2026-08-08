import json
from decimal import Decimal
import os


def calculate_profit(file_name: str) -> None:

    base_dir = os.path.dirname(__file__)
    file_name = os.path.join(base_dir, file_name)

    with open(file_name, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            amount = Decimal(trade["bought"])
            matecoin_account += amount
            earned_money -= amount * price  # витрати
        if trade["sold"]:
            amount = Decimal(trade["sold"])
            matecoin_account -= amount
            earned_money += amount * price  # дохід

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    profit_path = os.path.join(os.getcwd(), "profit.json")
    with open(profit_path, "w") as f:
        json.dump(result, f, indent=2)
