import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        list_dict_info = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for dict_info in list_dict_info:
        matecoin_price = Decimal(dict_info["matecoin_price"])
        if dict_info["bought"]:
            bought = Decimal(dict_info["bought"])
            matecoin_account += bought
            earned_money -= bought * matecoin_price
        if dict_info["sold"]:
            sold = Decimal(dict_info["sold"])
            matecoin_account -= sold
            earned_money += sold * matecoin_price

    profit_dict = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as file:
        json.dump(profit_dict, file, indent=2)
