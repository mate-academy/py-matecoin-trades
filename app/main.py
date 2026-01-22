import json
from decimal import Decimal
from typing import NoReturn


def calculate_profit(filename: str) -> NoReturn:
    with open(filename, "r") as f:
        trades = json.load(f)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in trades:
        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            matecoin_account += amount
            earned_money -= amount * price
        if trade["sold"] is not None:
            amount = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            matecoin_account -= amount
            earned_money += amount * price
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
