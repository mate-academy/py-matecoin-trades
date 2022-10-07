import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:

    profit = 0
    balance = 0

    with open(filename, "r") as f:
        date_coins = json.load(f)

    for transaction in date_coins:
        price = Decimal(transaction["matecoin_price"])

        if transaction["sold"]:
            profit += Decimal(transaction["sold"]) * price
            balance -= Decimal(transaction["sold"])
        if transaction["bought"]:
            profit -= Decimal(transaction["bought"]) * price
            balance += Decimal(transaction["bought"])

    output = {
        "earned_money": str(profit),
        "matecoin_account": str(balance)
    }

    with open("profit.json", "w") as output_file:
        json.dump(output, output_file, indent=2)
