import json
from decimal import Decimal
from typing import Dict


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r", encoding="utf-8") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade.get("bought"):
            bought_volume = Decimal(trade["bought"])
            earned_money -= bought_volume * price
            matecoin_account += bought_volume

        if trade.get("sold"):
            sold_volume = Decimal(trade["sold"])
            earned_money += sold_volume * price
            matecoin_account -= sold_volume

    result: Dict[str, str] = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
