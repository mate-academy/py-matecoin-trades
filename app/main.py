from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    profit = {
        "earned_money": Decimal(0),
        "matecoin_account": Decimal(0)
    }

    for trade in trades:
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

    profit_str = {
        key: str(value) for key, value in profit.items()
    }

    with open("profit.json", "w") as file:
        json.dump(profit_str, file, indent=2)
