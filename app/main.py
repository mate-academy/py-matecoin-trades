import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    profit = Decimal(0)
    amount = Decimal(0)

    with open(file_name, "r") as file_in:
        trades = json.load(file_in)

    for trade in trades:
        if trade["bought"]:
            amount += Decimal(trade["bought"])
            profit -= (Decimal(trade["bought"])
                       * Decimal(trade["matecoin_price"]))

        if trade["sold"]:
            amount -= Decimal(trade["sold"])
            profit += (Decimal(trade["sold"])
                       * Decimal(trade["matecoin_price"]))

    with open("profit.json", "w") as file_out:
        json.dump(
            {"earned_money": str(profit),
             "matecoin_account": str(amount)},
            file_out,
            indent=2)
