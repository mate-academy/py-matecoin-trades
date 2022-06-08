import json
from decimal import Decimal


def calculate_profit(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
    total_bought_cost = 0
    total_sold_cost = 0
    amount_of_bought_coins = 0
    amount_of_sold_coins = 0
    for trade in data:
        if trade["bought"]:
            amount_of_bought_coins += Decimal(trade["bought"])
            bought = \
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            total_bought_cost += bought
        if trade["sold"]:
            amount_of_sold_coins += Decimal(trade["sold"])
            sold = Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            total_sold_cost += sold
    profit = total_bought_cost - total_sold_cost
    total_coins = amount_of_bought_coins - amount_of_sold_coins
    result = {
        "earned_money": str(profit),
        "matecoin_account": str(total_coins)
    }
    with open("profit.json", "w") as json_outcome_file:
        json.dump(result, json_outcome_file, indent=2)
