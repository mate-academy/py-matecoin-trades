import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as trades_file:
        trades = json.load(trades_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            earned_money -= bought * price
            matecoin_account += bought

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            earned_money += sold * price
            matecoin_account -= sold

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as profit_file:
        json.dump(profit, profit_file, indent=2)
