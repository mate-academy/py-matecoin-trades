import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        trades_history = json.load(f)

    profit = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    for trade in trades_history:

        if trade["bought"] is not None:
            profit["matecoin_account"] += Decimal(trade["bought"])
            profit["earned_money"] -= (
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            )

        if trade["sold"] is not None:
            profit["matecoin_account"] -= Decimal(trade["sold"])
            profit["earned_money"] += (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            )

    profit["matecoin_account"] = str(profit["matecoin_account"])
    profit["earned_money"] = str(profit["earned_money"])

    with open("profit.json", "w") as t:
        json.dump(profit, t, indent=2)
