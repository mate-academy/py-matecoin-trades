import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as f:
        trades_data = json.load(f)

    total_earned_money = Decimal("0")
    total_matecoin_account = Decimal("0")

    for trade in trades_data:
        if trade.get("bought"):
            total_earned_money -= (
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            )
            total_matecoin_account += Decimal(trade["bought"])
        if trade.get("sold"):
            total_earned_money += (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            )
            total_matecoin_account -= Decimal(trade["sold"])

    profit_data = {
        "earned_money": str(total_earned_money),
        "matecoin_account": str(total_matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(profit_data, f, indent=2)
