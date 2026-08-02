import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(trades_file, "r") as source_file:
        trades = json.load(source_file)

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * price

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * price

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }
    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
