import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename) as trades_file:
        trades = json.load(trades_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])
        bought = (
            Decimal(trade["bought"])
            if trade["bought"] is not None
            else Decimal("0")
        )
        sold = (
            Decimal(trade["sold"])
            if trade["sold"] is not None
            else Decimal("0")
        )

        earned_money += sold * matecoin_price
        earned_money -= bought * matecoin_price
        matecoin_account += bought
        matecoin_account -= sold

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
