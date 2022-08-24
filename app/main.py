import json
from decimal import Decimal


def calculate_profit(name):
    with open(f"{name}") as f:
        trades_data = json.load(f)
    for i in trades_data:
        if i["bought"] is None:
            i["bought"] = 0
        if i["sold"] is None:
            i["sold"] = 0

    matecoin_account = 0
    earned_money = 0
    for i in trades_data:
        matecoin_account += Decimal(i["bought"]) - Decimal(i["sold"])
        earned_money += \
            ((Decimal(i["sold"]) - Decimal(
                i["bought"])) * Decimal(i["matecoin_price"]))

    dict_result = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}

    r = open("profit.json", "w")
    json.dump(dict_result, r, indent=2)
