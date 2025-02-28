import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    matecoin_account = Decimal("0.0")
    earned_money = Decimal("0.0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"]:
            bought_amount = Decimal(trade["bought"])
            matecoin_account += bought_amount
            earned_money -= bought_amount * price

        if trade["sold"]:
            sold_amount = Decimal(trade["sold"])
            matecoin_account -= sold_amount
            earned_money += sold_amount * price

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=2)
