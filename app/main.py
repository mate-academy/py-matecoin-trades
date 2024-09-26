from decimal import Decimal
import json


def calculate_profit(name_file: str) -> None:
    money = 0
    coins = 0

    with open(name_file, "r") as f:
        trades_data = json.load(f)

    for trade in trades_data:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            coins += Decimal(trade["bought"])
            money -= Decimal(trade["bought"]) * price
        if trade["sold"]:
            coins -= Decimal(trade["sold"])
            money += Decimal(trade["sold"]) * price

    result = {
        "earned_money": str(money),
        "matecoin_account": str(coins)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
