import json
from decimal import Decimal


def calculate_profit(filename: str = "trades.json") -> None:
    with open(filename) as j:
        trades_file = json.load(j)

    earned_money = Decimal("0")
    for operation in trades_file:
        if operation["sold"]:
            earned_money += (Decimal(operation["sold"]) * Decimal(
                operation["matecoin_price"]))
        if operation["bought"]:
            earned_money -= (Decimal(operation["bought"]) * Decimal(
                operation["matecoin_price"]))

    matecoin_account = Decimal("0")
    for operation in trades_file:
        if operation["bought"]:
            matecoin_account += Decimal(operation["bought"])
        if operation["sold"]:
            matecoin_account -= Decimal(operation["sold"])

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
