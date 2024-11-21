import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    profit = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0"),
    }
    with open(file_name, "r") as file:
        trades = json.load(file)
    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            profit["earned_money"] -= bought * price
            profit["matecoin_account"] += bought
        if trade["sold"]:
            sold = Decimal(trade["sold"])
            profit["earned_money"] += sold * price
            profit["matecoin_account"] -= sold
    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])
    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
