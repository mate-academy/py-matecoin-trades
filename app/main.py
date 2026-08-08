import json
from decimal import Decimal
from typing import Dict


def calculate_profit(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            matecoin_account += amount
            earned_money -= amount * price
        if trade["sold"] is not None:
            amount = Decimal(trade["sold"])
            matecoin_account -= amount
            earned_money += amount * price

    data: Dict[str, str] = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return None
