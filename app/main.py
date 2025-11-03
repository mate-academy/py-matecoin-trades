from __future__ import annotations

import json
from decimal import Decimal
from typing import Any


def calculate_profit(file_name: str) -> None:
    """Calculate total profit and remaining Matecoin balance."""
    with open(file_name, "r", encoding="utf-8") as file:
        trades: list[dict[str, Any]] = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            earned_money -= bought * price
            matecoin_account += bought
        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            earned_money += sold * price
            matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as output_file:
        json.dump(result, output_file, indent=2)


if __name__ == "__main__":
    calculate_profit("app/trades.json")
