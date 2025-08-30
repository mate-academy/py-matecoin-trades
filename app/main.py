import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:

    # Result dict
    result = {"Earned money": [], "bought": [], "sold": []}

    # Open json
    with open(filename, "r") as file:
        data = json.load(file)

    # Operation with iteration value in json
    for operation in data:
        bought = operation.get("bought")
        sold = operation.get("sold")
        matecoin_price = operation.get("matecoin_price")
        result["Earned money"].append(
            (
                Decimal(sold or 0) - Decimal(bought or 0)
            ) * Decimal(matecoin_price)
        )
        result["bought"].append(Decimal(bought or 0))
        result["sold"].append(Decimal(sold or 0))

    # Write JSON file
    with open("profit.json", "w") as file:
        json.dump({
            "earned_money": str(sum(result["Earned money"])),
            "matecoin_account": str(
                sum(result["bought"]) - sum(result["sold"])
            )
        },
            file, indent=2)
