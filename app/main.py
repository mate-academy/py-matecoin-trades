import os
from decimal import Decimal
import json


def calculate_profit(file_name_json: str) -> None:

    file_path = os.path.join(os.path.dirname(__file__), file_name_json)
    with open(file_path, "r") as file:
        data = json.load(file)
        matecoin_account = 0
        earned_money = 0
    for item in data:
        if item["bought"] is not None:
            matecoin_account += Decimal(item["bought"])
            earned_money -= (
                Decimal(item["bought"]) * Decimal(item["matecoin_price"]))
        if item["sold"] is not None:
            matecoin_account -= Decimal(item["sold"])
            earned_money += (
                Decimal(item["sold"]) * Decimal(item["matecoin_price"]))

    result_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }
    with open("profit.json", "w") as file:
        json.dump(result_dict, file, indent=2)


calculate_profit("trades.json")
