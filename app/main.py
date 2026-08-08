import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)
    calculated_profit = {"earned_money": 0, "matecoin_account": 0}
    for trade in trades:
        if trade["bought"]:
            calculated_profit["matecoin_account"] += Decimal(trade["bought"])
            calculated_profit["earned_money"] -= (
                Decimal(trade["bought"])
                * Decimal(trade["matecoin_price"])
            )
        if trade["sold"]:
            calculated_profit["matecoin_account"] -= Decimal(trade["sold"])
            calculated_profit["earned_money"] += (
                Decimal(trade["sold"])
                * Decimal(trade["matecoin_price"])
            )
    for key, value in calculated_profit.items():
        calculated_profit[key] = str(value)
    with open("profit.json", "w") as file:
        json.dump(calculated_profit, file, indent=2)
