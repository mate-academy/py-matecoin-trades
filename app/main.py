from decimal import Decimal
import json
from typing import Any


def to_decimal(value: Any) -> Decimal:
    if value is None:
        return Decimal("0")
    return Decimal(str(value))


def calculate_profit(filename: str) -> None:

    with open(filename, "r") as file:
        trades = json.load(file)
        matecoin_account = Decimal("0")
        earned_money = Decimal("0")

        for trade in trades:
            bought = to_decimal(trade.get("bought"))
            sold = to_decimal(trade.get("sold"))
            price = to_decimal(trade.get("matecoin_price"))
            delta = bought - sold
            earned_money -= delta * price
            matecoin_account += delta

    with open("./profit.json", "w") as file:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            file,
            indent=2
        )


if __name__ == "__main__":
    calculate_profit("./trades.json")
