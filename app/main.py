import json

from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        matecoin_value = json.load(file)

    matecoin_account = 0
    earned_money = 0

    for key in matecoin_value:
        bought = key["bought"]
        sold = key["sold"]
        price = Decimal(key["matecoin_price"])

        if key["bought"]:
            earned_money -= Decimal(bought) * price
            matecoin_account += Decimal(bought)

        if key["sold"]:
            matecoin_account -= Decimal(sold)
            earned_money += Decimal(sold) * price

        profit_json = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        with open("profit.json", "w") as file:
            json.dump(profit_json, file, indent=2)
