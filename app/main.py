import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = 0
    matecoin_account = 0
    with (open(file_name) as f):
        file_with_trade = json.load(f)
        for dict1 in file_with_trade:
            if dict1["bought"] is None:
                dict1["bought"] = 0

            if dict1["sold"] is None:
                dict1["sold"] = 0

            earned_money = earned_money - \
                Decimal(dict1["bought"]) * Decimal(dict1["matecoin_price"]) + \
                (Decimal(dict1["sold"]) * Decimal(dict1["matecoin_price"]))

            matecoin_account = matecoin_account + \
                (Decimal(dict1["bought"]) - Decimal(dict1["sold"]))

    to_json = {"earned_money": str(earned_money),
               "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as f:
        json.dump(to_json, f, indent=2)
