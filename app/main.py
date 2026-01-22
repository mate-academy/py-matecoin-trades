from decimal import Decimal
import json


def calculate_profit(name_of_file: str) -> None:
    with open(name_of_file, "r") as f:
        info = json.load(f)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for operation in info:
        if operation["bought"] is not None:
            matecoin_account += Decimal(operation["bought"])
            earned_money -= (Decimal(operation["bought"])
                             * Decimal(operation["matecoin_price"]))

        if operation["sold"] is not None:
            matecoin_account -= Decimal(operation["sold"])
            earned_money += (Decimal(operation["sold"])
                             * Decimal(operation["matecoin_price"]))

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)
