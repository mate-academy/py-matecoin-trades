import json
from decimal import Decimal


def calculate_profit(json_file_name):
    with open(json_file_name) as file:
        file_content = json.load(file)

    coins_amount = Decimal("0")
    profit = Decimal("0")

    for deal in file_content:
        if deal["bought"]:
            coins_amount += Decimal(deal["bought"])
            profit -= Decimal(deal["bought"]) * Decimal(deal["matecoin_price"])
        if deal["sold"]:
            coins_amount -= Decimal(deal["sold"])
            profit += Decimal(deal["sold"]) * Decimal(deal["matecoin_price"])

    dict_for_json = {
        "earned_money": str(profit),
        "matecoin_account": str(coins_amount)
    }

    with open("profit.json", "w") as output_file:
        json.dump(dict_for_json, output_file, indent=2)
