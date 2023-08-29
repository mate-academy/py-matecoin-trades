import json
from decimal import Decimal


def calculate_profit(file_name: str) -> str:
    with open(f"{file_name}", "r") as file:
        data = json.load(file)

    earned_money = 0
    matecoin_account = 0

    for item in data:

        if item["bought"]:
            earned_money -= Decimal(item["bought"]) * Decimal(
                item["matecoin_price"])
            matecoin_account += Decimal(item["bought"])

        if item["sold"]:
            earned_money += Decimal(item["sold"]) * Decimal(
                item["matecoin_price"])
            matecoin_account -= Decimal(item["sold"])

    result_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as json_file:
        json.dump(result_dict, json_file, indent=2)
