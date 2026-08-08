import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        trades = json.load(f)

    cost = Decimal("0.0")
    revenue = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in trades:
        if trade["bought"]:
            price = Decimal(trade["matecoin_price"])
            bought = Decimal(trade["bought"])
            cost += bought * price
            matecoin_account += bought

        if trade["sold"]:
            price = Decimal(trade["matecoin_price"])
            sold = Decimal(trade["sold"])
            revenue += sold * price
            matecoin_account -= sold

    profit = revenue - cost

    result = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
