import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        data = json.load(file)
    profit = Decimal("0.0")
    balance = Decimal("0.0")
    for dict_json in data:
        if dict_json["bought"]:
            bought = Decimal(dict_json["bought"])
            balance += bought
            profit -= bought * Decimal(dict_json["matecoin_price"])
        if dict_json["sold"]:
            sold = Decimal(dict_json["sold"])
            balance -= sold
            profit += sold * Decimal(dict_json["matecoin_price"])
    profit_dict = {
        "earned_money": str(profit),
        "matecoin_account": str(balance)
    }
    with open("profit.json", "w") as file:
        json.dump(profit_dict, file, indent=2)
