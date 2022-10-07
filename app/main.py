import decimal

import json


def calculate_profit(name: str) -> None:
    with open(f"{name}", "r") as f:
        data = json.load(f)

    total_bought = 0
    total_sold = 0
    cost_bought = 0
    cost_sold = 0
    for element in data:
        if element["bought"] is not None:
            total_bought += decimal.Decimal(element["bought"])
            cost_bought += (decimal.Decimal(element["bought"])
                            * decimal.Decimal(element["matecoin_price"]))
        if element["sold"] is not None:
            total_sold += decimal.Decimal(element["sold"])
            cost_sold += (decimal.Decimal(element["sold"])
                          * decimal.Decimal(element["matecoin_price"]))

    total_profit = cost_sold - cost_bought
    account_left = total_bought - total_sold

    dictionary = {
        "earned_money": str(total_profit),
        "matecoin_account": str(account_left)
    }

    with open("profit.json", "w") as json_file:
        json.dump(dictionary, json_file, indent=2)
