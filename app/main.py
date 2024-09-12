import json
from decimal import Decimal


def calculate_profit(file):
    earned_money = 0
    matecoin_account = 0
    with open(file) as f:
        json_content = json.load(f)
    for transaction in json_content:
        price = Decimal(transaction["matecoin_price"])
        if transaction["bought"]:
            matecoin_account += Decimal(transaction["bought"])
            earned_money -= Decimal(transaction["bought"]) * price
        if transaction["sold"]:
            matecoin_account -= Decimal(transaction["sold"])
            earned_money += Decimal(transaction["sold"]) * price
    profit = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as f:
        json.dump(profit, f)
