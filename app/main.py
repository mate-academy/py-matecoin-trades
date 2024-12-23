import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open("C:\\Users\\arise\\py-matecoin-trades\\app\\trades.json", "r") as file:
        trades = json.load(file)
    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in trades:
        bought = Decimal(trade["bought"]) \
            if trade["bought"] is not None else Decimal("0.0")

        sold = Decimal(trade["sold"]) \
            if trade["sold"] is not None else Decimal("0.0")

        matecoin_price = Decimal(trade["matecoin_price"])

        earned_money += sold * matecoin_price
        earned_money -= bought * matecoin_price
        matecoin_account += bought
        matecoin_account -= sold

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=2)
