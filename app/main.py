import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(trades_file, "r") as file_in:
        trades = json.load(file_in)

        for trade in trades:
            if trade["bought"]:
                earned_money -= (
                    Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
                )
                matecoin_account += Decimal(trade["bought"])
            if trade["sold"]:
                earned_money += (
                    Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
                )
                matecoin_account -= Decimal(trade["sold"])

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file_out:
        json.dump(profit, file_out, indent=2)
