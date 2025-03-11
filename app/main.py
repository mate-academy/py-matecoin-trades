import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    profit = {"earned_money": Decimal("0"), "matecoin_account": Decimal("0")}

    with open(file_name, "r") as file:
        operations = json.load(file)

    for operation in operations:
        if operation["bought"]:
            profit["matecoin_account"] += Decimal(operation["bought"])
            profit["earned_money"] -= Decimal(operation["bought"]) * Decimal(
                operation["matecoin_price"]
            )
        if operation["sold"]:
            profit["matecoin_account"] -= Decimal(operation["sold"])
            profit["earned_money"] += Decimal(operation["sold"]) * Decimal(
                operation["matecoin_price"]
            )

    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])

    with open("profit.json", "w") as file_name:
        json.dump(profit, file_name, indent=2)
