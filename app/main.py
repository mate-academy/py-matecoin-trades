import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades_data = json.load(f)

    earned_money = 0
    matecoin_account = 0
    for trade in trades_data:
        if trade["bought"] is not None:
            earned_money -= (
                Decimal(trade["bought"])
                * Decimal(trade["matecoin_price"])
            )
            matecoin_account += Decimal(trade["bought"])
        if trade["sold"] is not None:
            earned_money += (
                Decimal(trade["sold"])
                * Decimal(trade["matecoin_price"])
            )
            matecoin_account -= Decimal(trade["sold"])

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
