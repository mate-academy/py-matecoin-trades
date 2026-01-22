from decimal import Decimal

import json


def calculate_profit(name: str) -> None:
    with open(name, "r") as file:
        trades = json.load(file)

        earned_money = Decimal("0")
        matecoin_account = Decimal("0")

        for trade in trades:
            matecoin_price = Decimal(trade["matecoin_price"])
            if trade["bought"] is not None:
                bought = Decimal(trade["bought"])
                earned_money -= bought * matecoin_price
                matecoin_account += bought

            if trade["sold"] is not None:
                sold = Decimal(trade["sold"])
                earned_money += sold * matecoin_price
                matecoin_account -= sold

        profit = {"earned_money": f"{earned_money}",
                  "matecoin_account": f"{matecoin_account}"}

        print(profit)

        with open("profit.json", "w") as file2:
            json.dump(profit, file2, indent=2)
