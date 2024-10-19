import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    with open(file_name) as inner_file:
        operations = json.load(inner_file)
        for operation in operations:
            if operation["bought"] is not None:
                earned_money -= Decimal(operation["bought"]) \
                    * Decimal(operation["matecoin_price"])
                matecoin_account += Decimal(operation["bought"])
            if operation["sold"] is not None:
                earned_money += Decimal(operation["sold"]) \
                    * Decimal(operation["matecoin_price"])
                matecoin_account -= Decimal(operation["sold"])

    with open("../profit.json", "w") as outer_file:
        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        json.dump(result, outer_file, indent=2)

