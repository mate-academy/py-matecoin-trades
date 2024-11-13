import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as f:
        trades = json.load(f)
    earned_money = Decimal("0")
    matecoin_price = Decimal("0")
    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            matecoin_price += Decimal(trade["bought"])
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
        elif trade["sold"]:
            matecoin_price -= Decimal(trade["sold"])
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))
    profit_data = {"earned_money": str(earned_money),
                   "matecoin_price": str(matecoin_price)}
    with open("profit.json", "w") as f:
        json.dump(profit_data, f, indent=2)
