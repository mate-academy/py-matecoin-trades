import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades = json.load(f)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trades:
        bought = Decimal(trade["bought"] if trade["bought"] else Decimal("0"))
        sold = Decimal(trade["sold"] if trade["sold"] else Decimal("0"))
        price = Decimal(trade["matecoin_price"])

        earned_money -= bought * price
        matecoin_account += bought

        earned_money += sold * price
        matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
