import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades_data = json.load(file)

    bought = sum(
        Decimal(item["bought"]) * Decimal(item["matecoin_price"])
        for item in trades_data
        if item.get("bought") is not None
        and item.get("matecoin_price") is not None
    )

    sold = sum(
        Decimal(item["sold"]) * Decimal(item["matecoin_price"])
        for item in trades_data
        if item.get("sold") is not None
        and item.get("matecoin_price") is not None
    )

    total_matecoin = sum(
        (Decimal(item["bought"]) if item.get("bought") is not None
         else Decimal(0))
        - (Decimal(item["sold"]) if item.get("sold") is not None
           else Decimal(0))
        for item in trades_data
    )

    dict_to_json = {
        "earned_money": str(sold - bought),
        "matecoin_account": str(total_matecoin)
    }

    with open("profit.json", "w") as json_file:
        json.dump(dict_to_json, json_file, indent=2)
