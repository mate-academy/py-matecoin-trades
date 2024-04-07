import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        trades = json.load(file)

    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    for trade in trades:
        bought = trade["bought"]
        sold = trade["sold"]
        matecoin_price = Decimal(trade["matecoin_price"])

        if bought:
            bought = Decimal(bought)
            matecoin_account += bought
            earned_money -= bought * matecoin_price
        if sold:
            sold = Decimal((sold))
            matecoin_account -= sold
            earned_money += sold * matecoin_price

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
