import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    with open(file_path, "r") as trades_file:
        data = json.load(trades_file)

    account = Decimal("0")
    profit = Decimal("0")

    for trade in data:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought_amount = Decimal(trade["bought"])
            account += bought_amount
            profit -= bought_amount * price

        if trade["sold"] is not None:
            sold_amount = Decimal(trade["sold"])
            account -= sold_amount
            profit += sold_amount * price

    profits = {
        "earned_money": str(profit),
        "matecoin_account": str(account)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profits, profit_file, indent=2)
