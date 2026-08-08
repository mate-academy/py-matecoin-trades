import json
from decimal import Decimal
import os


def calculate_profit(trades: str) -> None:
    with open(trades, "r") as file:
        trades_new = json.load(file)

    money = Decimal("0")
    coins = Decimal("0")
    for trade in trades_new:
        if trade["bought"] is not None:
            coins += Decimal(trade["bought"])
            money -= (Decimal(trade["bought"])
                      * Decimal(trade["matecoin_price"]))
        if trade["sold"] is not None:
            coins -= Decimal(trade["sold"])
            money += (Decimal(trade["sold"])
                      * Decimal(trade["matecoin_price"]))

    profit = {
        "earned_money": str(money),
        "matecoin_account": str(coins)
    }
    root_dir = os.path.dirname(os.path.dirname(trades))
    profit_path = os.path.join(root_dir, "profit.json")

    with open(profit_path, "w") as file:
        json.dump(profit, file, indent=2)
