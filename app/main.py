import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
    mate_coin = 0
    balance = 0

    for item in data:
        if item["bought"]:
            mate_coin += Decimal(item["bought"])
            balance -= (Decimal(item["bought"])
                        * Decimal(item["matecoin_price"]))
        if item["sold"]:
            mate_coin -= Decimal(item["sold"])
            balance += Decimal(item["sold"]) * Decimal(item["matecoin_price"])
    result = {"earned_money": str(balance), "matecoin_account": str(mate_coin)}
    with open("profit.json", "w") as json_file:
        json.dump(result, json_file, indent=2)
