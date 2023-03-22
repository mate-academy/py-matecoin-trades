import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as source:
        trades = json.load(source)

    earned_money = Decimal("0.00")
    matecoin_account = Decimal("0.00")

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])
        if trade.get("bought"):
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * matecoin_price

        if trade.get("sold"):
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * matecoin_price

    profit = {
        "earned_money": f"{earned_money}",
        "matecoin_account": f"{matecoin_account}"
    }

    with open("profit.json", "w") as output:
        json.dump(profit, output, indent=2)
