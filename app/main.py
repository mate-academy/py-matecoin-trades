import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        traders = json.load(file)

    calculating_profit = {"earned_money": 0, "matecoin_account": 0}

    for trades in traders:
        if trades["bought"]:
            calculating_profit["earned_money"] -= \
                (Decimal(trades["bought"]) * Decimal(trades["matecoin_price"]))
            calculating_profit["matecoin_account"] += Decimal(trades["bought"])

        if trades["sold"]:
            calculating_profit["earned_money"] += \
                (Decimal(trades["sold"]) * Decimal(trades["matecoin_price"]))
            calculating_profit["matecoin_account"] -= Decimal(trades["sold"])

    for key, value in calculating_profit.items():
        calculating_profit[key] = str(value)

    with open("profit.json", "w") as file:
        json.dump(calculating_profit, file, indent=2)
