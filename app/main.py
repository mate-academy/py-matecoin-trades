import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    wallet = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            earned_money -= amount * price
            wallet += amount

        if trade["sold"] is not None:
            amount = Decimal(trade["sold"])
            earned_money += amount * price
            wallet -= amount

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(wallet)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
