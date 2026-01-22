import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        traders_data = json.load(file)

    profit = 0
    volume = 0

    for order in traders_data:
        if order["bought"]:
            profit -= (
                Decimal(order["bought"]) * Decimal(order["matecoin_price"])
            )
            volume += Decimal(order["bought"])
        if order["sold"]:
            profit += (
                Decimal(order["sold"]) * Decimal(order["matecoin_price"])
            )
            volume -= Decimal(order["sold"])

    trading_result = {
        "earned_money": str(profit),
        "matecoin_account": str(volume)
    }

    with open("profit.json", "w") as file:
        json.dump(trading_result, file, indent=2)
