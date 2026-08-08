import json
from decimal import Decimal


def calculate_profit(file_name):
    with open(file_name, 'r') as f:
        transactions = json.load(f)
        earned_money = Decimal()
        matecoin_account = Decimal()
        for transaction in transactions:
            price = Decimal(transaction["matecoin_price"])
            if transaction["bought"]:
                matecoin_account += Decimal(transaction["bought"])
                earned_money -= Decimal(transaction["bought"]) * price
            if transaction["sold"]:
                matecoin_account -= Decimal(transaction["sold"])
                earned_money += Decimal(transaction["sold"]) * price

    result = {
        "earned_money": earned_money,
        "matecoin_account": matecoin_account
    }
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
