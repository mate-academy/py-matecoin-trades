import json
from decimal import Decimal
from typing import Any, Dict


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades: Any = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        matecoin_price = Decimal(trade["matecoin_price"])

        matecoin_account += bought
        matecoin_account -= sold
        earned_money -= bought * matecoin_price
        earned_money += sold * matecoin_price

    result: Dict[str, str] = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=4)
