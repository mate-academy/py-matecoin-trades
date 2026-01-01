from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    res_dict = {}
    dicts = {}
    sold = Decimal("0")
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(file_name, "r") as f:
        dicts = json.load(f)

    for something in dicts:
        price = Decimal(something["matecoin_price"])
        if something["bought"]:
            amount = Decimal(something["bought"])
            matecoin_account += amount
            earned_money -= amount * price
        if something["sold"]:
            amount = Decimal(something["sold"])
            sold += Decimal(something["sold"])
            matecoin_account -= amount
            earned_money += amount * price

    res_dict["earned_money"] = str(earned_money)
    res_dict["matecoin_account"] = str(matecoin_account)

    with open("profit.json", "w") as f:
        json.dump(res_dict, f, indent=2)
