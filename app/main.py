import json
import os
from decimal import Decimal
from pathlib import Path


def calculate_profit(file_name: str) -> None:
    b_coins, s_coins, b_money, s_money = 4 * (Decimal("0"),)

    with open(file_name, "r") as file:
        trades = json.load(file)

        for trade in trades:
            if trade.get("bought"):
                b_coins += Decimal(trade.get("bought"))
                b_money += (
                    Decimal(trade.get("bought"))
                    * Decimal(trade.get("matecoin_price"))
                )
            if trade.get("sold"):
                s_coins += Decimal(trade.get("sold"))
                s_money += (
                    Decimal(trade.get("sold"))
                    * Decimal(trade.get("matecoin_price"))
                )
    path = str(Path(__file__).resolve().parent.parent) + os.sep + "profit.json"
    with open(path, "w") as file:

        json.dump({
            "earned_money": str(s_money - b_money),
            "matecoin_account": str(b_coins - s_coins)
        }, file, indent=2)
