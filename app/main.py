import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    print(trades)

    profit = Decimal("0")
    coins = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            coins += amount
            profit -= amount * price

        if trade["sold"] is not None:
            amount = Decimal(trade["sold"])
            coins -= amount
            profit += amount * price

    result = {
        "earned_money": str(profit),
        "matecoin_account": str(coins),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
