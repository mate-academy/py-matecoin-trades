import json
from decimal import Decimal


def calculate_profit(file_name: str):
    with open(file_name) as file:
        file_content = json.load(file)

    money_total = 0
    coins_left = 0

    for transaction in file_content:
        price = Decimal(transaction["matecoin_price"])

        if transaction["bought"]:
            money_total -= Decimal(transaction["bought"]) * price
            coins_left += Decimal(transaction["bought"])
        else:
            money_total += Decimal(transaction["sold"]) * price
            coins_left -= Decimal(transaction["sold"])

    dict_to_dump = {
        "earned_money": str(money_total),
        "matecoin_account": str(coins_left)
    }

    with open("profit.json", "w") as file_to_write:
        json.dump(dict_to_dump, file_to_write, indent=2)
