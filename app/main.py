import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        data = json.load(file)
    profit = {"earned_money": Decimal(0), "matecoin_account": Decimal(0)}
    for trade in data:
        if trade["bought"] is not None:
            profit["earned_money"] -= (
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            )
            profit["matecoin_account"] += Decimal(trade["bought"])
        if trade["sold"] is not None:
            profit["earned_money"] += (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            )
            profit["matecoin_account"] -= Decimal(trade["sold"])
    profit = {key: str(value) for key, value in profit.items()}
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
