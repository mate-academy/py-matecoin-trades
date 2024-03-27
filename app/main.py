import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as trades_file:
        trades_description = json.load(trades_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_description:
        if trade["bought"]:
            matecoin_account += Decimal(trade["bought"])
            earned_money -= (
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            )
        if trade["sold"]:
            matecoin_account -= Decimal(trade["sold"])
            earned_money += (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            )

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
