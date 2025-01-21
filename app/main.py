import json
from decimal import Decimal


def calculate_profit(jsonfile: str):
    with open(jsonfile, "r") as f:
        jsondata = json.load(f)
    sum_bought = Decimal(0)
    sum_sold = Decimal(0)
    metacoin_account = Decimal(0)
    for i in jsondata:
        if i["bought"] is not None:
            sum_bought += Decimal(i["bought"]) * Decimal(i["matecoin_price"])
            print(sum_bought)
            metacoin_account += Decimal(i["bought"])
        if i["sold"] is not None:
            sum_sold += Decimal(i["sold"]) * Decimal(i["matecoin_price"])
            print(sum_sold)
            metacoin_account -= Decimal(i["sold"])
    profit_json = {
        "earned_money": str(sum_sold - sum_bought),
        "matecoin_account": str(metacoin_account),
    }
    with open("profit.json", "w") as profit:
        json.dump(profit_json, profit, indent=2)
