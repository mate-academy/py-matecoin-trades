import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        trades_list = json.load(file)

    profit = {"earned_money": Decimal(0), "matecoin_account": Decimal(0)}

    for trade in trades_list:
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            profit["matecoin_account"] += bought
            profit["earned_money"] -= bought * Decimal(trade["matecoin_price"])

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            profit["matecoin_account"] -= sold
            profit["earned_money"] += sold * Decimal(trade["matecoin_price"])

    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
