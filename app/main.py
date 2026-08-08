import json
from decimal import Decimal


def calculate_profit(name: str) -> None:
    with open(name, "r") as file:
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
    profit["matecoin_account"] = str(profit["matecoin_account"])
    profit["earned_money"] = str(profit["earned_money"])
    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
