import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    earned_money_balance = 0
    matecoin_balance = 0

    with open(file_path, "r") as file:
        trades = json.load(file)

    for trade in trades:
        if trade["bought"]:
            earned_money_balance -= (
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            )
            matecoin_balance += Decimal(trade["bought"])

        if trade["sold"]:
            earned_money_balance += (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            )
            matecoin_balance -= Decimal(trade["sold"])

    result_balance = {
        "earned_money": str(earned_money_balance),
        "matecoin_account": str(matecoin_balance)
    }

    with open("profit.json", "w") as file:
        json.dump(result_balance, file, indent=2)
