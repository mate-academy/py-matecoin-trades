import json
from decimal import Decimal


def calculate_profit(file_name: str):
    with open(file_name, "r") as t:
        trades = json.load(t)

    print(trades)
    profit = {"earned_money": 0, "matecoin_account": 0}

    for account in trades:
        if account["bought"]:
            profit["earned_money"] += \
                Decimal(account["bought"]) * Decimal(account["matecoin_price"])
            profit["matecoin_account"] += Decimal(account["bought"])

        elif account["sold"]:
            profit["earned_money"] -= \
                Decimal(account["sold"]) * Decimal(account["matecoin_price"])
            profit["matecoin_account"] -= Decimal(account["sold"])

    profit["earned_money"] = float(profit["earned_money"])
    profit["matecoin_account"] = float(profit["matecoin_account"])

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
