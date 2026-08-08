import json
from decimal import Decimal
import os


def calculate_profit(name_file):
    path = os.path.abspath(name_file)
    with open(path, "r") as file:
        trade_info = json.load(file)
    calculate_profit = {"earned_money": Decimal(0),
                        "matecoin_account": Decimal(0)}
    for i in trade_info:
        if i["bought"]:
            calculate_profit["matecoin_account"] += Decimal(i["bought"])
            costs = Decimal(i["bought"]) * Decimal(i["matecoin_price"])
            calculate_profit["earned_money"] -= costs

        if i["sold"]:
            calculate_profit["matecoin_account"] -= Decimal(i["sold"])
            calculate_profit["earned_money"] += \
                Decimal(i["sold"]) * Decimal(i["matecoin_price"])

    calculate_pro = {key: str(value)
                     for key, value in calculate_profit.items()}

    with open("profit.json", "w") as profit_calc:
        json.dump(calculate_pro, profit_calc, indent=2)
