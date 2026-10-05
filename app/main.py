import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    result = {}

    with open(file_name, "r") as cur_file:
        data = json.load(cur_file)

        earned_money = Decimal("0")
        matecoin_account = Decimal("0")
        for item in data:
            price = Decimal(item["matecoin_price"])

            if item["sold"] is not None:
                earned_money += Decimal(item["sold"]) * price
                matecoin_account -= Decimal(item["sold"])

            if item["bought"] is not None:
                earned_money -= Decimal(item["bought"]) * price
                matecoin_account += Decimal(item["bought"])

        result["earned_money"] = str(earned_money)
        result["matecoin_account"] = str(matecoin_account)

    with open("profit.json", "w") as new_file:
        json.dump(result, new_file, indent=2)
