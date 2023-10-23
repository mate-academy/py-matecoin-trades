import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    with (open(file_name) as json_file):
        py_file = json.load(json_file)

        profit = 0
        coin = 0
        result = []

        for trade in py_file:

            price = Decimal(trade["matecoin_price"])

            if trade.get("bought"):
                bought = Decimal(trade.get("bought"))
                profit -= bought * price
                coin += bought

            if trade.get("sold"):
                sold = Decimal(trade.get("sold"))
                profit += sold * price
                coin -= sold

            temp = {"earned_money": str(profit),
                    "matecoin_account": str(coin)}

            result.append(temp)

    with open("profit.json", "w") as file_json:
        json.dump(temp, file_json, indent=2)
