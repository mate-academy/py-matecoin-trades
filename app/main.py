from __future__ import annotations

from decimal import Decimal
import json


def calculate_profit(trades_file_name: str) -> None:
    with open(trades_file_name, "r", encoding="utf-8") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(str(trade["matecoin_price"]))

        if trade.get("bought"):
            bought_amount = Decimal(str(trade["bought"]))
            matecoin_account += bought_amount
            earned_money -= bought_amount * price
        elif trade.get("sold"):
            sold_amount = Decimal(str(trade["sold"]))
            matecoin_account -= sold_amount
            earned_money += sold_amount * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
