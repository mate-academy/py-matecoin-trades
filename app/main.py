import json

import decimal


def calculate_profit(name_f):
    with open(name_f, "r") as f:
        data = json.load(f)
    earned_money, matecoin_account = 0, 0
    for value in data:
        change = decimal.Decimal(value["matecoin_price"])
        if value["bought"]:
            earned_money -= decimal.Decimal(value["bought"]) * change
            matecoin_account += decimal.Decimal(value["bought"])
        if value["sold"]:
            earned_money += decimal.Decimal(value["sold"]) * change
            matecoin_account -= decimal.Decimal(value["sold"])
    new_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(new_dict, f, indent=2)
