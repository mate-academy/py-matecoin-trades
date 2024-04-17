import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as trades_file:
        trades = json.load(trades_file)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])

        if trade["bought"]:
            bought_amount = Decimal(trade["bought"])
            cost = bought_amount * matecoin_price
            matecoin_account += bought_amount
            earned_money -= cost

        if trade["sold"]:
            sold_amount = Decimal(trade["sold"])
            income = sold_amount * matecoin_price
            matecoin_account -= sold_amount
            earned_money += income

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as profit_file:
        json.dump(result, profit_file, indent=2)
