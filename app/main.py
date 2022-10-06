import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as json_trades:
        data = json.load(json_trades)

    earned_money = 0
    matecoin_account = 0

    for operation in data:
        bought = operation["bought"]
        sold = operation["sold"]
        price = Decimal(operation["matecoin_price"])

        if operation["bought"]:
            earned_money -= Decimal(bought) * price
            matecoin_account += Decimal(bought)

        if operation["sold"]:
            earned_money += Decimal(sold) * price
            matecoin_account -= Decimal(sold)

        profit_dict = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as json_profit:
            json.dump(profit_dict, json_profit, indent=2)
