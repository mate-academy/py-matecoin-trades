import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    expenses = {
        "bought": Decimal("0"),
        "sold": Decimal("0"),
        "matecoin_account": Decimal("0")
    }
    for trade in trades:
        if trade["bought"] is not None:
            expenses["bought"] \
                += Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            expenses["matecoin_account"] += Decimal(trade["bought"])
        if trade["sold"] is not None:
            expenses["sold"] \
                += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            expenses["matecoin_account"] -= Decimal(trade["sold"])

    earned_money = str(expenses["sold"] - expenses["bought"])
    matecoin_account = str(expenses["matecoin_account"])

    profit = {
        "earned_money": earned_money,
        "matecoin_account": matecoin_account
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
