import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades_dict = json.load(f)

    earned_money = 0
    matecoin_account = 0

    for operation in trades_dict:
        price = Decimal(operation["matecoin_price"])

        if operation["bought"]:
            matecoin_account += Decimal(operation["bought"])
            earned_money -= Decimal(operation["bought"]) * price

        if operation["sold"]:
            matecoin_account -= Decimal(operation["sold"])
            earned_money += Decimal(operation["sold"]) * price

        profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as f:
            json.dump(profit, f, indent=2)
