import json
import os
from decimal import Decimal


def calculate_profit(trades_info: str) -> None:
    filepath = os.path.join(os.path.dirname(__file__), trades_info)
    with open(filepath, "r") as file:
        trades = json.load(file)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trades:
        if trade["bought"]:
            matecoin_account += Decimal(trade["bought"])
            earned_money -= (Decimal(trade["matecoin_price"])
                             * Decimal(trade["bought"]))

        if trade["sold"]:
            matecoin_account -= Decimal(trade["sold"])
            earned_money += (Decimal(trade["matecoin_price"])
                             * Decimal(trade["sold"]))

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f)
