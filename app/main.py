import json
from decimal import Decimal


def calculate_profit(name_of_file: str):
    with open(name_of_file, "r") as f:

        mate_coin_account = Decimal("0")
        earned_money = Decimal("0")

        transactions = json.load(f)

        for transaction in transactions:

            price = Decimal(transaction["mate_coin_price"])

            if transaction["bought"]:

                bought = Decimal(transaction["bought"])

                mate_coin_account += bought
                earned_money -= bought * price
            else:

                sold = Decimal(transaction["sold"])

                mate_coin_account -= sold
                earned_money += sold * price

        profit = {"earned_money": f"{earned_money}",
                  "mate_coin_account": f"{mate_coin_account}"}

        with open("profit.json", "w") as p:
            json.dump([profit], p, indent=2)
