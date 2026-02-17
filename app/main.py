import json
from decimal import Decimal


def calculate_profit(trades_path: str) -> None:

    with open(trades_path, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= price * bought

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += price * sold

    total = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)

    }

    with open("profit.json", "w") as f:
        json.dump(total, f, indent=2)
