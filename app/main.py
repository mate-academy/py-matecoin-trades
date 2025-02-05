import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    for trade in trades:
        if trade["bought"]:
            bought_volume = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            matecoin_account += bought_volume
            earned_money -= bought_volume * price

        if trade["sold"]:
            sold_volume = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            matecoin_account -= sold_volume
            earned_money += sold_volume * price

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=2)
