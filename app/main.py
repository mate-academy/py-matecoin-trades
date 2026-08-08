import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    profit = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }
    with open(file_name, "r") as file:
        trades = json.load(file)

    for day in trades:
        if day["bought"]:
            profit["earned_money"] -= \
                Decimal(day["matecoin_price"]) * Decimal(day["bought"])
            profit["matecoin_account"] += Decimal(day["bought"])
        if day["sold"]:
            profit["earned_money"] += \
                Decimal(day["matecoin_price"]) * Decimal(day["sold"])
            profit["matecoin_account"] -= Decimal(day["sold"])

    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
