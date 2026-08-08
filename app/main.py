from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        info = json.load(file)
    new_info, earned_money, matecoin_account = {}, Decimal(0.0), Decimal(0.0)
    for trans in info:
        if trans["bought"] is not None:
            earned_money -= \
                Decimal(trans["bought"]) * Decimal(trans["matecoin_price"])
            matecoin_account += Decimal(trans["bought"])

        if trans["sold"] is not None:
            earned_money += \
                Decimal(trans["sold"]) * Decimal(trans["matecoin_price"])
            matecoin_account -= Decimal(trans["sold"])

    new_info["earned_money"] = str(earned_money)
    new_info["matecoin_account"] = str(matecoin_account)

    with open("profit.json", "w") as file:
        json.dump(new_info, file, indent=2)
