import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    with open(file_path, "r") as file:
        list_of_trades = json.load(file)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in list_of_trades:
        if trade["bought"] is not None:
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account += Decimal(trade["bought"])
        if trade["sold"] is not None:
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account -= Decimal(trade["sold"])

    profits = {"earned_money": str(earned_money),
               "matecoin_account": str(matecoin_account)
               }

    with open("profit.json", "w") as f:
        json.dump(profits, f, indent=2)
