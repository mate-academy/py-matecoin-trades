import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    with open(file_name, "r") as trades_file:
        trades = json.load(trades_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:

        coin_price = Decimal(trade["matecoin_price"])

        if trade.get("bought"):
            coin_bought = Decimal(trade["bought"])
            matecoin_account += coin_bought
            earned_money -= coin_bought * coin_price

        if trade.get("sold"):
            coin_sold = Decimal(trade["sold"])
            matecoin_account -= coin_sold
            earned_money += coin_sold * coin_price

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
