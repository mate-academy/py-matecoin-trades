import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    matecoin_account = Decimal("0.0")
    earned_money = Decimal("0.0")

    for trade in trades:
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            matecoin_account += bought
            earned_money -= bought * matecoin_price

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    with open("profit.json", "w") as profit_json:
        done_data = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        json.dump(done_data, profit_json, indent=2)
