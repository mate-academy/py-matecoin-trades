import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    profit = Decimal(0)
    money = Decimal(0)

    with open(filename, "r") as f:
        trades = json.load(f)

    for trade in trades:
        if trade["bought"]:
            profit = Decimal(Decimal(profit) - Decimal(trade["bought"]))
            money = Decimal(money) - (Decimal(trade["bought"])
                                      * Decimal(trade["matecoin_price"]))
        if trade["sold"]:
            profit = Decimal(Decimal(profit) + Decimal(trade["sold"]))
            money = Decimal(money) + (Decimal(trade["sold"])
                                      * Decimal(trade["matecoin_price"]))

    with open("profit.json", "w") as f:
        json.dump({
            "earned_money": str(money),
            "matecoin_account": str(profit * -1)
        }, f, indent=2)
