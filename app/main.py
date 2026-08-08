import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(f"{file_name}", "r") as f:
        trades = json.load(f)
    coins = 0
    revenue = 0
    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            expenses = bought * matecoin_price
            coins += bought
            revenue -= expenses
        if trade["sold"]:
            sold = Decimal(trade["sold"])
            profit = sold * matecoin_price
            coins -= sold
            revenue += profit
    result = {"earned_money": str(revenue), "matecoin_account": str(coins)}
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
