from decimal import Decimal
import json


def calculate_profit(file_name):
    with open(file_name, 'r') as f:
        transactions = json.load(f)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for transaction in transactions:
        matecoin_price = Decimal(transaction["matecoin_price"])

        if transaction["bought"]:
            bought = Decimal(transaction["bought"])
            earned_money -= bought * matecoin_price
            matecoin_account += bought
        else:
            sold = Decimal(transaction["sold"])
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open('profit.json', 'w') as json_file:
        json.dump(profit, json_file, indent=2)
