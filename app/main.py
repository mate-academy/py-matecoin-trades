import json
from decimal import Decimal
from typing import Any


def calculate_profit(filename: str) -> None:
    """
    Read trades from a JSON file, compute USD profit and Matecoin balance,
    and write them to profit.json as strings.
    """
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(filename, "r", encoding="utf-8") as file:
        trades: list[dict[str, Any]] = json.load(file)

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"]:
            volume = Decimal(trade["bought"])
            earned_money -= volume * price
            matecoin_account += volume

        if trade["sold"]:
            volume = Decimal(trade["sold"])
            earned_money += volume * price
            matecoin_account -= volume

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
