from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    profit = Decimal("0")
    matecoin_account = Decimal("0")

    with open(filename, "r") as source_file:
        data_json = json.load(source_file)

        for operation in data_json:
            if operation["bought"]:
                profit -= (Decimal(operation["bought"])
                           * Decimal(operation["matecoin_price"]))
                matecoin_account += Decimal(operation["bought"])

            if operation["sold"]:
                profit += (Decimal(operation["sold"])
                           * Decimal(operation["matecoin_price"]))
                matecoin_account -= Decimal(operation["sold"])

    data = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as destination_file:
        json.dump(data, destination_file, indent=2)
