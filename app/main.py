from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(str(trade["matecoin_price"]))

        if trade["bought"] is not None:
            bought_amount = Decimal(str(trade["bought"]))
            earned_money -= bought_amount * price
            matecoin_account += bought_amount

        if trade["sold"] is not None:
            sold_amount = Decimal(str(trade["sold"]))
            earned_money += sold_amount * price
            matecoin_account -= sold_amount

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
