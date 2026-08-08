import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        transactions = json.load(file)

    result = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    for transaction in transactions:
        if transaction["bought"]:
            bought = Decimal(transaction["bought"])
            matecoin_price = Decimal(transaction["matecoin_price"])
            result["matecoin_account"] += bought
            result["earned_money"] -= bought * matecoin_price

        if transaction["sold"]:
            sold = Decimal(transaction["sold"])
            matecoin_price = Decimal(transaction["matecoin_price"])
            result["matecoin_account"] -= sold
            result["earned_money"] += sold * matecoin_price

    result["earned_money"] = str(result["earned_money"])
    result["matecoin_account"] = str(result["matecoin_account"])

    with open("profit.json", "w") as json_file:
        json.dump(result, json_file, indent=2)
