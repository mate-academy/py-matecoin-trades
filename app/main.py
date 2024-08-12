import json
from decimal import Decimal, getcontext


getcontext().prec = 10


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in trades:
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            matecoin_account += bought
            earned_money -= bought * price
        if trade["sold"]:
            sold = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            matecoin_account -= sold
            earned_money += sold * price

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
