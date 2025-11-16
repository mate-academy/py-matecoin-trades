import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    with open(trades) as json_file:
        data = json.load(json_file)
    if not data:
        return
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in data:
        if trade["bought"]:
            earned_money -= (Decimal(str(trade["bought"]))
                             * Decimal(str(trade["matecoin_price"])))
            matecoin_account += Decimal(str(trade["bought"]))
        if trade["sold"]:
            earned_money += (Decimal(str(trade["sold"]))
                             * Decimal(str(trade["matecoin_price"])))
            matecoin_account -= Decimal(str(trade["sold"]))
        profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        }
        with open("profit.json", "w") as json_file:
            json.dump(profit, json_file, indent=2)
