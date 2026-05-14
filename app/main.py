import json
from decimal import Decimal


def calculate_profit(filename: str):
    with open(filename, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        bought = Decimal(trade["bought"]) if trade["bought"] is not None else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] is not None else Decimal("0")

        if bought:
            earned_money -= price * bought
            matecoin_account += bought

        if sold:
            earned_money += price * sold
            matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)

    return None