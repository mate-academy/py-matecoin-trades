import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades = json.load(f)

    money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought_amount = Decimal(trade["bought"])
            matecoin_account += bought_amount
            money -= bought_amount * price

        if trade["sold"] is not None:
            sold_amount = Decimal(trade["sold"])
            matecoin_account -= sold_amount
            money += sold_amount * price

    result = {
        "earned_money": str(money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)

    return None
