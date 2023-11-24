import json

from decimal import Decimal


def calculate_profit(trades: str) -> None:
    with open(trades) as file:
        data = json.load(file)

    matecoin_bought = Decimal("0")
    matecoin_sold = Decimal("0")
    matecoin_amount = Decimal("0")

    for operation in data:
        price = Decimal(operation["matecoin_price"])
        if operation["bought"]:
            matecoin_bought += Decimal(operation["bought"]) * price
            matecoin_amount += Decimal(operation["bought"])
        if operation["sold"]:
            matecoin_sold += Decimal(operation["sold"]) * price
            matecoin_amount -= Decimal(operation["sold"])

    profit_dict = {
        "earned_money": str(Decimal(matecoin_sold) - Decimal(matecoin_bought)),
        "matecoin_account": str(matecoin_amount),
    }

    with open("profit.json", "w") as json_file:
        json.dump(profit_dict, json_file, indent=2)
