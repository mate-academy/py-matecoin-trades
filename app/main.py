import json
from decimal import Decimal


def calculate_profit(file_name: str):
    sum_earned_money = 0
    sum_spent_money = 0
    sum_bought_coins = 0
    sum_sold_coins = 0

    with open(file_name) as f:
        trades_list = json.load(f)

        for key in trades_list:
            if key["bought"]:
                sum_spent_money += \
                    Decimal(key["bought"]) * Decimal(key["matecoin_price"])
                sum_bought_coins += Decimal(key["bought"])

            if key["sold"]:
                sum_earned_money += \
                    Decimal(key["sold"]) * Decimal(key["matecoin_price"])
                sum_sold_coins += Decimal(key["sold"])

    native_data = {
        "earned_money": str(sum_earned_money - sum_spent_money),
        "matecoin_account": str(sum_bought_coins - sum_sold_coins),
    }
    with open("profit.json", "w") as f:
        json.dump(native_data, f, indent=2)
