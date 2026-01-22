import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    profit = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    for trade in trades:
        coins = 0
        if trade["bought"]:
            coins += Decimal(trade["bought"])
        if trade["sold"]:
            coins -= Decimal(trade["sold"])
        profit["earned_money"] -= coins * Decimal(trade["matecoin_price"])
        profit["matecoin_account"] += coins

    profit = {key: str(value) for key, value in profit.items()}

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
