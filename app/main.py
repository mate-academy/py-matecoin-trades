import json
from decimal import Decimal
from typing import Any


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades: list[dict[str, Any]] = json.load(f)

    earned_money: Decimal = Decimal("0")
    matecoin_account: Decimal = Decimal("0")

    for trade in trades:
        price: Decimal = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought: Decimal = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * price

        if trade["sold"] is not None:
            sold: Decimal = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * price

    result: dict[str, str] = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
