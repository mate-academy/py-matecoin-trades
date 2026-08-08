import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades = json.load(f)

    matecoin_account = 0
    earned_money = 0

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"]:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * price

        if trade["sold"]:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * price

    profit_data = {
        "earned_money": f"{earned_money:.7f}",
        "matecoin_account": f"{matecoin_account:.5f}"
    }

    with open("profit.json", "w") as f:
        json.dump(profit_data, f, indent=2)
