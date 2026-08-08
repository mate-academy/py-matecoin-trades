# write your code here
from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trade = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for deal in trade:
        if deal["bought"]:
            bought = Decimal(deal["bought"])
        else:
            bought = Decimal("0")
        if deal["sold"]:
            sold = Decimal(deal["sold"])
        else:
            sold = Decimal("0")
        matecoin_price = Decimal(deal["matecoin_price"])

        matecoin_account += bought
        matecoin_account -= sold

        earned_money -= bought * matecoin_price
        earned_money += sold * matecoin_price

        profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as f:
            json.dump(profit, f, indent=2)
