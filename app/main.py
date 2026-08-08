import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    profit = 0
    current_coin = 0

    for day in trades:
        bought = Decimal(day["bought"]) \
            if not day["bought"] is None else Decimal("0")
        sold = Decimal(day["sold"]) \
            if not day["sold"] is None else Decimal("0")
        current_price = Decimal(day["matecoin_price"])
        current_coin += bought
        current_coin -= sold
        profit -= bought * current_price
        profit += sold * current_price

    data = {
        "earned_money": str(profit),
        "matecoin_account": str(current_coin)
    }
    with open("profit.json", "w") as file:
        json.dump(data, file, indent=2)
