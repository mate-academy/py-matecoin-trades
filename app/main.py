from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as data:
        trades = json.load(data)

    profit = {"earned_money": Decimal(0), "matecoin_account": Decimal(0)}

    for trade in trades:
        if trade["bought"]:
            profit["matecoin_account"] += Decimal(trade["bought"])
            profit["earned_money"] -= (Decimal(trade["bought"])
                                       * Decimal(trade["matecoin_price"]))

        if trade["sold"]:
            profit["matecoin_account"] -= Decimal(trade["sold"])
            profit["earned_money"] += (Decimal(trade["sold"])
                                       * Decimal(trade["matecoin_price"]))

    calculate = {key: str(value) for key, value in profit.items()}

    with open("profit.json", "w") as profit_calculation:
        json.dump(calculate, profit_calculation, indent=2)
