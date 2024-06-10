import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    with open(name_file, "r") as file:
        trades = json.load(file)
    profit = {"earned_money": 0, "matecoin_account": 0}
    for trade in trades:
        if trade["bought"]:
            profit["matecoin_account"] += Decimal(trade["bought"])
            profit["earned_money"] -= (Decimal(trade["bought"])
                                       * Decimal(trade["matecoin_price"]))
        if trade["sold"]:
            profit["matecoin_account"] -= Decimal(trade["sold"])
            profit["earned_money"] += (Decimal(trade["sold"])
                                       * Decimal(trade["matecoin_price"]))
    for key, value in profit.items():
        profit[key] = str(value)
    with open("profit.json", "w") as file_prof:
        json.dump(profit, file_prof, indent=2)
