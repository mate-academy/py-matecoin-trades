import json
from decimal import Decimal


def calculate_profit(input_file: str) -> None:
    print(input_file)
    with open(input_file, "r") as data_file:
        data = json.load(data_file)

    if not data:
        return None

    total = {"earned_money": Decimal(0), "matecoin_account": Decimal(0)}

    for item in data:
        if item["bought"] is not None:
            total["earned_money"] -= Decimal(item["bought"]) * Decimal(
                item["matecoin_price"])
            total["matecoin_account"] += Decimal(item["bought"])
        if item["sold"] is not None:
            total["earned_money"] += Decimal(item["sold"]) * Decimal(
                item["matecoin_price"])
            total["matecoin_account"] -= Decimal(item["sold"])

    total["earned_money"] = str(total["earned_money"])
    total["matecoin_account"] = str(total["matecoin_account"])

    with open("profit.json", "w") as result_file:
        json.dump(total, result_file, indent=2)


# print(calculate_profit("trades.json"))
