import json
from decimal import Decimal
import os


def calculate_profit(file_data: str) -> None:
    with open(os.path.join(file_data), "r") as f:
        trades = json.load(f)

    trade_data = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    for trade in trades:
        if trade["bought"]:
            trade_data["earned_money"] -= (
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            )
            trade_data["matecoin_account"] += Decimal(trade["bought"])
        if trade["sold"]:
            trade_data["earned_money"] += (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            )
            trade_data["matecoin_account"] -= Decimal(trade["sold"])

    trade_data = {
        "earned_money": str(trade_data["earned_money"]),
        "matecoin_account": str(trade_data["matecoin_account"]),
    }

    with open("profit.json", "w") as profit:
        json.dump(trade_data, profit, indent=2)