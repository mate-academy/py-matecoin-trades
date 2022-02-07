import json
from decimal import Decimal


def calculate_profit(trades_file):
    with open(trades_file) as file:
        users = json.load(file)

    for data in users:
        for key in data.keys():
            if data[key]:
                data[key] = Decimal(data[key])

    bought_sum = sum([val["bought"] for val in users if val["bought"]])
    sold_sum = sum([val["sold"] for val in users if val["sold"]])
    matecoin_total = bought_sum - sold_sum

    bought_money_sum = sum([val["bought"] * val["matecoin_price"] for val in users if val["bought"]])
    sold_money_sum = sum([val["sold"] * val["matecoin_price"] for val in users if val["sold"]])
    earned_total = bought_money_sum - sold_money_sum

    profit_json = {
        "earned_money": str(earned_total),
        "matecoin_account": str(matecoin_total)
    }

    with open("profit.json", "w") as result:
        json.dump(profit_json, result, indent=2)


calculate_profit("trades.json")
