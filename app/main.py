import json
from decimal import Decimal


def calculate_profit(trades_file_name: str) -> None:
    with open(trades_file_name, "r") as trades_file:
        trades = json.load(trades_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        bought = Decimal(trade["bought"] or 0)
        sold = Decimal(trade["sold"] or 0)
        volume = bought - sold

        matecoin_account += volume
        earned_money -= volume * price

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
