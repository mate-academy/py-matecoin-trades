import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    with open(file_path, "r") as file:
        data = json.load(file)
    total_revenue = Decimal("0")
    total_expenses = Decimal("0")
    total_account = Decimal("0")
    for trade in data:
        if trade.get("bought"):
            total_expenses += (
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            )
            total_account += Decimal(trade["bought"])
        if trade.get("sold"):
            total_revenue += (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            )
            total_account -= Decimal(trade["sold"])
    profit = {
        "earned_money": str(total_revenue - total_expenses),
        "matecoin_account": str(total_account)
    }
    with open("profit.json", "w") as file_jsn:
        json.dump(profit, file_jsn, indent=2)
