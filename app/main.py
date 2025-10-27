import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in trades:
        if trade["bought"]:
            amount = (Decimal(trade["bought"])
                      * Decimal(trade["matecoin_price"]))
            earned_money = earned_money - amount
            matecoin_account = matecoin_account + Decimal(trade["bought"])

        if trade["sold"]:
            amount = Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            earned_money = earned_money + amount
            matecoin_account = matecoin_account - Decimal(trade["sold"])

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
