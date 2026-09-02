import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = 0
    matecoin_account = 0

    with (open(file_name, "r") as f):
        trades_list = json.load(f)
        for trade in trades_list:
            if trade["bought"] is not None:
                earned_money -= (
                    Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
                )
                matecoin_account += Decimal(trade["bought"])
            if trade["sold"] is not None:
                earned_money += (
                    Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
                )
                matecoin_account -= Decimal(trade["sold"])
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
