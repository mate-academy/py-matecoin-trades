import json
from decimal import Decimal


def calculate_profit(file_name: str) -> json:
    with open(file_name, "r") as json_file:
        operations = json.load(json_file)

    money = 0
    account = 0
    for op in operations:
        if op["bought"]:
            money -= Decimal(op["bought"]) * Decimal(op["matecoin_price"])
            account += Decimal(op["bought"])
        if op["sold"]:
            money += Decimal(op["sold"]) * Decimal(op["matecoin_price"])
            account -= Decimal(op["sold"])

    profit = {"earned_money": str(money),
              "matecoin_account": str(account)}

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
