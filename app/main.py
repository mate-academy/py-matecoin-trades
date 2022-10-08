import json
from decimal import Decimal


def calculate_profit(trades: json) -> None:
    earned_money = 0
    matecoin_account = 0

    with open(trades) as f:
        for trade in json.load(f):
            if trade["bought"]:
                earned_money -= (Decimal(trade["bought"])
                                 * Decimal(trade["matecoin_price"]))
                matecoin_account += Decimal(trade["bought"])

            if trade["sold"]:
                earned_money += (Decimal(trade["sold"])
                                 * Decimal(trade["matecoin_price"]))
                matecoin_account -= Decimal(trade["sold"])

        profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        }

        with open("profit.json", "w") as f:
            json.dump(profit, f, indent=2)
