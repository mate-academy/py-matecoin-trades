import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade["bought"]:
            earned_money -= (
                Decimal(trade["matecoin_price"]) * Decimal(trade["bought"])
            )
            matecoin_account += Decimal(trade["bought"])

        if trade["sold"]:
            earned_money += (
                Decimal(trade["matecoin_price"]) * Decimal(trade["sold"])
            )
            matecoin_account -= Decimal(trade["sold"])
    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as jsonfile:
        json.dump(profit_data, jsonfile, indent=2)
