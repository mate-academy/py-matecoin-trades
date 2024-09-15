import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        data = json.load(file)

    matecoin_account = 0
    profit = 0
    for value in data:
        if value["bought"]:
            profit -= (Decimal(value["bought"])
                       * Decimal(value["matecoin_price"]))
            matecoin_account += Decimal(value["bought"])
        if value["sold"]:
            profit += (Decimal(value["sold"])
                       * Decimal(value["matecoin_price"]))
            matecoin_account -= Decimal(value["sold"])

    result = {"earned_money": str(profit),
              "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
