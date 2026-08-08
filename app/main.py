import json
from decimal import Decimal


def calculate_profit(trades_file: json) -> None:
    earned_money = 0
    matecoin_account = 0
    with open(trades_file, "r") as f:
        trades_file = json.load(f)
        for trade in trades_file:
            if trade["bought"]:
                matecoin_account += Decimal(trade["bought"])
                earned_money -= (Decimal(trade["bought"])
                                 * Decimal(trade["matecoin_price"]))
            if trade["sold"]:
                matecoin_account -= Decimal(trade["sold"])
                earned_money += (Decimal(trade["sold"])
                                 * Decimal(trade["matecoin_price"]))
    with open("profit.json", "w") as profit_file:
        json.dump({
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }, profit_file, indent=2)
