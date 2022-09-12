import json

import decimal


def calculate_profit(name_f):
    with open(name_f, "r") as f:
        data = json.load(f)
    earned_money, matecoin_account = 0, 0
    for i in data:
        change = decimal.Decimal(i["matecoin_price"])
        if "bought" in i and i["bought"] is not None:
            earned_money -= decimal.Decimal(i["bought"]) * change
            matecoin_account += decimal.Decimal(i["bought"])
        if "sold" in i and i["sold"] is not None:
            earned_money += decimal.Decimal(i["sold"]) * change
            matecoin_account -= decimal.Decimal(i["sold"])
    new_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(new_dict, f, indent=2)
