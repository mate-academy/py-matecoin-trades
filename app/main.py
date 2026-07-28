import json
from decimal import Decimal


def calculate_profit(json_file: str) -> None:
    with open(json_file) as json_file:
        data = json.load(json_file)

    profit = Decimal("0")
    matecoin_amount = Decimal("0")
    for operation in data:
        if operation["bought"]:
            profit -= (
                Decimal(operation["bought"])
                * Decimal(operation["matecoin_price"])
            )
            matecoin_amount += Decimal(operation["bought"])

        if operation["sold"]:
            profit += (
                Decimal(operation["sold"])
                * Decimal(operation["matecoin_price"])
            )
            matecoin_amount -= Decimal(operation["sold"])

    prepared_data = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin_amount)
    }

    with open("profit.json", "w") as json_file:
        json.dump(prepared_data, json_file, indent=2)
