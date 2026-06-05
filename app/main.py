import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    trades = json.load(open(filename))
    matecoin_account = Decimal("0")
    earned_money = Decimal("0")
    for trade in trades:
        if trade["bought"]:
            matecoin_account += Decimal(trade["bought"])
            earned_money -= (
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            )
        if trade["sold"]:
            matecoin_account -= Decimal(trade["sold"])
            earned_money += (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            )
    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
