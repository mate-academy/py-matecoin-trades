import json
from decimal import Decimal


def calculate_profit(file_name: str) -> json:
    with open(file_name, "r") as json_file:
        deals = json.load(json_file)

    money = 0
    account = 0
    for deal in deals:
        if deal["bought"]:
            money -= Decimal(deal["bought"]) * Decimal(deal["matecoin_price"])
            account += Decimal(deal["bought"])
        if deal["sold"]:
            money += Decimal(deal["sold"]) * Decimal(deal["matecoin_price"])
            account -= Decimal(deal["sold"])

    profit = {"earned_money": str(money),
              "matecoin_account": str(account)}

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
