import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        data = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in data:
        coin_bought = Decimal("0")
        coin_sold = Decimal("0")
        expenses = Decimal("0")
        revenue = Decimal("0")
        matecoin_price = Decimal(trade["matecoin_price"])

        if trade["bought"]:
            coin_bought += Decimal(trade["bought"])
            expenses += (Decimal(trade["bought"]) * matecoin_price)

        if trade["sold"]:
            coin_sold += Decimal(trade["sold"])
            revenue += (Decimal(trade["sold"]) * matecoin_price)

        matecoin_account += coin_bought - coin_sold
        earned_money += revenue - expenses

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
