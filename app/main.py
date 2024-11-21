import json

from decimal import Decimal


def calculate_profit(file):
    with open(file) as f:
        python_data = json.load(f)

    money_profit = 0
    coin_account = 0

    for transaction in python_data:
        price = Decimal(transaction["matecoin_price"])

        if transaction["bought"]:
            coin_account += Decimal(transaction["bought"])
            money_profit -= Decimal(transaction["bought"]) * price

        if transaction["sold"]:
            coin_account -= Decimal(transaction["sold"])
            money_profit += Decimal(transaction["sold"]) * price

    with open("profit.json", "w") as result_file:
        json.dump(
            {"money_profit": str(money_profit),
             "coin_account": str(coin_account)},
            result_file,
            indent=2
        )
