import json
from decimal import Decimal
from typing import Dict


def calculate_profit(
        filename: str = "trades.json") -> Dict[str, str]:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(filename, "r", encoding="utf-8") as f:
        trades = json.load(f)

    for trade in trades:
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            matecoin_account += bought
            earned_money -= bought * price
        elif trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            matecoin_account -= sold
            earned_money += sold * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    return result
