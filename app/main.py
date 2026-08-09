import json
from decimal import Decimal
from typing import Any


def calculate_profit(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as file:
        trades: list[dict[str, Any]] = json.load(file)

    matecoin_account: Decimal = Decimal("0")
    earned_money: Decimal = Decimal("0")

    for trade in trades:
        price: Decimal = Decimal(trade["matecoin_price"])

        bought: str | None = trade["bought"]
        sold: str | None = trade["sold"]

        if bought is not None:
            bought_amount: Decimal = Decimal(bought)
            matecoin_account += bought_amount
            earned_money -= bought_amount * price

        if sold is not None:
            sold_amount: Decimal = Decimal(sold)
            matecoin_account -= sold_amount
            earned_money += sold_amount * price

    result: dict[str, str] = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
