import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal("0")
    amount_of_coins = Decimal("0")
    with open(file_name, "r") as file:
        trades = json.load(file)
    for trade in trades:
        if trade.get("bought"):
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))

            amount_of_coins += Decimal(trade["bought"])
        if trade.get("sold"):
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))

            amount_of_coins -= Decimal(trade["sold"])
    with open("profit.json", "w") as result:
        json.dump({
            "earned_money": str(earned_money),
            "matecoin_account": str(amount_of_coins)
        }, result, indent=2)
