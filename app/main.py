import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    money = 0
    coins = 0

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            money -= price * bought
            coins += bought

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            money += price * sold
            coins -= sold

    result = {
        "earned_money": str(money),
        "matecoin_account": str(coins)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
