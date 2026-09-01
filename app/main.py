import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(filename, "r", encoding="utf-8") as trades_file:
        trades = json.load(trades_file)

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought_coins = Decimal(trade["bought"])
            matecoin_account += bought_coins
            earned_money -= bought_coins * matecoin_price

        if trade["sold"] is not None:
            sold_coins = Decimal(trade["sold"])
            matecoin_account -= sold_coins
            earned_money += sold_coins * matecoin_price

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as profit_file:
        json.dump(profit, profit_file, indent=2)
