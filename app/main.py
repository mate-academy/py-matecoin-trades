import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    total_earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in trades:
        if trade["bought"] is not None:
            bought_amount = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            matecoin_account += bought_amount
            total_earned_money -= bought_amount * matecoin_price
        elif trade["sold"] is not None:
            sold_amount = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            matecoin_account -= sold_amount
            total_earned_money += sold_amount * matecoin_price

    profit_data = {
        "earned_money": str(total_earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit_data, file)
