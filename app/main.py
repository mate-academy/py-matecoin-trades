from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    trades = {}
    profits = {"earned_money": "0", "matecoin_account": "0"}
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with open(filename, "r") as file:
        trades = json.load(file)
    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            earned_money -= price * bought
            matecoin_account += bought
        if trade["sold"]:
            sold = Decimal(trade["sold"])
            earned_money += price * sold
            matecoin_account -= sold
    profits["earned_money"] = str(earned_money)
    profits["matecoin_account"] = str(matecoin_account)

    with open("profit.json", "w") as file:
        json.dump(profits, file, indent=2)
