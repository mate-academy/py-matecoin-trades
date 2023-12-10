import os
import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        data = json.load(file)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for transaction in data:
        try:

            if transaction["bought"]:
                bought_coins = Decimal(transaction["bought"])
                price = Decimal(transaction["matecoin_price"])
                earned_money -= bought_coins * price
                matecoin_account += bought_coins

            if transaction["sold"]:
                sold_coins = Decimal(transaction["sold"])
                price = Decimal(transaction["matecoin_price"])
                earned_money += sold_coins * price
                matecoin_account -= sold_coins

        except KeyError:
            continue

    profit = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}

    with open(os.path.join("../profit.json"), "w") as dump_file:
        json.dump(profit, dump_file, indent=2)
