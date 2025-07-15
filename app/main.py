import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade.get("bought"):
            matecoin_account += Decimal(trade["bought"])
            earned_money -= (
                Decimal(trade["bought"])
                * Decimal(trade["matecoin_price"])
            )

        if trade.get("sold"):
            matecoin_account -= Decimal(trade["sold"])
            earned_money += (
                Decimal(trade["sold"])
                * Decimal(trade["matecoin_price"])
            )

    with open("profit.json", "w") as file:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            file,
            indent=2
        )
