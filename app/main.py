import json

from decimal import Decimal


def calculate_profit(file_path: str) -> None:

    with open(file_path, "r") as info:
        trades_data = json.load(info)

    balance = Decimal()
    coins = Decimal()

    for trade in trades_data:
        price = Decimal(trade["matecoin_price"])
        bought = trade["bought"]
        sold = trade["sold"]
        if bought:
            balance -= Decimal(bought) * price
            coins += Decimal(bought)
        if sold:
            balance += Decimal(sold) * price
            coins -= Decimal(sold)

    profit = {
        "earned_money": str(balance),
        "matecoin_account": str(coins)
    }
    with open("profit.json", "w") as report:
        json.dump(profit, report, indent=2)
