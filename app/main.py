import json
from decimal import Decimal


def calculate_profit(filename: str = "trades.json") -> None:

    with open(filename) as f:
        trades = json.load(f)

    total_money = Decimal("0")
    total_matecoin = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            total_money -= bought * price
            total_matecoin += bought

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            total_money += sold * price
            total_matecoin -= sold

    result = {
        "earned_money": str(total_money),
        "matecoin_account": str(total_matecoin)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
