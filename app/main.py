import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file_r:
        trades = json.load(file_r)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade["bought"] and trade["sold"]:
            earned_money += ((Decimal(trade["sold"])
                              - Decimal(trade["bought"]))
                             * Decimal(trade["matecoin_price"]))
            matecoin_account += (Decimal(trade["bought"])
                                 - Decimal(trade["sold"]))
        elif trade["bought"]:
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account += Decimal(trade["bought"])
        else:
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account -= Decimal(trade["sold"])

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file_w:
        json.dump(profit, file_w, indent=2)
