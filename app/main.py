import json
from decimal import Decimal
from typing import Any


def calculate_profit(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as f:
        trades: list[dict[str, Any]] = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought_amount = Decimal(trade["bought"])
            # You spent money → negative
            earned_money -= bought_amount * price
            matecoin_account += bought_amount

        if trade["sold"] is not None:
            sold_amount = Decimal(trade["sold"])
            # You earned money → positive
            earned_money += sold_amount * price
            matecoin_account -= sold_amount

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
