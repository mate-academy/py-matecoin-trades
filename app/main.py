import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trade_up = json.load(file)
    profit = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }
    for order in trade_up:
        if order["bought"] is not None:
            profit["matecoin_account"] += Decimal(order["bought"])
            profit["earned_money"] -= (
                Decimal(order["matecoin_price"]) * Decimal(order["bought"])
            )
        if order["sold"] is not None:
            profit["matecoin_account"] -= Decimal(order["sold"])
            profit["earned_money"] += (
                Decimal(order["matecoin_price"]) * Decimal(order["sold"])
            )
    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])
    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
