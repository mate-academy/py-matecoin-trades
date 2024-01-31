import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_balance = Decimal("0")

    for trade in trades:
        if trade.get("bought"):
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_balance += Decimal(trade["bought"])
        if trade.get("sold"):
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_balance -= Decimal(trade["sold"])

    with open("profit.json", "w") as file:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_balance)
            },
            file,
            indent=2
        )
