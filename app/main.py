import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    total_money = Decimal("0")
    total_coins = Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            total_money -= (
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            )
            total_coins += Decimal(trade["bought"])

        if trade["sold"] is not None:
            total_money += (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            )
            total_coins -= Decimal(trade["sold"])

    profit_data = {
        "earned_money": str(total_money),
        "matecoin_account": str(total_coins)
    }

    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=2)
