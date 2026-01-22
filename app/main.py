import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    with open(name_file, "r") as file:
        for transaction in json.load(file):
            price = Decimal(transaction["matecoin_price"])
            if volume_of_coins := transaction.get("bought"):
                matecoin_account += Decimal(volume_of_coins)
                earned_money -= Decimal(volume_of_coins) * price
            if volume_of_coins := transaction.get("sold"):
                matecoin_account -= Decimal(volume_of_coins)
                earned_money += Decimal(volume_of_coins) * price

    date_profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(date_profit, file, indent=2)
