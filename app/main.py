from __future__ import annotations

import decimal
import json


def calculate_profit(traders_data: json) -> None:
    sell_coins = 0
    bought_coins = 0
    sell_money = 0
    bought_money = 0
    with open(traders_data) as traders_info:
        user_data = json.load(traders_info)
        for money in user_data:
            if money["bought"]:
                bought_coins += decimal.Decimal(money["bought"])
                sell_money += (decimal.Decimal(money["bought"])
                               * decimal.Decimal(money["matecoin_price"]))
            if money["sold"]:
                sell_coins += decimal.Decimal(money["sold"])
                bought_money += (decimal.Decimal(money["sold"])
                                 * decimal.Decimal(money["matecoin_price"]))

    result = {
        "earned_money": str(bought_money - sell_money),
        "matecoin_account": str(bought_coins - sell_coins)
    }

    with open("profit.json", "w") as profit:
        json.dump(result, profit, indent=2)
