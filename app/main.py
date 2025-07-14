import json
from decimal import Decimal


def calculate_profit(json_file: str) -> None:
    with open(json_file, "r") as file:
        operation_dict = json.load(file)

    your_money = Decimal("0")
    matecoin_wallet = Decimal("0")

    for operation in operation_dict:
        if operation["bought"]:
            your_money -= (Decimal(operation["bought"])
                           * Decimal(operation["matecoin_price"]))
            matecoin_wallet += Decimal(operation["bought"])
        if operation["sold"]:
            your_money += (Decimal(operation["sold"])
                           * Decimal(operation["matecoin_price"]))
            matecoin_wallet -= Decimal(operation["sold"])

    return_dict = {"earned_money": str(your_money),
                   "matecoin_account": str(matecoin_wallet)}

    with open("../profit.json", "w") as file:
        json.dump(return_dict, file, indent=2)
