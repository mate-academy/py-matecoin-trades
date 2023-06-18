import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(filename, "r", encoding="utf-8") as operations_file:
        operations = json.load(operations_file)
    for operation in operations:
        if operation["bought"]:
            earned_money -= (Decimal(operation["bought"])
                             * Decimal(operation["matecoin_price"]))
            matecoin_account += Decimal(operation["bought"])
        if operation["sold"]:
            earned_money += (Decimal(operation["sold"])
                             * Decimal(operation["matecoin_price"]))
            matecoin_account -= Decimal(operation["sold"])

        with open("profit.json", "w", encoding="utf-8") as profit_file:
            profit = {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            }
            json.dump(profit, profit_file, indent=2)
