import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        data = json.load(f)
    result_data = {}
    earned_money = Decimal(0.0)
    matecoin_account = Decimal(0.0)

    for item in data:
        if item["bought"] is not None:
            earned_money -= (Decimal(item["bought"])
                             * Decimal(item["matecoin_price"]))
            matecoin_account += Decimal(item["bought"])

        if item["sold"] is not None:
            earned_money += (Decimal(item["sold"])
                             * Decimal(item["matecoin_price"]))
            matecoin_account -= Decimal(item["sold"])

    result_data["earned_money"] = str(earned_money)
    result_data["matecoin_account"] = str(matecoin_account)

    with open("profit.json", "w") as result_file:
        json.dump(result_data, result_file, indent=2)
