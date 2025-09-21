import json
from decimal import Decimal


def calculate_profit(trades_file: list) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with open(trades_file, "r") as json_file:
        data = json.load(json_file)
        for trade in data:
            bought = Decimal(trade["bought"]) if trade["bought"] else None
            sold = Decimal(trade["sold"]) if trade["sold"] else None
            price = Decimal(trade["matecoin_price"])

            if bought:
                matecoin_account += bought
            if sold:
                earned_money += sold * price
                matecoin_account -= sold

    with open("profit.json", "w") as profit_file:
        json.dump({
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)}, profit_file, indent=5)
