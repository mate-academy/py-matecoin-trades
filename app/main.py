import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with open(file_name, "r") as f:
        trade_view = json.load(f)

        for trade in trade_view:
            bought = Decimal(trade["bought"]) if trade["bought"] \
                else Decimal("0")
            sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
            price = Decimal(trade["matecoin_price"])

            matecoin_account += bought
            matecoin_account -= sold

            earned_money -= bought * price
            earned_money += sold * price

        profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
