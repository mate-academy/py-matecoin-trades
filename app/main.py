import json
from decimal import Decimal


def calculate_profit(file_name: str = "trades.json") -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)
        profit = {
            "earned_money": "0",
            "matecoin_account": "0"
        }
        for trade in trades:
            if trade["bought"]:
                profit["earned_money"] = str(
                    Decimal(profit["earned_money"])
                    - Decimal(trade["bought"])
                    * Decimal(trade["matecoin_price"])
                )
                profit["matecoin_account"] = str(
                    Decimal(profit["matecoin_account"])
                    + Decimal(trade["bought"])
                )
            if trade["sold"]:
                profit["earned_money"] = str(
                    Decimal(profit["earned_money"])
                    + Decimal(trade["sold"])
                    * Decimal(trade["matecoin_price"])
                )
                profit["matecoin_account"] = str(
                    Decimal(profit["matecoin_account"])
                    - Decimal(trade["sold"])
                )
    with open("profit.json", "w") as file_profit:
        json.dump(profit, file_profit, indent=2)
