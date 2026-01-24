import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    with open("trades.json", "r") as file:
        trades = json.load(file)

    profit = {"earned_money": Decimal("0"), "matecoin_account": Decimal("0")}

    for trade in trades:
        if trade["bought"] is not None:
            profit["matecoin_account"] += Decimal(trade["bought"])
            profit["earned_money"] -= (Decimal(trade["bought"])
                                       * Decimal(trade["matecoin_price"]))
        elif trade["sold"] is not None:
            profit["matecoin_account"] -= Decimal(trade["sold"])
            profit["earned_money"] -= (Decimal(trade["sold"])
                                       * Decimal(trade["matecoin_price"]))

    profit_str = {key: str(value) for key, value in profit.items()}

    with open("profit.json", "w") as file:
        profit = json.dump(profit_str, file)
