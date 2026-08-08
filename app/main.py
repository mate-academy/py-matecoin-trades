from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    earned_money = 0
    matecoin_account = 0
    with open(file_name, "r") as json_file:
        for line in json.load(json_file):
            if line["sold"]:
                earned_money += Decimal(
                    line["sold"]
                ) * Decimal(line["matecoin_price"])
                matecoin_account -= Decimal(line["sold"])

            if line["bought"]:
                earned_money -= Decimal(line["bought"]) * Decimal(
                    line["matecoin_price"]
                )
                matecoin_account += Decimal(line["bought"])

    with open("profit.json", "w") as json_file:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account),
            },
            json_file,
            indent=2,
        )
    return None
