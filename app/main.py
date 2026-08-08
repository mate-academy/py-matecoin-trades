import json
from decimal import Decimal


def calculate_profit(name_of_file: str) -> None:
    with open(name_of_file, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * price

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * price

    with open("profit.json", "w") as new_file:
        json.dump({
            "earned_money": str(earned_money.normalize()),
            "matecoin_account": str(matecoin_account.normalize())
        }, new_file, indent=2)
