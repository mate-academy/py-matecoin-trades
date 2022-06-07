import json
from decimal import Decimal


def calculate_profit(file_name):
    with open(file_name) as f:
        data = json.load(f)
    total_bought_cost = 0
    total_sold_cost = 0
    total_bought_coins = 0
    total_sold_coins = 0
    for trade in data:
        if trade["bought"]:
            total_bought_coins += Decimal(trade["bought"])
            bought = \
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            total_bought_cost += bought
        if trade["sold"]:
            total_sold_coins += Decimal(trade["sold"])
            sold = Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            total_sold_cost += sold
    profit = total_bought_cost - total_sold_cost
    total_coins = total_bought_coins - total_sold_coins
    result = {
        "earned_money": str(profit),
        "matecoin_account": str(total_coins)
    }
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
