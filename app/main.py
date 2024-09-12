import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    matecoin_account, earned_money = 0, 0

    for trade in trades:
        if trade.get("bought"):
            bought = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            earned_money -= bought * matecoin_price
            matecoin_account += bought
        if trade.get("sold"):
            sold = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    profit = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as write_f:
        json.dump(profit, write_f, indent=2)
