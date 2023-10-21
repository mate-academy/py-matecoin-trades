import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    with open(file_name, "r") as file:
        json_file = json.load(file)

    earned_money = 0
    matecoin_account = 0

    for item in json_file:
        if item["bought"]:
            matecoin_account += Decimal(item["bought"])
            earned_money -= (Decimal(item["matecoin_price"])
                             * Decimal(item["bought"]))
        if item["sold"]:
            matecoin_account -= Decimal(item["sold"])
            earned_money += (Decimal(item["matecoin_price"])
                             * Decimal(item["sold"]))

    trade_result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as result_file:
        json.dump(trade_result, result_file, indent=2)
