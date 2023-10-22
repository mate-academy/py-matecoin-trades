import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    profit_data = {
        "matecoin_account" : Decimal(0),
        "total_bought" : Decimal(0),
        "total_sold" : Decimal(0)
    }

    with open(file_name, "r") as file:
        trade_data = json.load(file)

    for trade in trade_data:
        if trade.get("bought"):
            profit_data["matecoin_account"] += Decimal(trade["bought"])
            profit_data["total_bought"] += (
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            )
        if trade.get("sold"):
            profit_data["matecoin_account"] -= Decimal(trade["sold"])
            profit_data["total_sold"] += (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            )
    total_earned = profit_data["total_sold"] - profit_data["total_bought"]
    profit = {
        "earned_money" : str(total_earned),
        "matecoin_account" : str(profit_data["matecoin_account"])
    }

    with open("profit.json", "w") as file_out:
        json.dump(profit, file_out, indent=2)
