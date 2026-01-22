import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(trades_file, "r") as file:
        trades = json.load(file)

    for operation in trades:
        if operation["bought"]:
            matecoin_account += Decimal(operation["bought"])
            earned_money -= Decimal(operation["bought"]) * Decimal(
                operation["matecoin_price"])

        if operation["sold"]:
            matecoin_account -= Decimal(operation["sold"])
            earned_money += Decimal(operation["sold"]) * Decimal(
                operation["matecoin_price"])

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
