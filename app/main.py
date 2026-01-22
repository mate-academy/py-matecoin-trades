import json
from decimal import Decimal


def calculate_profit(name_json: str) -> None:
    with open(name_json, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade.get("bought"):
            matecoin_account += Decimal(trade.get("bought"))
            earned_money -= (Decimal(trade.get("matecoin_price"))
                             * Decimal(trade.get("bought")))
        if trade.get("sold"):
            matecoin_account -= Decimal(trade.get("sold"))
            earned_money += (Decimal(trade.get("matecoin_price"))
                             * Decimal(trade.get("sold")))

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
