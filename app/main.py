import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        matecoin_value = json.load(f)

    earned_money = 0
    matecoin_account = 0

    for token in matecoin_value:
        bought = token["bought"]
        sold = token["sold"]
        price = Decimal(token["matecoin_price"])

        if token["bought"]:
            earned_money -= Decimal(bought) * price
            matecoin_account += Decimal(bought)

        if token["sold"]:
            earned_money += Decimal(sold) * price
            matecoin_account -= Decimal(sold)

        profit_json = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as f:
            json.dump(profit_json, f, indent=2)
