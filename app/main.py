import json
from decimal import Decimal


def calculate_profit(name: str) -> None:
    with open(name) as f:
        trades = json.load(f)

    total_bought_money = 0
    total_sold_money = 0
    total_sold = 0
    total_bought = 0
    for trade in trades:
        if trade.get("bought"):
            total_bought_money += (
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"]))
            total_bought += Decimal(trade["bought"])
        if trade.get("sold"):
            total_sold_money += (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"]))
            total_sold += Decimal(trade["sold"])

    with open("profit.json", "w") as f:
        json.dump(
            {"earned_money": str(total_sold_money - total_bought_money),
             "matecoin_account": str(total_bought - total_sold)},
            f, indent=2)
