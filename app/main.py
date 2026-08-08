import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    profit_dict = {"earned_money": 0, "matecoin_account": 0}
    with open(file_name, "r") as f:
        trades = json.load(f)
    for trade in trades:
        if trade["bought"] is not None:
            profit_dict["matecoin_account"] += Decimal(trade["bought"])
            profit_dict["earned_money"] -= (
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            )
        if trade["sold"] is not None:
            profit_dict["earned_money"] += (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            )
            profit_dict["matecoin_account"] -= Decimal(trade["sold"])

    with open("profit.json", "w") as p:
        json.dump(
            {
                key: str(value) for key, value in profit_dict.items()
            }, p, indent=2
        )
