import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    with open(file_name, "r") as file_in:
        trades = json.load(file_in)

    for trade in trades:
        if trade["bought"]:
            matecoin_account += Decimal(trade["bought"])
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))

        if trade["sold"]:
            matecoin_account -= Decimal(trade["sold"])
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))

    with open("profit.json", "w") as file_out:
        json.dump(
            {"earned_money": str(earned_money),
             "matecoin_account": str(matecoin_account)},
            file_out,
            indent=2)
