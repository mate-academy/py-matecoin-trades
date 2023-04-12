from __future__ import annotations
import json
from _decimal import Decimal


def calculate_profit(trades_file: json) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * matecoin_price
        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * matecoin_price

    with open("profit.json", "w") as file:
        json.dump({"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)},
                  file, indent=2,)
