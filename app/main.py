import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    money = Decimal("0")
    coins = Decimal("0")

    with open(file_name) as f:
        data = json.load(f)

    for trade in data:

        price = Decimal(trade["matecoin_price"])

        if trade["bought"]:
            money -= Decimal(trade["bought"]) * price
            coins += Decimal(trade["bought"])
        if trade["sold"]:
            money += Decimal(trade["sold"]) * price
            coins -= Decimal(trade["sold"])

    profit = {
        "earned_money": str(money),
        "matecoin_account": str(coins)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
