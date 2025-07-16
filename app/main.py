import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        data_orders = json.load(file)

    count = Decimal("0")
    profit = Decimal("0")

    for order in data_orders:
        if order["bought"]:
            count += Decimal(order["bought"])
            profit -= (Decimal(order["bought"])
                       * Decimal(order["matecoin_price"]))
        if order["sold"]:
            count -= Decimal(order["sold"])
            profit += Decimal(order["sold"]) * Decimal(order["matecoin_price"])

    result = {
        "earned_money": str(profit),
        "matecoin_account": str(count)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
