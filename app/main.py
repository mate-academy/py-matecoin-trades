import decimal
import json


def calculate_profit(filename: str) -> None:
    earned_money = decimal.Decimal(0)
    matecoin_account = decimal.Decimal(0)
    profit = {}

    with open(filename, "r") as json_file:
        data = json.load(json_file)

    for operation in data:
        price = decimal.Decimal(operation["matecoin_price"])
        if operation["bought"]:
            bought = decimal.Decimal(operation["bought"])
            matecoin_account += bought
            earned_money -= bought * price

        if operation["sold"]:
            sold = decimal.Decimal(operation["sold"])
            matecoin_account -= sold
            earned_money += sold * price

    profit["earned_money"] = f"{earned_money}"
    profit["matecoin_account"] = f"{matecoin_account}"

    with open("profit.json", "w") as json_file:
        json.dump(profit, json_file, indent=2)
