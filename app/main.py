import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    with open(trades, "r") as read_f:
        data = json.load(read_f)
    earned_money = 0
    matecoin_account = 0
    for trade in data:
        if trade["bought"] is not None:
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account += Decimal(trade["bought"])
        if trade["sold"] is not None:
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account -= Decimal(trade["sold"])
    profit = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as write_f:
        json.dump(profit, write_f, indent=2)
