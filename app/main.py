import json
import os
from decimal import Decimal


def calculate_profit(trades_file_name: str) -> None:
    with open(trades_file_name, "r") as f:
        trades_of_data = json.load(f)
    amount = Decimal("0.0")
    matecoin_coint = Decimal("0.0")

    for trade in trades_of_data:
        if trade["bought"]:
            matecoin_coint += Decimal(trade["bought"])
            amount -= (Decimal(trade["bought"])
                       * Decimal(trade["matecoin_price"]))

        if trade["sold"]:
            matecoin_coint -= Decimal(trade["sold"])
            amount += (Decimal(trade["sold"])
                       * Decimal(trade["matecoin_price"]))
    profit_path = os.path.join(os.getcwd(), "profit.json")

    with open(profit_path, "w") as file_profit:
        json.dump({
            "earned_money": str(amount),
            "matecoin_account": str(matecoin_coint)
        }, file_profit, indent=2)
