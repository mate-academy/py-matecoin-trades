import json
from decimal import Decimal


def calculate_profit(json_file: str) -> None:
    with open(json_file) as source_file:
        source_data = json.load(source_file)

    profit = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    for trade in source_data:
        if trade["bought"]:
            bought = (
                Decimal(trade["bought"])
                * Decimal(trade["matecoin_price"])
            )
            profit["earned_money"] -= bought
            profit["matecoin_account"] += Decimal(trade["bought"])
        if trade["sold"]:
            sold = (
                Decimal(trade["sold"])
                * Decimal(trade["matecoin_price"])
            )
            profit["earned_money"] += sold
            profit["matecoin_account"] -= Decimal(trade["sold"])

    for key in profit:
        profit[key] = str(profit[key])

    with open("profit.json", "w") as outfile:
        json.dump(profit, outfile, indent=2)
