import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    profit = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    with open(file_name, "r") as source:
        trade_info = json.load(source)

    for info in trade_info:
        if info["bought"]:
            profit["earned_money"] -= \
                (Decimal(info["matecoin_price"]) * Decimal(info["bought"]))
            profit["matecoin_account"] += Decimal(info["bought"])
        if info["sold"]:
            profit["earned_money"] += \
                (Decimal(info["matecoin_price"]) * Decimal(info["sold"]))
            profit["matecoin_account"] -= Decimal(info["sold"])

    for key in profit.keys():
        profit[key] = str(profit[key])

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
