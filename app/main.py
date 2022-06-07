import json

from decimal import Decimal


def calculate_profit(file_name: str):
    with open(file_name) as file:
        trades_data = json.load(file)

    bought_in_dollars = 0
    sold_in_dollars = 0
    coins_bougth = 0
    coins_sold = 0

    for trade in trades_data:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            bought_in_dollars += Decimal(trade["bought"]) * price
            coins_bougth += Decimal(trade["bought"])
        elif trade["sold"]:
            sold_in_dollars += Decimal(trade["sold"]) * price
            coins_sold += Decimal(trade["sold"])

    profit = sold_in_dollars - bought_in_dollars
    coins = coins_bougth - coins_sold

    profit_dict = {
        "earned_money": str(profit),
        "matecoin_account": str(coins)
    }

    with open("profit.json", "w") as f1:
        json.dump(profit_dict, f1, indent=2)
