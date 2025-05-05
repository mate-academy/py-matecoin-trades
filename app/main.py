import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file_in:
        trades = json.load(file_in)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in trades:
        if trade.get("bought"):
            earned_money -= (Decimal(str(trade["bought"]))
                             * Decimal(str(trade["matecoin_price"])))
            matecoin_account += Decimal(str(trade["bought"]))

        if trade.get("sold"):
            earned_money += (Decimal(str(trade["sold"]))
                             * Decimal(str(trade["matecoin_price"])))
            matecoin_account -= Decimal(str(trade["sold"]))

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file_out:
        json.dump(profit, file_out, indent=2)
