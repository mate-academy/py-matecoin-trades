import json
import os
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trades:
        if trade["bought"] is not None:
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account += Decimal(str(trade["bought"]))

        if trade["sold"] is not None:
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account -= Decimal(trade["sold"])

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    matecoin_dir = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))
    profit_path = os.path.join(matecoin_dir, "profit.json")

    with open(profit_path, "w") as file:
        json.dump(profit, file, indent=2)
