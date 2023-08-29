import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        data = json.load(f)
    result = {}
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

    result["earned_money"] = str(earned_money)
    result["matecoin_account"] = str(matecoin_account)

    with open("profit.json", "w") as new_f:
        json.dump(result, new_f, indent=2)
