import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    total_bought = 0
    total_bought_price = 0
    total_sold = 0
    total_sold_price = 0

    for trade in trades:
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            total_bought += bought
            total_bought_price += bought * price

        if trade["sold"]:
            sold = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            total_sold += sold
            total_sold_price += sold * price

    currently_profit = str(total_sold_price - total_bought_price)
    currently_balance = str(total_bought - total_sold)

    profit = {"earned_money": currently_profit,
              "matecoin_account": currently_balance}

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
