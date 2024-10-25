import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    dollars = Decimal("0")
    coins = Decimal("0")

    with open(file_name, "r") as f:
        trades = json.load(f)

        for record in trades:
            price = Decimal(record["matecoin_price"])
            if record["bought"]:
                bought = Decimal(record["bought"])
                dollars -= bought * price
                coins += bought
            if record["sold"]:
                sold = Decimal(record["sold"])
                dollars += sold * price
                coins -= sold

    with open("profit.json", "w") as f:
        profit = {
            "earned_money": str(dollars),
            "matecoin_account": str(coins),
        }
        json.dump(profit, f, indent=2)
