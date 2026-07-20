from decimal import Decimal
import json
import os


def calculate_profit(trades_file_name: str) -> None:
    if os.path.exists(trades_file_name):
        with open(trades_file_name, "r") as source:
            trades = json.load(source)

        earned_money = Decimal("0")
        matecoin_account = Decimal("0")

        for transaction in trades:
            if transaction["bought"]:
                earned_money -= Decimal(transaction["bought"]) * Decimal(
                    transaction["matecoin_price"]
                )
                matecoin_account += Decimal(transaction["bought"])
            if transaction["sold"]:
                earned_money += Decimal(transaction["sold"]) * Decimal(
                    transaction["matecoin_price"]
                )
                matecoin_account -= Decimal(transaction["sold"])

        profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        }
        with open("profit.json", "w") as target:
            json.dump(profit, target, indent=2)
