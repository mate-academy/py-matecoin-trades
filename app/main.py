from decimal import Decimal

import json


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        data = json.load(f)

    bought_coins_money = 0
    sold_coins_money = 0
    current_coin_account = 0

    for item in data:
        price_1_matecoin = Decimal(item["matecoin_price"])

        if item["bought"] is not None:
            bought_coins_money += (Decimal(item["bought"]) * price_1_matecoin)
            current_coin_account += Decimal(item["bought"])
        if item["sold"] is not None:
            sold_coins_money += (Decimal(item["sold"]) * price_1_matecoin)
            current_coin_account -= (Decimal(item["sold"]))

    balance = sold_coins_money - bought_coins_money

    result_dict = {
        "earned_money": str(balance),
        "matecoin_account": str(current_coin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result_dict, f, indent=2)
