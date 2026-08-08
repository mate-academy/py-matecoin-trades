import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        bought = trade["bought"]
        sold = trade["sold"]

        if bought is not None:
            bought_amount = Decimal(bought)
            earned_money -= bought_amount * price
            matecoin_account += bought_amount

        if sold is not None:
            sold_amount = Decimal(sold)
            earned_money += sold_amount * price
            matecoin_account -= sold_amount

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
