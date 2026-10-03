from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        data = json.load(file)

    profits = [0, 0]
    for item in data:
        if "matecoin_price" in item:
            if "bought" in item and item["bought"] is not None:
                profits[0] -= (
                    Decimal(item["bought"]) * Decimal(item["matecoin_price"])
                )
                profits[1] += Decimal(item["bought"])

            if "sold" in item and item["sold"] is not None:
                profits[0] += (
                    Decimal(item["sold"]) * Decimal(item["matecoin_price"])
                )
                profits[1] -= Decimal(item["sold"])

    with open("profit.json", "w") as file:
        json.dump({
            "earned_money": str(profits[0]),
            "matecoin_account": str(profits[1])
        }, file, indent=2)
