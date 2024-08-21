import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        trades = json.load(file)

    total_cost = Decimal("0.0")
    total_revenue = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in trades:
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            total_cost += bought * price
            matecoin_account += bought
        if trade["sold"]:
            sold = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            total_revenue += sold * price
            matecoin_account -= sold

    profit = total_revenue - total_cost

    profit_data = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=2)
