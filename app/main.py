import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    total_bought = Decimal("0")
    total_sold = Decimal("0")
    spent_money = Decimal("0")
    received_money = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            total_bought += amount
            spent_money += amount * price

        if trade["sold"] is not None:
            amount = Decimal(trade["sold"])
            total_sold += amount
            received_money += amount * price

    result = {
        "earned_money": str(received_money - spent_money),
        "matecoin_account": str(total_bought - total_sold),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
