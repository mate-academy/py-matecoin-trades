from __future__ import annotations

import json
from decimal import Decimal
from typing import TypedDict


class Trade(TypedDict):
    bought: str | None
    sold: str | None
    matecoin_price: str | None


def calculate_profit(file_name: str) -> None:
    trades: list[Trade]

    with open(file_name) as f:
        trades = json.load(f)

    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    for trade in trades:
        if bought := trade["bought"]:
            bought = Decimal(bought)
            matecoin_account += bought
            earned_money -= bought * Decimal(trade["matecoin_price"])

        if sold := trade["sold"]:
            sold = Decimal(sold)
            matecoin_account -= sold
            earned_money += sold * Decimal(trade["matecoin_price"])

    with open("profit.json", "w") as profit_file:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            profit_file,
            indent=2,
        )
