import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(file_name) as file:
        trades = json.load(file)

        for trade in trades:
            price = Decimal(trade["matecoin_price"])
            bought = Decimal(trade["bought"]) if trade["bought"] else None
            sold = Decimal(trade["sold"]) if trade["sold"] else None

            if bought:
                earned_money -= bought * price
                matecoin_account += bought

            if sold:
                earned_money += sold * price
                matecoin_account -= sold

    with open("profit.json", "w") as file:
        json.dump({
            "earned_money": format(earned_money, "f"),
            "matecoin_account": format(matecoin_account, "f")},
            file, indent=2
        )
