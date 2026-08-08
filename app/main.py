import decimal

import json


def calculate_profit(trades):
    sum_bought_coin = 0
    sum_sold_coin = 0
    sum_spent = 0
    sum_earned = 0

    with open(trades) as f:
        trades_list = json.load(f)

    for key in trades_list:
        if key["bought"]:
            sum_spent += decimal.Decimal(key["bought"])\
                * decimal.Decimal(key["matecoin_price"])
            sum_bought_coin += decimal.Decimal(key["bought"])

        if key["sold"]:
            sum_earned += decimal.Decimal(key["sold"])\
                * decimal.Decimal(key["matecoin_price"])
            sum_sold_coin += decimal.Decimal(key["sold"])

    nativ_data = {
        "earned_money": str(sum_earned - sum_spent),
        "matecoin_account": str(sum_bought_coin - sum_sold_coin)
    }

    with open("profit.json", "w") as n:
        json.dump(nativ_data, n, indent=2)
