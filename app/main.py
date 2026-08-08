from decimal import Decimal
import json


def calculate_profit(file_name):
    income_money = 0
    coin_counter = 0

    with open(file_name) as f:
        buyers = json.load(f)

    for buyer in buyers:
        price = Decimal(buyer["matecoin_price"])
        if buyer["bought"]:
            income_money -= Decimal(buyer["bought"]) * price
            coin_counter += Decimal(buyer["bought"])
        if buyer["sold"]:
            income_money += Decimal(buyer["sold"]) * price
            coin_counter -= Decimal(buyer["sold"])

    add_profit = {"earned_money": f'{income_money}',
                  "matecoin_account": f'{coin_counter}'}
    with open("profit.json", "w") as f:
        json.dump(add_profit, f, indent=2)
