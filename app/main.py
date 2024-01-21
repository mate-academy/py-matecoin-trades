import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file_in, open("profit.json", "w") as file_out:
        json_data = json.load(file_in)
        earned_money = 0
        matecoin_account = 0

        for data in json_data:
            if data["bought"]:
                matecoin_account += Decimal(data["bought"])
                earned_money -= Decimal(data["bought"]) \
                    * Decimal(data["matecoin_price"])
            if data["sold"]:
                matecoin_account -= Decimal(data["sold"])
                earned_money += Decimal(data["sold"]) \
                    * Decimal(data["matecoin_price"])

        res = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        json.dump(res, file_out, indent=2)
