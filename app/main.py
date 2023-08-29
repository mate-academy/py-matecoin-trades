import json
from decimal import Decimal
import os
from os.path import abspath, dirname

BASE_DIR: str = dirname(dirname(abspath(__file__)))
PROFIT: str = os.path.join(BASE_DIR, "profit.json")


def calculate_profit(filename: str) -> None:
    matecoin_account: Decimal = Decimal("0")
    earned_money: Decimal = Decimal("0")

    with open(filename, "r") as fobj:
        trades: list[dict] = json.load(fobj)

    for trade in trades:
        if trade["bought"] is not None:
            matecoin_account += Decimal(trade["bought"])
            earned_money -= Decimal(trade["bought"]) * Decimal(
                trade["matecoin_price"]
            )
        if trade["sold"] is not None:
            matecoin_account -= Decimal(trade["sold"])
            earned_money += Decimal(trade["sold"]) * Decimal(
                trade["matecoin_price"]
            )
    with open(PROFIT, "w") as fobj:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account),
            },
            fobj,
            indent=2,
        )
