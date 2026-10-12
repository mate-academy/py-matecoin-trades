import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(filename, encoding="utf-8") as trades_file:
        trades = json.load(trades_file)

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        bought = Decimal(trade["bought"] or "0")
        sold = Decimal(trade["sold"] or "0")

        earned_money += sold * price - bought * price
        matecoin_account += bought - sold

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as profit_file:
        json.dump(profit, profit_file, indent=2)
