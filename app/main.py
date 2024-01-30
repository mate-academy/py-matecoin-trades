from decimal import Decimal
import json
import os


def calculate_profit(trades: str) -> None:
    with (open(trades, "r") as source_file):
        operations = json.load(source_file)

    earned_money = 0
    account = 0
    for trade in operations:
        currency = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            earned_money -= Decimal(trade["bought"]) * currency
            account += Decimal(trade["bought"])
        if trade["sold"]:
            earned_money += Decimal(trade["sold"]) * currency
            account -= Decimal(trade["sold"])
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(account)
    }

    parent_path = os.path.dirname(os.getcwd())
    result_path = os.path.join(parent_path, "profit.json")

    with open(result_path, "w") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
