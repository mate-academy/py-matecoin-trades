import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename) as file:
        trades = json.load(file)

    earned_money = 0
    matecoin_account = 0

    for trade in trades:
        if trade.get("bought"):
            matecoin_account += Decimal(trade.get("bought"))
            earned_money -= (Decimal(trade.get("bought"))
                             * Decimal(trade.get("matecoin_price")))

        if trade.get("sold"):
            matecoin_account -= Decimal(trade.get("sold"))
            earned_money += (Decimal(trade.get("sold"))
                             * Decimal(trade.get("matecoin_price")))

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
