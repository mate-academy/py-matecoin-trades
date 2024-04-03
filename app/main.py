import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades = json.load(f)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            earned_money -= bought * matecoin_price
            matecoin_account += bought
        if trade["sold"]:
            sold = Decimal(trade["sold"])
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
