import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        value = Decimal(0)

        bought = trade["bought"]
        sold = trade["sold"]

        if bought:
            value += Decimal(bought)

        if sold:
            value -= Decimal(sold)

        earned_money -= value * price
        matecoin_account += value

    profit_json = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit_json, file, indent=2)
