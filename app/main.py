import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"]:
            bought_volume = Decimal(trade["bought"])
            earned_money -= bought_volume * price
            matecoin_account += bought_volume

        if trade["sold"]:
            sold_volume = Decimal(trade["sold"])
            earned_money += sold_volume * price
            matecoin_account -= sold_volume

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
