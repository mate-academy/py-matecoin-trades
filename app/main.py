import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file_in:
        data = json.load(file_in)

    new_data = {}

    for item in data:
        if item["bought"] is None:
            item["bought"] = "0.0"
        if item["sold"] is None:
            item["sold"] = "0.0"

    new_data["earned_money"] = str(
        sum(
            (Decimal(elem["sold"]) - Decimal(elem["bought"]))
            * Decimal(elem["matecoin_price"])
            for elem in data
        )
    )
    new_data["matecoin_account"] = str(
        sum(Decimal(elem["bought"]) - Decimal(elem["sold"]) for elem in data)
    )

    with open("profit.json", "w") as file_out:
        json.dump(new_data, file_out, indent=2)
