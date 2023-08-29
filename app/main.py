import json
from decimal import Decimal


def calculate_profit(name: str) -> None:
    with open(name, "r") as f:
        data = json.load(f)

    earned_money = 0
    matecoin_account = 0

    for operation in data:
        if operation["bought"]:
            earned_money -= Decimal(
                operation["bought"]
            ) * Decimal(operation["matecoin_price"])
            matecoin_account += Decimal(operation["bought"])
        if operation["sold"]:
            earned_money += Decimal(
                operation["sold"]
            ) * Decimal(operation["matecoin_price"])
            matecoin_account -= Decimal(operation["sold"])

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
