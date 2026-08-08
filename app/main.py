import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    total_bought = Decimal("0")
    total_sold = Decimal("0")
    total_spent = Decimal("0")
    total_earned = Decimal("0")

    with open(file_name, "r") as file:
        trades = json.load(file)  # Correctly load JSON data

    for trade in trades:
        if trade.get("bought"):
            bought_amount = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            total_bought += bought_amount
            total_spent += bought_amount * price
        if trade.get("sold"):
            sold_amount = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            total_sold += sold_amount
            total_earned += sold_amount * price

    earned_money = total_earned - total_spent
    matecoin_account = total_bought - total_sold

    profit_m = {
        "earned_money": f"{earned_money}",
        "matecoin_account": f"{matecoin_account}"
    }

    with open("profit.json", "w") as f:
        json.dump(profit_m, f, indent=2)
