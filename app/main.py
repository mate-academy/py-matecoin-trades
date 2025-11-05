import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            matecoin_account += Decimal(trade["bought"])

            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))

        if trade["sold"] is not None:
            matecoin_account -= Decimal(trade["sold"])

            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))

    profit_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit_dict, f, indent=2)
