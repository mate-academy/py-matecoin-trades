import json
from decimal import Decimal


def calculate_profit(trades_filename: str) -> None:
    with open(trades_filename, "r") as file:
        trades = json.load(file)

    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    for trade in trades:
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        price = Decimal(trade["matecoin_price"])

        matecoin_account += bought
        matecoin_account -= sold
        earned_money += sold * price
        earned_money -= bought * price

    result = {
        "earned_money": format(earned_money, "f"),
        "matecoin_account": format(matecoin_account, "f")
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=4)
