import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            amount = Decimal(trade["bought"])
            earned_money -= amount * price
            matecoin_account += amount
        elif trade["sold"]:
            amount = Decimal(trade["sold"])
            earned_money += amount * price
            matecoin_account -= amount

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f)
