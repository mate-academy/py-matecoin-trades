import json
from decimal import Decimal
from typing import Any


def calculate_profit(file_name: str) -> None:

    with open(file_name, "r") as file:
        trades: list[dict[str, Any]] = json.load(file)

    earned_money: Decimal = Decimal("0")
    matecoin_account: Decimal = Decimal("0")

    for trade in trades:

        if trade["bought"] is not None:
            money_spent = Decimal(trade["bought"]) * Decimal(
                trade["matecoin_price"]
            )

            earned_money -= money_spent
            matecoin_account += Decimal(trade["bought"])

        if trade["sold"] is not None:
            money_received = Decimal(trade["sold"]) * Decimal(
                trade["matecoin_price"]
            )

            earned_money += money_received
            matecoin_account -= Decimal(trade["sold"])

    result: dict[str, str] = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
