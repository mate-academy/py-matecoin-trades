import decimal

import json


def calculate_profit(name_of_file: str) -> None:
    with open(name_of_file, "r") as file:
        operations = json.load(file)

    count_matecoin = decimal.Decimal("0")
    earned_money = decimal.Decimal("0")
    for operation in operations:
        matecoint_price = decimal.Decimal(operation["matecoin_price"])
        if operation["bought"]:
            bought_money = decimal.Decimal(
                operation["bought"]
            ) * matecoint_price
            earned_money -= bought_money
            count_matecoin += decimal.Decimal(operation["bought"])
        if operation["sold"]:
            sold_money = decimal.Decimal(operation["sold"]) * matecoint_price
            earned_money += sold_money
            count_matecoin -= decimal.Decimal(operation["sold"])

    profit = dict()

    profit["earned_money"] = str(earned_money)
    profit["matecoin_account"] = str(count_matecoin)

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
